## Image generation(stylegan2)
This project is an example of training generative models for customized data and generating new images.

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Training](#training)
4. [Generate an image](#Generate-an-image)

## Overview
This project involves the following key steps:
1. Prepareing custom dataset: [kaggle's cat dataset was used.](https://www.kaggle.com/datasets/crawford/cat-dataset)
```bash
#Download cat dataset
pip install kaggle
kaggle datasets download -d crawford/cat-dataset
unzip cat-dataset.zip -d /workspace/cat_dataset
```

2. Image preprocessing
```bash
python preprocessing.py
```
3. Convert to TFRecord format.
```bash
python dataset_tool.py create_from_images <tfrecords_output_path> <input_images_path>
```
4. Model training can be conducted, and new cat images can be generated through the trained models.

## Installation
This section describes the steps to set up the necessary packages and environment.
```bash
#Create a Docker container
docker build -t stylegan2 .
docker run --shm-size=8g --gpus all -v path/to/desired/directory:/workspace -it --rm stylegan2
```

## Training  [The trained model can be downloaded from Google Drive.](https://drive.google.com/drive/folders/1ZfcyJhiYpgQc-v0ysRsyFCeW7r9O9fIB?usp=sharing)
```bash
python run_training.py --num-gpus=2 --data-dir=/workspace/stylegan2/cat_dataset --config=config-f --dataset=tfrecord --total-kimg=2334
```

## Generate an image
Images are saved in the 'results/' folder.
```bash
python run_generator.py generate-images --network=stylegan2-ffhq-config-f.pkl --seeds=0-9 --truncation-psi=0.5
```

| cat1 | cat2 | cat3 | cat4 |
|-----------|-----------|-----------|-----------|
| ![Result](https://github.com/hanacho1/Image_generation/blob/main/results/00015-generate-images/seed0000.png) | ![Result](https://github.com/hanacho1/Image_generation/blob/main/results/00015-generate-images/seed0001.png) | ![Result](https://github.com/hanacho1/Image_generation/blob/main/results/00015-generate-images/seed0002.png) | ![Result](https://github.com/hanacho1/Image_generation/blob/main/results/00015-generate-images/seed0003.png) |


