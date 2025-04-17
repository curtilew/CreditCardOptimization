#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 15:29:26 2025

@author: lewiswcurtisiii
"""
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from IPython.display import clear_output
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets




csv_data = 'Working Folder/Models/ccTransactions/ccTransactions_prepocessed_v3.csv'



# df = pd.read_csv(csv_data)


# df = df.drop(columns=["Merchant City", "Merchant State", "User", "Card"])

# scaler = StandardScaler()
# df_scaled = scaler.fit_transform(df)



DF = pd.read_csv(csv_data)
print(DF)


DF = DF.dropna()
DF = DF.drop(columns=["Merchant City", "Merchant State", "User", "Card", "Zip", "Time"])
##--------------------------------
## Remove and save the label
## Next, update the label so that 
## rather than names like "Iris-setosa"
## we use numbers instead. 
## This will be necessary when we "color"
## the data in our plot
##---------------------------------------
DFLabel = DF["MCC"]  ## Save the Label 
print(DFLabel)  ## print the labels
print(type(DFLabel))  ## check the datatype you have

## Remap the label names from strings to numbers


###-------------------------------------------
### Standardize your dataset
###-------------------------------------------
scaler = StandardScaler() ##Instantiate
DF = scaler.fit_transform(DF) ## Scale data
print(DF)

###############################################
###--------------PERFORM PCA------------------
###############################################
## Instantiate PCA and choose how many components
MyPCA = PCA(n_components=4)
Result = MyPCA.fit_transform(DF)
## Print the values of the first component 
print(Result[:, 0]) 
print(Result) ## Print the new (transformed) dataset
print("The relative eigenvalues are:", MyPCA.explained_variance_ratio_)
print("The actual eigenvalues are:", MyPCA.explained_variance_)
EVects = MyPCA.components_
print("The eigenvectors are:\n", EVects)

#################################################
## Visualize the transformed 3D dataset
## we just created using PCA
#################################################
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')

x = Result[:, 0]
y = Result[:, 1] 
z = Result[:, 2]

ax2.scatter(x, y, z, cmap="RdYlGn", edgecolor='k', s=200, c=DFLabel)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('3D PCA')

plt.show()
plt.savefig("MyImage.jpeg")

############################################
## Create Plot to Show Eigenvalues
############################################
plt.bar(
    range(len(MyPCA.explained_variance_ratio_)), 
    MyPCA.explained_variance_ratio_,
    alpha=0.5, align='center', label='Individual Explained Variances'
)
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal component index')
plt.title("Eigenvalues: Percentage of Variance/Information")
plt.tight_layout()
plt.show()



plt.plot(
    range(len(MyPCA.explained_variance_ratio_)),
    np.cumsum(MyPCA.explained_variance_ratio_),
    'r-', linewidth=2, label='Cumulative Explained Variance'
)
plt.axhline(y=0.95, color='g', linestyle='-', label='95% Explained Variance')
plt.legend(loc='best')

































# ###Perform K-Means clustering
# num_clusters = 6 #Adjusting number of clusters until a distinct set of clusters is shown

# kmeans = KMeans(n_clusters=num_clusters, random_state=42) 

# df['Cluster'] = kmeans.fit_predict(df_scaled) #Creating another column to assign cluster number to each row 
#                                                         #based on calculated distance


# K_range = range(1, 11)


# # Calculate inertia for each K
# inertia = []
# for k in K_range:
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(df_scaled)
#     inertia.append(kmeans.inertia_)

# # Plot the elbow curve
# plt.plot(K_range, inertia, marker='o')
# plt.xlabel('Number of Clusters')
# plt.ylabel('Inertia ')
# plt.title('Elbow Method for Optimal K')
# plt.show()

# # Print cluster
# print(df[['Cluster']].value_counts())  

# # Print cluster centers
# print("Cluster Centers (Centroids):")
# print(kmeans.cluster_centers_)




# centroids = scaler.inverse_transform(kmeans.cluster_centers_)

# plt.figure(figsize=(10, 8))
# sns.pairplot(df, hue='Cluster', palette='viridis')
# plt.suptitle('Pairwise Scatter Plots with Cluster Assignments', y=1.02)
# plt.savefig('pairwise_seaborn.png')



# # Print cluster
# print(df[['Cluster']].value_counts())  

# # Print cluster centers
# print("Cluster Centers (Centroids):")
# print(kmeans.cluster_centers_)




# new_data = pd.DataFrame({
#     'Year': [2025],
#     'Month': [4],    
#     'Day': [10],     
#     'Time': [720],   
#     'Amount': [85.75],
#     'Zip': [97330],   
#     'MCC': [5812]     
# })

# # Scale the new data using the same scaler
# new_data_scaled = scaler.transform(new_data)

# # Predict which cluster it belongs to
# cluster_prediction = kmeans.predict(new_data_scaled)

# print(f"The new transaction belongs to cluster: {cluster_prediction[0]}")



# plt.figure(figsize=(10, 8))


# feature1 = 'Amount'
# feature2 = 'Time'
# feature_idx1 = df.columns.get_loc(feature1)
# feature_idx2 = df.columns.get_loc(feature2)

# # Plot existing data points
# for cluster in range(num_clusters):
#     cluster_points = df[df['Cluster'] == cluster]
#     plt.scatter(cluster_points[feature1], cluster_points[feature2], label=f'Cluster {cluster}')

# # Plot the new point with a different marker
# plt.scatter(new_data[feature1], new_data[feature2], color='red', marker='*', s=200, label='New Point')

# # Plot centroids
# plt.scatter(centroids[:, feature_idx1], centroids[:, feature_idx2], color='black', marker='X', s=100, label='Centroids')

# plt.xlabel(feature1)
# plt.ylabel(feature2)
# plt.title('Cluster Assignment for New Data Point')
# plt.legend()
# plt.show()
