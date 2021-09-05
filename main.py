import numpy
import scipy
from scipy.spatial \
import distance_matrix
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    categories = []
    danceability = []
    energy = []
    speechiness = []
    acousticness = []
    liveness = []
    valence = []
    duration = []

    print(distance_matrix([[0,0],[0,1]], [[1,0],[1,1]]))
    df = pd.read_csv('/Users/bensauberman/Desktop/CSC373/BeatlesProject/TheBeatlesCleaned.csv')
    for row in df:
        categories.append(row)


    for index, row in df.iterrows():
        danceability.append(row[4])
        energy.append(row[5])
        speechiness.append(row[6])
        acousticness.append(row[7])
        liveness.append(row[8])
        valence.append(row[9])
        duration.append(row[10])

    X = numpy.concatenate((danceability, energy, speechiness, acousticness, liveness, valence, duration), axis=0, out=None, dtype=None, casting="same_kind")
    print(X)
