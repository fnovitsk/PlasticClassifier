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

## Tech Stack

- **Model:** ResNet-50 (pretrained on ImageNet, fine-tuned on plastic dataset)
- **Framework:** PyTorch + torchvision
- **Web:** Flask + plain HTML/CSS/JS
