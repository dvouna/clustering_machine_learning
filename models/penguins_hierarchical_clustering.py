# Import Required Packages
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram 
from scipy.cluster.vq import whiten 

# Loading and examining the dataset
penguins_df = pd.read_csv("penguins.csv")
penguins_df.head() 

# Examine the data types 
penguins_df.info() 

# Normalize the data with whiten method 
whitened_data = whiten(penguins_df.values)
print(whitened_data)

# Convert normalized data to a DataFrame and assign the original column names
penguins_norm = pd.DataFrame(whitened_data, columns=penguins_df.columns)
penguins_norm.describe() 

# Create distance matrix 
distance_matrix = linkage(penguins_norm, method='ward', metric = 'euclidean') 

# Visualizing clusters with dendrogram
dn = dendrogram(distance_matrix)
plt.show()

# Create clusters using fcluster
# The criterion 'maxclust' is used to form flat clusters based on the distance matrix.
penguins_norm['cluster_labels'] = fcluster(distance_matrix, 4, criterion='maxclust')
print(penguins_norm['cluster_labels'].value_counts()) 

# Plotting the clusters 
plt.scatter(penguins_norm['cluster_labels'], penguins_norm['culmen_length_mm'], cmap='viridis') 
plt.xlabel('Cluster') 
plt.ylabel('culmen_length_mm') 
plt.title('Hierarchical Clustering of Penguins') 
plt.show()

