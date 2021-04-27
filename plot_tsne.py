import matplotlib.pyplot as plt
import cv2
import os
import random
import numpy as np
from PIL import Image
from sklearn.feature_extraction import image
from skimage import io
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

def main():
    data =[]
    data_dir = 'data/hand/'
    subsets = ['hand_train/', 'hand_test/']
    for subset in subsets:
        subset = os.path.join(data_dir, subset)
        for file_name in os.listdir(subset):
            image = cv2.imread(os.path.join(subset, file_name))
            if image is not None:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                image = cv2.resize(image, (27, 27))
                image = image.flatten()
                data.append([image, subset + file_name])

    features, images = zip(*data)
    features = np.array(features)
    pca = PCA(n_components= 5)
    pca.fit(features)
    pca_features = pca.transform(features)

    num_images_to_plot = 1753
    if len(images) == num_images_to_plot:
        sort_oder = sorted(random.sample(range(len(images)), num_images_to_plot))
        images = [images[i] for i in sort_oder]
        pca_features = [pca_features[i] for i in  sort_oder]

    X = np.array(pca_features)
    tsne = TSNE(n_components= 2, learning_rate= 150, perplexity= 30, angle= 0.2, verbose=2).fit_transform(X)

    tx, ty = tsne[:, 0], tsne[:, 1]

    tx = (tx - np.min(tx)) / (np.max(tx) - np.min(tx))
    ty = (ty - np.min(ty)) / (np.max(ty) - np.min(ty))

    width = 4000
    height = 3000
    max_dim = 100

    save_file = "out.png"
    window_name = 'image'
    full_image = Image.new('RGBA', (width, height))
    for img, x, y in zip(images, tx, ty):
        tile = Image.open(img)
        rs = max(1, tile.width / max_dim, tile.height / max_dim)
        tile = tile.resize((int(tile.width / rs), int(tile.height / rs)), Image.ANTIALIAS)
        full_image.paste(tile, (int((width - max_dim) * x), int((height - max_dim) * y)), mask=tile.convert('RGBA'))

    full_image = np.array(full_image)

    cv2.imwrite(save_file, full_image)

    plt.figure(figsize=(16, 12))
    plt.imshow(full_image)
    plt.show()

if __name__ == '__main__':
    main()
