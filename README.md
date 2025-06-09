# Image Classifier: Empty vs Not Empty

This project trains an image classifier to detect whether an image region is **empty** or **not empty**, using a Support Vector Machine (SVM) trained on small 15x15 image patches.

---

## Features

- Loads and preprocesses image data from folders `empty/` and `not_empty/`
- Resizes images to 15x15 and flattens them into feature vectors
- Uses GridSearchCV to tune hyperparameters of an SVM
- Saves the best model using `pickle`
- Prints classification accuracy on the test set

---

## Included Dataset

The dataset is included in this repository under the `clf-data/` folder.


## Requirements

Install all Python dependencies using:

```bash
pip install -r requirements.txt
