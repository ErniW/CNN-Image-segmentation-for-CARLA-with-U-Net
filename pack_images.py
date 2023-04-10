import os
import argparse
import imageio
import numpy as np
import pickle as pkl
from PIL import Image, ImageOps

RESIZE_WIDTH = 128
RESIZE_HEIGHT = 96

def load_images(dir):

    path = dir
    IMAGE_PATH = os.path.join(path, 'images/')
    MASK_PATH = os.path.join(path, 'masks/')

    images_list = os.listdir(IMAGE_PATH)
    masks_list = os.listdir(MASK_PATH)

    images_list = [IMAGE_PATH + i for i in images_list]
    masks_list = [MASK_PATH + i for i in masks_list]

    images = []
    masks = []
    amount = len(images_list)

    print(f"Starting conversion of {amount} images")

    for i in range(amount):
        img = Image.open(images_list[i])
        mask = Image.open(masks_list[i])

        img = img.resize((RESIZE_WIDTH, RESIZE_HEIGHT), Image.NEAREST)
        mask = mask.resize((RESIZE_WIDTH, RESIZE_HEIGHT), Image.NEAREST)

        img = np.array(img)
        mask = np.array(mask)

        images.append(img)
        masks.append(mask[:,:,0])

    return images, masks
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="Pack images into a single file")
    parser.add_argument('input_dir')
    args = parser.parse_args()

    images, masks = load_images(args.input_dir)
    
    images = np.array(images)
    masks = np.array(masks)
    
    with open('dataset_images.pickle', 'wb') as f:
        pkl.dump(images, f)

    with open('dataset_masks.pickle', 'wb') as f:
        pkl.dump(masks, f)

    print(f"Done saving - Images Shape: {images.shape}, Masks Shape: {masks.shape}")