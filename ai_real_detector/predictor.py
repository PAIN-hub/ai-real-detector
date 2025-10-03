import numpy as np
from tensorflow.keras.preprocessing import image
from .metadata import extract_metadata
from .model_loader import load_model

model = load_model()

def preprocess(img_path):
    img = image.load_img(img_path, target_size=(32, 32))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return x / 255.0

def predict(img_path):
    x = preprocess(img_path)
    prob = model.predict(x)[0][0]

    if prob < 0.4:
        label = "Real"
    elif prob > 0.6:
        label = "AI-Generated"
    else:
        label = "Uncertain"
        metadata = extract_metadata(img_path)
        return {
            "prediction": label,
            "confidence": float(prob),
            "metadata_check": metadata,
            "final_suggestion": (
                "Likely Real (metadata supports)" 
                if "Camera" in metadata and "Unknown" not in metadata 
                else "Likely AI (metadata missing/strange)"
            )
        }

    return {
        "prediction": label,
        "confidence": float(prob),
        "metadata_check": "Skipped (high confidence)",
        "final_suggestion": label
    }