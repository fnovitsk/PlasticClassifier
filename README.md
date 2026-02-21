# Plastic Classifier

A deep learning web app that classifies plastic images into one of seven categories using a fine-tuned ResNet-50 model trained with PyTorch.

## Supported Plastic Types

| Label | Description |
|-------|-------------|
| HDPE  | High-Density Polyethylene (milk jugs, detergent bottles) |
| LDPE  | Low-Density Polyethylene (shopping bags, squeeze bottles) |
| Other | Mixed or unidentified plastics |
| PET   | Polyethylene Terephthalate (water bottles, food trays) |
| PP    | Polypropylene (tupperware, bottle caps) |
| PS    | Polystyrene (foam cups, plastic cutlery) |
| PVC   | Polyvinyl Chloride (pipes, window frames) |

---

## Project Structure

```
PlasticClassifier/
├── app.py                          # Flask web application
├── plastic_classifier.pth          # Trained model weights
├── plastic_classifier_pytorch.ipynb # Training notebook
├── requirements.txt
├── templates/
│   └── index.html                  # Upload UI
├── Data/
│   └── Plastic Classification/     # Training images (per-class folders)
└── ExternalImages/                 # Sample test images
```

---

## Setup

### 1. Clone / open the project

```bash
cd PlasticClassifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If you have a CUDA-capable GPU, install the matching CUDA build of PyTorch from https://pytorch.org/get-started/locally/ for faster inference.

---

## Running the App

```bash
python app.py
```

You should see output similar to:

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

---

## Accessing the Live Demo

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

1. Click the upload area and select a plastic image (JPG, PNG, WEBP, etc.)
2. Click **Classify**
3. The predicted plastic type and a confidence bar chart for all classes are shown instantly

---

## Re-training the Model

Open `plastic_classifier_pytorch.ipynb` in VS Code or Jupyter and run all cells. The final cell saves new weights to `plastic_classifier.pth`.

---

## Deploying Publicly (optional)

To share the app over the internet you can deploy it to a free hosting platform:

### Render
1. Push the repository to GitHub.
2. Create a new **Web Service** on [render.com](https://render.com), pointing at your repo.
3. Set **Start Command** to `python app.py`.
4. Render will install `requirements.txt` automatically.

### Railway
1. Push to GitHub.
2. Create a new project on [railway.app](https://railway.app) and import the repo.
3. Set the start command to `python app.py`.

> For any public deployment, change the last line of `app.py` to:
> ```python
> app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
> ```
> and add `import os` at the top.

---

## Tech Stack

- **Model:** ResNet-50 (pretrained on ImageNet, fine-tuned on plastic dataset)
- **Framework:** PyTorch + torchvision
- **Web:** Flask + plain HTML/CSS/JS
