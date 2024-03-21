import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def PiNet_OptiAdvisor(pi_network_data):
    """
    Provides recommendations and insights to optimize Pi Network performance and cost-efficiency on the cloud.
    
    Parameters:
    pi_network_data (DataFrame): A pandas DataFrame containing the data of the Pi Network.
    
    Returns:
    recommendations (list): A list of recommendations to optimize Pi Network performance and cost-efficiency.
    """
    
    # Preprocess the data
    pi_network_data = pi_network_data.dropna()
    pi_network_data = pi_network_data.reset_index(drop=True)
    
    # Scale the data
    scaler = StandardScaler()
    pi_network_data = scaler.fit_transform(pi_network_data)
    
    # Find the optimal number of clusters using the silhouette score
    silhouette_scores = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(pi_network_data)
        score = silhouette_score(pi_network_data, kmeans.labels_)
        silhouette_scores.append(score)
    
    optimal_k = silhouette_scores.index(max(silhouette_scores)) + 2
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=optimal_k)
    kmeans.fit(pi_network_data)
    
    # Generate recommendations based on the cluster assignments
    recommendations = []
    for i in range(optimal_k):
        cluster_data = pi_network_data[kmeans.labels_ == i]
        cluster_mean = np.mean(cluster_data, axis=0)
       cluster_std = np.std(cluster_data, axis=0)
        if cluster_mean[0] < 0:
            recommendations.append('Reduce the number of nodes in Cluster ' + str(i) + ' to improve cost-efficiency.')
        elif cluster_std[0] > 0.2:
            recommendations.append('Consolidate nodes in Cluster ' + str(i) + ' to reduce variability.')
        elif cluster_mean[1] > 0:
            recommendations.append('Increase the memory allocation of nodes in Cluster ' + str(i) + ' to improve performance.')
    
    return recommendations
