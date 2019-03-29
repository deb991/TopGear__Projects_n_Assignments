import tensorflow as tf
import numpy as np

data1 = np.array([[1., 4, 2], [5, 6, 24], [15, 1, 5], [7,3,8], [9,4,7]]) #MxN matrics
data2 = np.array([[100., 400, 200], [500, 600, 240], [150, 100, 500], [700,300,800], [900,400,700]]) #NxP matrics

def tf_conv(x):
    x = x - tf.expand_dims(tf.reduce_mean(x, axis=1), 1)
    fact = tf.cast(tf.shape(x)[1] - 1, tf.float32)
    return tf.matmul(x, tf.conj(tf.transpose(x))) / fact
  
def tf_conv2(x):
    x = x - tf.expand_dims(tf.reduce_mean(x, axis=1), 1)
    fact = tf.cast(tf.shape(x)[1] - 1, tf.float32)
    return tf.matmul(x, tf.conj(tf.transpose(x))) / fact

with tf.Session() as sess:
    print('First Matrics :: \n', sess.run(tf_conv(tf.constant(data1, dtype=tf.float32))))

    
with tf.Session() as sess:
    print('Second Matrics :: \n', sess.run(tf_conv(tf.constant(data2, dtype=tf.float32))))
