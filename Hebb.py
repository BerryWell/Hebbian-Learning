# Hebbian classifier
# ex) list_in = [+1, -1]
#     list_weight = [+0.5, -0.5]
#     out = np.dot(list_in, list_wiehgt)
#     if(out >= 0) then apple
#     elif(out < 0) then banana
#      |       |
# -----------------------
# in_1 | w_11  | w_12
# -----------------------
# in_2 | w_21  | w_22
# -----------------------
#      | out_1 | out_2
# out_1 = in_1*w_11 + in_2*w_21
# out_2 = in_1*w_12 + in_2*w22
# 
# Issue: How to 'train' this algorithm?
# 1. Generate a weight vector randomly.
# 2. Compare the result with actual result.
# 3. If not consistent with the actual result, then modify the weight vector.
# weight_change = learning_rate * f1(input, weight) * f2(output, target_output)

import numpy as np

def Hebb(list_in):
	list_weight = np.array([[+0.5, -0.5],\
							[-0.5, +0.5]])
	list_result = list_in.reshape((2,1)) * list_weight
	list_result = list_result.sum(axis=0)
	return classfication(list_result)

def classfication(list_value):
# list_value = [ out_1, out_2 ]
	if(list_value[0] >= 0 and list_value[1] < 0):
		return 'apple'
	elif(list_value[0] < 0 and list_value[1] >= 0):
		return 'banana'

list_in = np.array([+1, -1])
print('Input: %s' % list_in)
out = Hebb(list_in)
print('Output for list_in = %s: %s' % (list_in, out))

list_in = np.array([-1, +1])
out = Hebb(list_in)
print('Output for list_in = %s: %s' % (list_in, out))
