from setuptools import setup, find_packages

setup(
    name="ai-real-detector",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow>=2.15.0,<2.21.0",
        "numpy",
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "ai-detect=ai_real_detector.cli:main"
        ]
    },
    author="Your Name",
    description="Detect AI vs Real images with deep learning + metadata fallback",
    url="https://github.com/yourusername/ai-real-detector",
    python_requires=">=3.9",
)