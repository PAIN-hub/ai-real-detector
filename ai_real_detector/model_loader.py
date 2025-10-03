import tensorflow as tf
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model/EfficientNet_model.h5")

def load_model():
    return tf.keras.models.load_model(MODEL_PATH)