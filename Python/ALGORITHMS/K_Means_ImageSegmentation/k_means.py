import random
import numpy as np

import basics as bs

MAX_ITER = int(100)

def init_centroids(K:int, range_:int = bs.RANGE_DEF) -> list:
    return sorted(random.sample(range(0, range_), K))

def assign_clusters(image:np.ndarray, centroids:list) -> np.ndarray:
    clusters_ = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            intensity = int(image[i, j])
            closest = min(range(len(centroids)), key=lambda c: abs(intensity - int(centroids[c])))
            clusters_[i, j] = closest

    return clusters_
    
def update_centroids(img_np:np.ndarray, clusters:np.ndarray, K:int) -> list:
    new_centroids_ = []

    for i in range(K):
        # get all the pixels from the current cluster
        cluster_pixels = img_np[clusters == i]

        # if it contains pixels
        if len(cluster_pixels) > 0:
            # calculate the mean of the pixels
            new_centroids_.append(int(np.mean(cluster_pixels)))
        else:
            # else add 0 instead
            new_centroids_.append(0)

    return new_centroids_

def start(img_np:np.ndarray, K:int, max_iter:int = MAX_ITER) -> tuple:
    centroids_ = init_centroids(K)
    print("Centroids start: ", centroids_)

    for iter in range(max_iter):
        clusters_ = assign_clusters(img_np, centroids_)
        new_centroids = update_centroids(img_np, clusters_, K)

        print(f'{iter + 1}. centroid: {new_centroids}')

        if new_centroids == centroids_:
            print("Converged. Done!")
            break

        centroids_ = new_centroids

    return clusters_, centroids_

def color_clusters(image_, clusters_, centorids_):
    height, width = image_.shape
    colored_image = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            cluster_index = clusters_[i, j]
            color = centorids_[cluster_index]
            colored_image[i, j] = [color, color, color]

    return colored_image