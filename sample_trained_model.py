import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)


from model import sample_trained_model
import matplotlib.pyplot as plt

num = 5
samples=sample_trained_model('wind25',500,num)


for ii in range(num):
    # plt.figure()
    plt.plot(samples[ii,:,0],'x-')

plt.show()    