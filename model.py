from PIL import Image
import pickle
from img2vec_pytorch import Img2Vec


with open('model.p', 'rb') as f:
    model = pickle.load(f)
    
img2vec = Img2Vec()

img_path = 'path of image to be classified'
img = Image.open(img_path)
img = img.convert('RGB')  # Ensure the image is in RGB format
img = img.resize((250, 225))  # Resize the image to match the model's input size
features = img2vec.get_vec(img)

pred = model.predict([features])

print (f"Predicted class: {pred[0]}")