#def add(a, b, c):
#  print (a, b, c)
#  return a + b + c
#
#sum = add(1,2,3)
#print (sum)

#def add(a, b, c):
#  print (a, b, c)
#  return a + b + c
#
#args = (1,2,3)
#sum = add(*args)
#print (sum)

#def add(a, b, c):
#  print (a, b, c)
#  return a + b + c
#
##args = (1,2,3)
##args = [1,2,3]
#args = 'abc'
#sum = add(*args)
#print (sum)

#def add(a, b, c):
#  print (a, b, b)
#  return a + b + c
#
#args = (1,2,3,5,6,7)
##sum = add(*args)
#sum = add(*args[-3:])
#print (sum)

#def add(a, b, c):
#  print (a, b, c)
#  return a + b + c
#
#args = {'a': 10, 'b': 20, 'c': 30}
#sum = add(**args)
#print (sum)


#def add(*nums):
#  print (nums)
#  return sum(nums)
#
#x = add(1, 2, 3)
#y = add(1, 2)
#z = add()
#print (x, y, z)

def add(*nums, **args):
  print (nums, args)
  return sum(nums) + sum(args.values())

x = add(1, 2, 3, k = 10)
print (x)




