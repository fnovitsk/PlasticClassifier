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

## Docker

### Build and run locally

```bash
docker build -t plastic-classifier .
docker run -p 5000:5000 plastic-classifier
```

Then open http://localhost:5000.

> The Docker image installs the **CPU-only** build of PyTorch, which is much smaller and works on any host (including Render's free tier which has no GPU).

### Deploy to Render via Docker

1. Push the repository to GitHub (make sure `plastic_classifier.pth` is committed).
2. Go to [render.com](https://render.com) → **New → Web Service**.
3. Connect your GitHub repo.
4. Set **Environment** to **Docker** — Render will detect the `Dockerfile` automatically.
5. Leave the start command blank (the `CMD` in the Dockerfile handles it).
6. Click **Deploy**. Render will build the image and expose the app on a public URL.

---

## Tech Stack

- **Model:** ResNet-50 (pretrained on ImageNet, fine-tuned on plastic dataset)
- **Framework:** PyTorch + torchvision
- **Web:** Flask + plain HTML/CSS/JS
