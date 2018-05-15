import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
from sklearn.mixture import GMM 
import _pickle as cPickle
import warnings
warnings.filterwarnings("ignore")


#path to training data
source   = "development_set\\"   

#path where training speakers will be saved
dest = "speaker_models\\"

train_file = "development_set_enroll.txt"        

file_paths = open(train_file,'r')

count = 0

# Extracting features for each speaker (5 files per speakers)
features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print (path)
    
    # read the audio
    sr,audio = read(source + path)
    
    # extract 40 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))

    count = count + 1
    # when features of 5 files of speaker are concatenated, then do model training
    if count == 5:    
        gmm = GMM(n_components = 16, n_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        picklefile = path.split("-")[0]+".gmm"
        cPickle.dump(gmm,open(dest + picklefile,"wb"))
        print ('Modeling completed for speaker:',picklefile)
        features = np.asarray(())
        count = 0
    