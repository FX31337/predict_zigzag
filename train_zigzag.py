#!/usr/bin/env python3

# To support both Python 2 and Python 3.
from __future__ import division, print_function, unicode_literals

# Common imports.
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_mldata

mnist = fetch_mldata('MNIST original')

data = np.genfromtxt('data.csv', delimiter=',') # @todo: numpy vs pandas
sgd_clf = SGDClassifier()
#sgd_clf.fit(X_train, y_train_5)
