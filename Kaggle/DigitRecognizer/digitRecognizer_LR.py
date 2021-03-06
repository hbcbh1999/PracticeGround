# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn import svm

# Importing the dataset
labeled_images = pd.read_csv('Data/train.csv')
images = labeled_images.iloc[0:5000,1:]
labels = labeled_images.iloc[0:5000,:1]
train_images, test_images,train_labels, test_labels = train_test_split(images, labels, train_size=0.8, random_state=0)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(train_images, train_labels.values.ravel())
classifier.score(test_images,test_labels)

test_images[test_images>0]=1
train_images[train_images>0]=1
            
# Retraining the model          
classifier = LogisticRegression(random_state = 0)
classifier.fit(train_images, train_labels.values.ravel())
classifier.score(test_images,test_labels)

# Making predicitons on test data      
test_data=pd.read_csv('Data/test.csv')
Xtest_images = labeled_images.iloc[0:5000,1:]
Xtest_labels = labeled_images.iloc[0:5000,:1]
test_data[test_data>0]=1 
classifier.score(Xtest_images,Xtest_labels) 