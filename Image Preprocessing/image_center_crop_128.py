import pandas as pd
import os
from torchvision.transforms import CenterCrop
import numpy as np
from PIL import Image, ImageDraw

completed_processing = set()

source_dir = "C:/Users/jessi/Documents/Master_Courses/MIE1517_IDL/Project/dataset/dataset/"
output_dir = "C:/Users/jessi/Documents/Master_Courses/MIE1517_IDL/Project/dataset/processed_dataset/"

i = 0
nb_excluded = 0

import time

start = time.time()

with os.scandir(source_dir) as it:
    for item in it:
        i += 1
        if item.name.endswith('.jpg'):
            if item.name in completed_processing:
                continue

            completed_processing.add(item.name)

            with Image.open(source_dir + item.name) as image:

                width, height = image.size
                if width < 128 or height < 128:
                    nb_excluded += 1
                    continue

                crop_img = CenterCrop(128)(image)
                crop_img.save(output_dir + item.name)

        if i % 50 == 0:
            print(i)

end = time.time()
print(end - start)
print(nb_excluded)
print(i)











