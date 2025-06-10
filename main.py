import os
from img2vec_pytorch import Img2Vec
import torch
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

#prepare the data
Img2Vec = Img2Vec()
data_dir = "C:\\Users\\d3vsh\\Downloads\\datasetfinal"
train_dir = "C:\\Users\\d3vsh\\Downloads\\datasetfinal\\train"
test_dir = "C:\\Users\\d3vsh\\Downloads\\datasetfinal\\test"


data = {}

for j, dir_ in enumerate([train_dir, test_dir]):
    features = []
    labels = []
    
    for category in os.listdir(dir_):
        for image_path  in os.listdir(os.path.join(dir_, category)):
            image_path_ = os.path.join(dir_, category, image_path)
            img = Image.open(image_path_)
            img = img.convert('RGB')  # Ensure the image is in RGB format
            img_features = Img2Vec.get_vec(img)
            
            features.append(img_features)
            labels.append(category)
    
    
    data[['train_data', 'test_data'][j]] = features
    data[['train_lables', 'test_lables'][j]] = labels

print(data.keys())
            
#train the model
model = RandomForestClassifier()
model.fit(data['train_data'], data['train_lables'])

#test performance
y_pred = model.predict(data['test_data'])
score = accuracy_score( y_pred, data['test_lables'])


print(f"Accuracy: {score * 100:.2f}%")


#save the model
with open('model.p', 'wb') as f:
    pickle.dump(model, f)
    f.close()
