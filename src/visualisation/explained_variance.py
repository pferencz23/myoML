import matplotlib.pyplot as plt
import numpy as np

def plot_explained_variance(explained_variance_ratio_):
    # x-values: component indices starting at 1
    x = np.arange(1, len(explained_variance_ratio_) + 1)[:100]

    # y-values: cumulative explained variance
    y = np.cumsum(explained_variance_ratio_)[:100]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o')
    plt.axhline(y=0.85, color='g', linestyle='--')
    plt.axhline(y=0.90, color='b', linestyle='--')

    plt.xlabel('Number of Principal Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Explained Variance by Number of Components')
    plt.grid(True)
    plt.show()