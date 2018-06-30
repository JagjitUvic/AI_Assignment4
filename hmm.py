# adding all required modules

import numpy as np
import matplotlib.pyplot as plt
import hmmlearn.hmm as hm

# Hidden Markov Model with multinomial (discrete) emissions

model_object = hm.MultinomialHMM(n_components=2)

# starting probability healthy because given in question, he starts out healthy

model_object.startprob_ = np.array([1.0, 0.0])

# transmission probabilities
model_object.transmat_ = np.array([[0.7, 0.3],
                                   [0.5, 0.5]])

# Emission probabilities
model_object.emissionprob_=np.array([[0.2,0.1,0.7],
                                     [0.3,0.6,0.1]])

# generate 300 samples
Emission,Transmission=model_object.sample(300)

# remodelling the system and fitting it

# resize the emission
Emission = np.reshape(Emission, (-1, 1))
Transmission = np.reshape(Transmission, (-1, 1))
# fit the Emission from samples
model_object.fit(Emission)

# printing the emission and transmission probabilities
print "Emission Probabilities after fitting the Model with samples : "
print (model_object.emissionprob_)
print "Transmission Probabilities after fitting the Model with samples : "
print (model_object.transmat_)

# predicting
Predict = model_object.predict(Emission)

# reshape the predict
Predict = np.reshape(Predict, (-1, 1))

# counting the errors
count = 0
for x in range(0,300):
    if Predict[x] != Transmission[x]:
        count = count + 1
# print the number of errors
print "Number of Errors made by HMM model when using the original states :",count
print "Percentage Accuracy of the HMM model when comparing with Ground Truth (original States)",((300 - count)/float(300))*100
