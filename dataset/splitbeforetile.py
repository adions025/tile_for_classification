""""
split before the tiling process

Written by Adonis Gonzalez
------------------------------------------------------------
"""

import sys, os
import numpy as np
from shutil import copyfile



ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(ROOT_DIR)


folder_to_split = os.path.join(ROOT_DIR, "../dataset3/data_final")

base_folder = os.path.join(ROOT_DIR, "../dataset3/base_folder") #folderbase
dest_train = os.path.join(ROOT_DIR, "../dataset3/base_folder/train")#folderbase/train
dest_test = os.path.join(ROOT_DIR, "../dataset3/base_folder/val")#folderbase/test


def grabNamesImages(path):
  files = os.listdir(path)
  print(files)
  with open(path + "/" + 'image.txt', 'w') as f:
    for item in files:
      if (item.endswith('.jpg')):#just because there are other files
        f.write("%s\n" % item)
  f.close()
  print("List of images, images.tx, was save in", path)


if __name__ == "__main__":

    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    if not os.path.exists(dest_train):
        os.makedirs(dest_train)

    if not os.path.exists(dest_test):
        os.makedirs(dest_test)

    grabNamesImages(folder_to_split)
    imgs_list = open(folder_to_split + '/image.txt', 'r').readlines()

    total_images = len(imgs_list)
    test_percentage = (total_images * 20)/100 # 20 percent for testing

    indexs_test = np.random.choice(len(imgs_list), test_percentage, replace=False)
    print("random test files", indexs_test)

    images = []
    for image_name in imgs_list:
        img_name = image_name.strip().split('/')[-1]
        images.append(img_name)

    for i in indexs_test:
        file_to_copy = os.path.join(folder_to_split, images[i])
        copyfile(file_to_copy, dest_test + "/" + images[i])

    indexs_train = []
    for i in images:
        indexs_train.append(images.index(i))

    training = list(set(indexs_train) ^ set(indexs_test)) #rest for training

    for i in training:
        file_to_copy = os.path.join(folder_to_split, images[i])
        copyfile(file_to_copy, dest_train + "/" + images[i])



    print("---------")
    print("random training files ", training)# 80% for traning




