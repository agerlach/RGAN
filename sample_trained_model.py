import tensorflow as tf
import numpy as np
#from data_utils import get_batch
import data_utils
import pdb
import json
from mod_core_rnn_cell_impl import LSTMCell          #modified to allow initializing bias in lstm
#from tensorflow.contrib.rnn import LSTMCell
tf.logging.set_verbosity(tf.logging.ERROR)
import mmd

from differential_privacy.dp_sgd.dp_optimizer import dp_optimizer
from differential_privacy.dp_sgd.dp_optimizer import sanitizer
from differential_privacy.privacy_accountant.tf import accountant

from model import sample_trained_model
import matplotlib.pyplot as plt

num = 5
samples=sample_trained_model('wippr_v1',485,num)


for ii in range(num):
    plt.figure()
    plt.plot(samples[ii,:,0],'x-')

plt.show()    