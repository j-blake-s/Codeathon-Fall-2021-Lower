def for_only_solve(file_name):
	"""
	The trick is that the middle (or left-middle, if even num elements)
	of the array is added "length" times, while those "m" elements next to 
	it are added "n-m" times.
	"""
	data_list = open(file_name,"r").read().split("\n")

	length = int(data_list[0])
	num_list = [int(i) for i in data_list[1].split()]
	
	# length = 10000000
	# num_list = [i for i in range(length)]
	ret_sum = 0

	half = int(length/2)

	if length %2 == 0:
		# even, changes the multiplier
		for i in range(length):
			# if(i == half):
			# 	print("*"*10)
			if(i < half):
				multiplier = 2*(i+1)
				# print(multiplier," x ",num_list[i])
				ret_sum += multiplier*num_list[i]
			else:
				multiplier = ((length-1) - 2*(i-half))
				# print(multiplier," x ",num_list[i])
				ret_sum += multiplier * num_list[i]
	else:
		# odd, changes the multiplier
		for i in range(length):
			# if(i == half):
			# 	print("*"*10)
			if(i < half):
				multiplier = 2*(i+1)
				# print(multiplier," x ",num_list[i])
				ret_sum += multiplier*num_list[i]
			else:
				multiplier = ((length) - 2*(i-half))
				# print(multiplier," x ",num_list[i])
				ret_sum += multiplier * num_list[i]

	print("for: sum: {}".format(ret_sum))


def naive_solve(file_name):
	"""
	The trick is that the middle (or left-middle, if even num elements)
	of the array is added "length" times, while those "m" elements next to 
	it are added "n-m" times.
	"""
	data_list = open(file_name,"r").read().split("\n")

	length = int(data_list[0])
	num_list = [int(i) for i in data_list[1].split()]
	
	ret_sum = 0

	going_right = True

	stride_size = length

	counter = 0

	while counter <= length/2:
		if going_right:
			for i in range(counter,stride_size):
				#print(num_list[i],end= " ")
				ret_sum += num_list[i]
			going_right = False
			stride_size -=1
			#print()
		else:
			for i in range(stride_size-1,counter-1,-1):
				#print(num_list[i],end= " ")
				ret_sum += num_list[i]
			going_right = True
			counter +=1
			#if(counter != length/2):
				#print()

	print("naive: sum: {}".format(ret_sum))

DIR = "INPUTS"
import os

# for f in os.listdir(DIR):
# 	file = os.path.join(DIR,f)
# 	naive_solve(file)
# 	for_only_solve(file)

for_only_solve("test")
naive_solve("test")
