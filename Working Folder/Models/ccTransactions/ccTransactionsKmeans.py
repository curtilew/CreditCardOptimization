from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

csv_data = '/Users/lewiswcurtisiii/Desktop/CreditCardOptimization/CreditCardOptimization/Working Folder/Models/ccTransactions/ccTransactions_prepocessed_v3.csv'

df = pd.read_csv(csv_data)
print(df)
df = df.dropna()

print(df)



df = df.drop(columns=["Merchant City", "Merchant State", "User", "Card", "Zip", "Time"])

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

###Perform K-Means clustering
num_clusters = 4 #Adjusting number of clusters until a distinct set of clusters is shown

kmeans = KMeans(n_clusters=num_clusters, random_state=42) 

df['Cluster'] = kmeans.fit_predict(df_scaled) #Creating another column to assign cluster number to each row 
                                                        #based on calculated distance


K_range = range(1, 11)


# Calculate inertia for each K
inertia = []
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(K_range, inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia ')
plt.title('Elbow Method for Optimal K')
plt.show()

# Print cluster
print(df[['Cluster']].value_counts())  

# Print cluster centers
print("Cluster Centers (Centroids):")
print(kmeans.cluster_centers_)




centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.figure(figsize=(10, 8))
sns.pairplot(df, hue='Cluster', palette='viridis')
plt.suptitle('Pairwise Scatter Plots with Cluster Assignments', y=1.02)
plt.savefig('pairwise_seaborn.png')



# Print cluster
print(df[['Cluster']].value_counts())  

# Print cluster centers
print("Cluster Centers (Centroids):")
print(kmeans.cluster_centers_)




new_data = pd.DataFrame({
 
    'Amount': [85.75],
    'MCC': [5812],
    'Month': [2],   
    'Day': [3]     
  
})

# Scale the new data using the same scaler
new_data_scaled = scaler.transform(new_data)

# Predict which cluster it belongs to
cluster_prediction = kmeans.predict(new_data_scaled)

print(f"The new transaction belongs to cluster: {cluster_prediction[0]}")



plt.figure(figsize=(10, 8))


feature1 = 'Amount'
feature2 = 'MCC'
feature_idx1 = df.columns.get_loc(feature1)
feature_idx2 = df.columns.get_loc(feature2)

# Plot existing data points
for cluster in range(num_clusters):
    cluster_points = df[df['Cluster'] == cluster]
    plt.scatter(cluster_points[feature1], cluster_points[feature2], label=f'Cluster {cluster}')

# Plot the new point with a different marker
plt.scatter(new_data[feature1], new_data[feature2], color='red', marker='*', s=200, label='New Point')

# Plot centroids
plt.scatter(centroids[:, feature_idx1], centroids[:, feature_idx2], color='black', marker='X', s=100, label='Centroids')

plt.xlabel(feature1)
plt.ylabel(feature2)
plt.title('Cluster Assignment for New Data Point')
plt.legend()
plt.show()
