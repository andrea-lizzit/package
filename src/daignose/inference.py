#!/usr/bin/env python
# coding: utf-8

import torch
import numpy as np
from torchvision import *
from importlib_resources import files, as_file

def predict_new_image(image_tensor):
    input = image_tensor.to(device)
    output = model(input)
    _, index = torch.max(output,1)
    percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100
    return percentage, index


#Set parameters
device = "cpu" # torch.device("cuda" if torch.cuda.is_available() else "cpu")
use_GPU=False #use_GPU=torch.cuda.is_available()
dispBool=True #print the predicted class and corresponding prediction for each sample
nTest=200

transfs = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=154,std=66),
])


if __name__ == "__main__":
    import argparse
    from pathlib import Path
    import daignose.data as modeldata
    from PIL import Image, ImageOps
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("--imPath", help="image path",
                        type=str)
    args = parser.parse_args()

    imPath = Path(args.imPath)
    modelfile = files(modeldata).joinpath('resnet.pt')

    with as_file(modelfile) as modelPath:
        #Load model
        model=torch.load(modelPath)
        model.eval()
        
        # Load data
        img = Image.open(imPath)
        if len(np.shape(img))==3:
            img=ImageOps.grayscale(img) 
        img_tensor = transfs(img).to(device).unsqueeze(0)
        perc, outputClass = predict_new_image(img_tensor)
        perc = perc.detach().numpy().tolist()
        class_data = {"0": "Atelectasis", "1": "Cardiomegaly", "2": "Consolidation", "3": "Edema", "4": "Effusion", "5": "Emphysema", "6": "Fibrosis", "7": "Hernia", "8": "Infiltration", "9": "Mass", "10": "No_Finding", "11": "Nodule", "12": "Pleural_Thickening", "13": "Pneumonia", "14": "Pneumothorax"}
        print(json.dumps({"prob": perc, "classes": class_data}))