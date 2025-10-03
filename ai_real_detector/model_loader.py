import os
import gdown
from keras.models import load_model

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_PATH = os.path.join(MODEL_DIR, "EfficientNet_model.h5")

FILE_ID = "1b_X8kmWhXbOvNS0OaXOe_RwAaAgz42ZM"
URL = f"https://drive.google.com/uc?id={FILE_ID}"

def get_model():
    """Ensure model is available and load it."""
    os.makedirs(MODEL_DIR, exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        print("Downloading EfficientNet model...")
        gdown.download(URL, MODEL_PATH, quiet=False)

    print("Model ready for inference!")
    return load_model(MODEL_PATH)