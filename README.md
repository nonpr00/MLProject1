# Regression Demo with Manim

This project is a visual demonstration of **linear and nonlinear regression**
using the **Manim** animation library, inspired by 3Blue1Brown-style explanations.

## Authors
- Piero Pilco Reynoso
- Juan Diego Luque Segura

## Requirements
- Python 3.12+
- Poetry

## Setup
```bash
poetry install

-- For normal resolution
poetry run manim -pqh src/regression_demo/scenes.py RegressionDemo

-- For high resolution
poetry run manim -pqh --resolution 1920,1080 src/regression_demo/scenes.py RegressionDemo 

