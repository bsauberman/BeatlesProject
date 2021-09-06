import numpy as np
np.set_printoptions(threshold = 1000000000)
import scipy
from scipy.spatial \
import distance_matrix
import pandas as pd
from sklearn.preprocessing import minmax_scale

def normalizer(array):
    normalizedArray = minmax_scale(array)
    return normalizedArray

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #create arrays of the different features
    categories = []
    danceability = []
    energy = []
    speechiness = []
    acousticness = []
    liveness = []
    valence = []
    duration = []

    #print(distance_matrix([[0,0],[0,1]], [[1,0],[1,1]]))

    df = pd.read_csv('TheBeatlesCleaned.csv')
    #for col in df:
        #categories.append(col)

    #add the data to each array
    for index, row in df.iterrows():
        danceability.append(row[4])
        energy.append(row[5])
        speechiness.append(row[6])
        acousticness.append(row[7])
        liveness.append(row[8])
        valence.append(row[9])
        duration.append(row[10])

    #normalize the features that are not already betwen 0 and 1
    duration = normalizer(duration)
    X = np.array([danceability, energy, speechiness, acousticness, liveness, valence, duration])

    from sklearn.metrics.pairwise import pairwise_distances
    similarity = pairwise_distances(X, metric= 'cosine')
    print(similarity)
    # formatted matrix: https://docs.google.com/document/d/13sXKPBVra6f6q-XC42iVizlgwjTcE_jT3BOrWjZ-2mM/edit?usp=sharing

    #read in the song popularity data
    #data is in # of millions of listens on Spotify as of 9/5/21, rounded to the nearest millionth
    Y = []
    with open('songPopularity') as f:
        Y.append(f.read().splitlines())
    Y = Y[0]

    #normalize the populalrity to be between 0 and 1
    Y = normalizer(Y)

    #print(X.shape) # 7 x 193
    #print(len(Y)) # 1 x 193

    #distance_matrix(X,Y)
