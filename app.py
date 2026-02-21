import io
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, request, render_template, jsonify

# ── Model definition (must match training) ────────────────────────────────────
CLASSES = ['HDPE', 'LDPE', 'Other', 'PET', 'PP', 'PS', 'PVC']

class ImageClassificationBase(nn.Module):
    pass  # inference only – training helpers not needed

class ResNet(ImageClassificationBase):
    def __init__(self):
        super().__init__()
        self.network = models.resnet50(weights=None)
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, len(CLASSES))

    def forward(self, xb):
        return torch.sigmoid(self.network(xb))

# ── Load model ─────────────────────────────────────────────────────────────────
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = ResNet()
model.load_state_dict(torch.load('plastic_classifier.pth', map_location=device))
model.to(device)
model.eval()

# ── Image transform (same as training) ────────────────────────────────────────
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])

# ── Flask app ──────────────────────────────────────────────────────────────────
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    try:
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
    except Exception:
        return jsonify({'error': 'Invalid image file'}), 400

    tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(tensor)
        probs = outputs[0]
        top_prob, top_idx = torch.max(probs, dim=0)

    label = CLASSES[top_idx.item()]
    confidence = round(top_prob.item() * 100, 1)

    # All class probabilities for display
    all_probs = {cls: round(p.item() * 100, 1) for cls, p in zip(CLASSES, probs)}

    return jsonify({'label': label, 'confidence': confidence, 'all_probs': all_probs})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
