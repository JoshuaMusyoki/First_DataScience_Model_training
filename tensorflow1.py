import tensorflow as tf
#creating nodes in computation graph
node1=tf.constant(6, dtype=tf.int32)
node2=tf.constant(8, dtype=tf.int32)
node3=tf.add(node1, node2)

#create tensorflow session object
sess=tf.compat.v1.Session()
#evaluating node3 and printing the result
print("Sum of Node_1 and Node_2 is: " ,sess.run(node3))
#closing the session
sess.close()