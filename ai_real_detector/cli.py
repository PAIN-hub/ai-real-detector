import argparse
from .predictor import predict

def main():
    parser = argparse.ArgumentParser(description="AI vs Real Image Detector")
    parser.add_argument("image", help="Path to image file")
    args = parser.parse_args()

    result = predict(args.image)
    print("\n===== AI vs Real Detector =====")
    print(f"Prediction: {result['prediction']}")
    print(f"Confidence: {result['confidence']*100:.2f}%")
    print(f"Metadata: {result['metadata_check']}")
    print(f"Final Suggestion: {result['final_suggestion']}")