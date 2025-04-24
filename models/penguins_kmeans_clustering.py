# Import Required Packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Loading and examining the dataset
penguins_df = pd.read_csv("penguins.csv")
penguins_df.head() 

# Examine the data types 
penguins_df.info() 

# Create dummy variables for categorical features
penguins_df = pd.get_dummies(penguins_df, dtype='int')
print(penguins_df) 
print(penguins_df.info()) 

# Checking for variance 
print(penguins_df.var())

# Standardizing the data 
scaler = StandardScaler()
penguins_scaled = pd.DataFrame(scaler.fit_transform(penguins_df), columns=penguins_df.columns)
print(penguins_scaled.var()) 

# Run KMeans for Elbow Analysis
# Inertia is the sum of squared distances from each point to its assigned center
inertia = [] 
for k in range(1, 10): 
    kmeans = KMeans(n_clusters=k, random_state=42).fit(penguins_scaled)
    inertia.append(kmeans.inertia_) 

# Plotting Inertias to find the optimal number of clusters
plt.figure(figsize=(8, 5))                  
plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia') 
plt.title('Elbow Method')
plt.show()

# Based on the elbow method, we can choose the number of clusters.
n_clusters = 4

# Run KMeans Algorithm 
kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(penguins_scaled) 
penguins_df['label'] = kmeans.labels_ 

# Plotting the clusters
plt.figure(figsize=(8, 5))
plt.scatter(penguins_df['label'], penguins_df['culmen_length_mm'], c=kmeans.labels_, cmap='viridis') 
plt.xlabel('Cluster') 
plt.ylabel('culmen_length_mm')
plt.xticks(range(int(penguins_df['label'].min()), int(penguins_df['label'].max()) + 1)) 
plt.title(f'K-Means Clustering (K={n_clusters})') 
plt.show() 

# Stat_penguins DataFrame 
numeric_columns = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'label'] 
stat_penguins = penguins_df[numeric_columns].groupby('label').mean()
print(stat_penguins) 