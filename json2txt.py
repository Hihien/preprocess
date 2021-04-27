import cv2
import os
import json
import tqdm
import numpy as np

def main():
    data_dir = 'data/DATA'
    subsets = ['test', 'train']
    ans = ['test_annotation', 'train_annotation']
    images = {}

    os.makedirs(data_dir, exist_ok= True)
    bbox_count = 0
    save_str = ''

    for an in subsets:
        an = os.path.join(data_dir, an)
        for txt_file in os.listdir(an):
            if txt_file.endswith('.txt'):
                txt_file = os.path.join(an, txt_file)
                os.remove(txt_file)

    for subset in subsets:
        subset = os.path.join(data_dir, subset)

        for json_file in os.listdir(subset):
            if not json_file.endswith('.json'):
                continue

            json_file = os.path.join(data_dir, json_file)
            with open(json_file) as json_file:
                json_data = json.load(json_file)
                for cate in json_data['categories']:
                    cls = cate['id']

                for img_obj in json_data['images']:
                    file_name = img_obj['file_name']
                    id = img_obj['id']
                    images[id] = file_name

                for annotation_obj in json_data['annotations']:
                    id = annotation_obj['id']
                    image_id = int(annotation_obj['image_id'])
                    file_name = images[image_id]
                    save_file = os.path.join(subset, file_name.replace('.jpg', '.txt'))
                    bbox = annotation_obj['bbox']
                    x, y, width, height = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
                    img = cv2.imread(file_name)

                    x = x / img.shape[1]
                    y = y / img.shape[0]
                    width = width / img.shape[1]
                    height = height / img.shape[0]

                    save_str += f'{cls} {x:.06f} {y:0.6f} {width:0.6f} {height:0.6f}'
                    bbox_count += 1
                    save_str += '\n'

                    with open(save_file, 'a') as r:
                        r.write(save_str)
                        save_str = ''
                        r.close()


    print(bbox_count)

if __name__ == '__main__':
    main()


