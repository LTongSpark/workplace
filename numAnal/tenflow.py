#-*-encoding:utf-8-*-
import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# a = tf.constant(2.3)
# b = tf.constant(2.3)
#
# print(tf.add(a,b))
# with tf.Session(config=tf.ConfigProto(log_device_placement = True)) as session:
#     print(session.run(tf.add(a,b)))

a = tf.constant([1,2,3,4,5,6])
b = tf.Variable(tf.random_normal([2,3] ,mean = 0.0 ,stddev = 1.0))
# 必须做一步显示的初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess :
    # 必须运行初始化
    sess.run(init_op)
    print(sess.run([a,b]))