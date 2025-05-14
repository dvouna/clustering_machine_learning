# Penguin Species Clustering in the Arctic

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-learn Version](https://img.shields.io/badge/scikit_learn-1.4.0+-orange.svg)](https://scikit-learn.org/stable/)
[![Scipy Version](https://img.shields.io/badge/scipy-1.12.0+-green.svg)](https://scipy.org/)
[![Pandas Version](https://img.shields.io/badge/pandas-2.2.1+-purple.svg)](https://pandas.pydata.org/)
[![Matplotlib Version](https://img.shields.io/badge/matplotlib-3.8.2+-yellow.svg)](https://matplotlib.org/)

## Project Overview

This data science project utilizes machine learning clustering techniques to identify distinct groups within a dataset of penguin species in the Arctic.  The primary goal is to uncover inherent patterns and relationships in the data, revealing potential species sub-groups or behavioral similarities.  Two different clustering algorithms are implemented: K-Means and Hierarchical Clustering.

## Libraries Used

The following Python libraries are used in this project:

* **Scikit-learn (sklearn):** For implementing the K-Means and Hierarchical Clustering algorithms, as well as data scaling and model evaluation.
* **Scipy:** For scientific computing, particularly for the hierarchical clustering dendrogram.
* **Pandas:** For data manipulation and analysis, including loading, cleaning, and transforming the penguin dataset.
* **Matplotlib:** For data visualization, specifically for plotting the clusters and dendrograms.

## Data Source

The data was collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network. The  dataset used in this project contains measurements such as culmen length (mm), culmen depth (mm), flipper length (mm), body mass (g), and penguin sex, for penguins observed in the Antartica. 

## Project Structure

The repository is organized as follows:

* `data/`:  This directory contains the penguin dataset.  
* `models/`:  This directory contains 2 models scripts used in this project: kmeans and hierarchical. 
* `notebooks/`: This directory contains the Jupyter Notebooks:
    * `penguins_hierarchical_clustering.ipynb`:  Demonstrates the implementation of Hierarchical clustering on the penguin dataset.
    * `penguins_kmeans_clustering.ipynb`: Demonstrates the implementation of K-Means clustering on the penguin dataset. 
*  `clustering_arctic_penguins_data_science.jpeg`: 
* `README.md`:  The file you are currently reading.

## Clustering Models

This project explores two popular clustering algorithms:

### 1. K-Means Clustering

* The `K_Means_Clustering.ipynb` notebook walks through the following steps:
    * Data loading and exploration using Pandas.
    * Data preprocessing, including handling missing values and scaling features.
    * Implementation of K-Means clustering using Scikit-learn.
    * Determination of the optimal number of clusters (K) using methods like the Elbow Method or Silhouette analysis.
    * Visualization of the resulting clusters using Matplotlib.
    * Interpretation of the clusters in the context of penguin species characteristics.

### 2. Hierarchical Clustering

* The `Hierarchical_Clustering.ipynb` notebook covers:
    * Data loading and exploration using Pandas.
    * Data preprocessing.
    * Implementation of Hierarchical clustering (agglomerative clustering) using Scikit-learn and Scipy.
    * Visualization of the dendrogram using Scipy to understand the hierarchical relationships between data points.
    * Cutting the dendrogram to obtain clusters.
    * Visualization of the resulting clusters using Matplotlib.
    * Comparison of the clusters obtained from Hierarchical clustering with those from K-Means.

## Results and Interpretation

* K-Means identified three clusters, which largely correspond to the three main penguin species in the dataset (Adelie, Chinstrap, and Gentoo).
* Hierarchical clustering revealed a similar grouping, but also highlighted some sub-clusters within the Gentoo species, suggesting potential variations in size or other features.

## Contributions

Contributions to this project are welcome.  If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.
