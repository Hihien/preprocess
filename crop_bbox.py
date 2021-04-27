import cv2
import os
import json
import tqdm
import numpy as np

def main():
    data_dir = 'data/DATA'
    subsets = ['train']
    images = {}

    os.makedirs(data_dir, exist_ok= True)
    bbox_count = 0

    for subset in subsets:
        subset = os.path.join(data_dir, subset)
        for json_file in os.listdir(subset):
            if not json_file.endswith('.json'):
                continue

            json_file = os.path.join(data_dir, json_file)
            with open(json_file) as json_file:
                json_data = json.load(json_file)
                for img_obj in json_data['images']:
                    file_name = img_obj['file_name']
                    id = img_obj['id']
                    images[id] = file_name

                for annotation_obj in json_data['annotations']:
                    id = annotation_obj['id']
                    image_id = int(annotation_obj['image_id'])
                    file_name = images[image_id]
                    bbox = annotation_obj['bbox']
                    x, y, width, height = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
                    img = cv2.imread(file_name)
                    crop_img = img[y: y+height, x: x+width]
                    name = str('hand_train_') + str(id) + '.jpg'
                    cv2.imwrite(name, crop_img)
                    print(file_name)
                    # window_name = "image"
                    # cv2.imshow(window_name, crop_img)
                    # cv2.waitKey(0)
                    bbox_count += 1
    print(bbox_count)

    #             for file_name in images:
    #                 print(file_name)
    #                 bbox = annotation_obj['bbox']
    #                 x, y, width, height = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    #                 img = images[file_name]
    #                 img = cv2.imread(img)
    #                 crop_img = img[y: y+height, x: x+width]
    #                 window_name = "image"
    #                 cv2.imshow(window_name, crop_img)
    #                 cv2.waitKey(0)
    #             bbox_count += 1
    # print(bbox_count)

if __name__ == '__main__':
    main()
