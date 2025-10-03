# AI-vs-Real Detector

> No fluff. This repo packages a small image detector that returns Real / AI-Generated / Uncertain and runs the model from model/EfficientNet_model.h5. If the model is missing it auto-downloads from Google Drive. Metadata (EXIF) is used as a fallback when the model is uncertain.

### Features

1. Binary classifier (Real vs AI) with confidence score (sigmoid output).

2. Uncertain zone and confidence buffer (default: ≤0.4 Real, ≥0.6 AI, else Uncertain).

3. Metadata (EXIF) check used to bias a final suggestion for Uncertain cases.

4. Auto-download model from Google Drive on first run (no manual drag/drop).

## Quick start (5 minutes)

### 1. Prereqs

> Recommended: Python 3.10 (TensorFlow 2.15 compatibility).

> Git, pip.


### 2. Clone & enter dir

```
git clone https://github.com/YOURUSER/ai-real-detector.git
cd ai-real-detector
```

### 3. Create and activate venv (example)

```
python3.10 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies
```
requirements.txt should include:

tensorflow>=2.15.0,<2.21.0
numpy
Pillow
gdown
```

#### Install:
```
pip install -r requirements.txt
```

### 5. Configure model download (one time)

> By default the project uses the Drive file ID provided in ai_real_detector/model_loader.py. If you prefer, set an environment variable instead:

```
export AI_MODEL_FILE_ID=1b_X8kmWhXbOvNS0OaXOe_RwAaAgz42ZM
```
(That 1b_... is the file id for the Drive link that been used.)

### 6. Run a quick prediction (CLI)

> If package installed with entrypoint "ai-detect" (see packaging below)
ai-detect path/to/image.jpg  Or run the CLI module directly
python -m ai_real_detector.cli path/to/image.jpg


*Expected output example:*

===== AI vs Real Detector =====
Prediction: Uncertain
Confidence: 0.5234
Metadata: No EXIF metadata found
Final Suggestion: Likely AI (metadata missing/strange)


# How it works (short) #

1. model_loader.get_model() ensures model/EfficientNet_model.h5 exists, otherwise downloads with gdown using the Drive file id.


2. predictor.predict() preprocesses the image (the input size is set per model; default for this checkpoint is 32×32 — change if you use a different model).


3. If probability p:

`` p <= 0.4 → Real``

`` p >= 0.6 → AI-Generated``

``else → Uncertain and run EXIF metadata check for a “final suggestion.”``



4. EXIF detection inspects Model and Software fields to bias the suggestion.

**Developer notes**

Model download behaviour

ai_real_detector/model_loader.py uses:

FILE_ID = os.environ.get("AI_MODEL_FILE_ID", "1b_X8kmWhXbOvNS0OaXOe_RwAaAgz42ZM")
URL = f"https://drive.google.com/uc?id={FILE_ID}"

If you want to use a different model, either:

Replace FILE_ID in the file, or

Set AI_MODEL_FILE_ID in your environment before running.


**Input size**

The shipped model expects 32×32 images (CIFAKE-style). If you substitute another model, update the preprocess target_size inside ai_real_detector/predictor.py.

## Contact / credits

Built by Pain. <a href='https://x.com/0x_beely'> Twitter </a>
