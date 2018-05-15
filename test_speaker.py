import os
import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time

def speakerName():
    #path to training data
    source   = "development_set\\"   

    modelpath = "speaker_models\\"

    test_file = "development_set_test.txt"        

    file_paths = open(test_file,'r')


    gmm_files = [os.path.join(modelpath,fname) for fname in 
                  os.listdir(modelpath) if fname.endswith('.gmm')]

    #Load the Gaussian gender Models
    models    = [cPickle.load(open(fname,'rb')) for fname in gmm_files]
    speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
                  in gmm_files]

    # Read the test directory and get the list of test audio files 

    sr,audio = read("file.wav")
    vector   = extract_features(audio,sr)
    
    log_likelihood = np.zeros(len(models)) 
    
    for i in range(len(models)):
        gmm    = models[i]         #checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
    
    winner = np.argmax(log_likelihood)
    #print (log_likelihood[winner],'\n')
    #print(winner)
    print ("\tDetected as - ", speakers[winner])

    return speakers[winner]

