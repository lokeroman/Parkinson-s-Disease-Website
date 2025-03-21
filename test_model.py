import pickle
import os

file_path = "parkinsons_model.sav"


if os.path.exists(file_path):
    print("File found, trying to load...")
    try:
        with open(file_path, "rb") as file:
            model = pickle.load(file)
        print("Model loaded successfully!")
    except Exception as e:
        print("Error loading model:", e)
else:
    print("File not found!")
