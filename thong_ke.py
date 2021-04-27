import os
import numpy as np
import cv2

def main():
    a = b = c = d = e = f = g = h = k = 0
    data_dir = 'data/hand'
    subsets = {'hand_test', "hand_train"}
    count = 0

    os.makedirs(data_dir, exist_ok= True)

    for subset in subsets:
        subset = os.path.join(data_dir, subset)
        for file in os.listdir(subset):
            if not file.endswith('.jpg'):
                continue

            img = cv2.imread(os.path.join(subset, file))
            width, height = img.shape[0], img.shape[1]
            # resolution = width * height
            if (width < 80):
                a += 1
            if (80 <= width) and (width < 100):
                b += 1
            if (100 <= width) and (width < 120):
                c += 1
            if (120 <= width) and (width < 140):
                d += 1
            if (140 <= width) and (width < 160):
                e += 1
            if (width >= 160):
                f += 1
            count += 1
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(count)

if __name__ == "__main__":
    main()