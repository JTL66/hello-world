#P1:
#Example1:
def my_range(start,end): 
	x = start
	while x < end:
		yield x 
		x = x + 1
for i in my_range(0,5):
	print(i)

#Example2:
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
for i in my_range(0,5,2):
	print(i)


#P2:
def bunnyEars2(bunnies):
  if bunnies == 0:
    return 0
  elif bunnies % 2 == 0:
    return (3 + bunnyEars2(bunnies - 1))
  else:
    return (2 + bunnyEars2(bunnies - 1))
print("bunnyEars2(0)->", bunnyEars2(0))
print("bunnyEars2(1)->", bunnyEars2(1))
print("bunnyEars2(2)->", bunnyEars2(2))

#pytest in test_bunnyEars2.py
from hw5 import bunnyEars2
def test_bunnyEars2():
  assert bunnyEars2(0) == 0
  assert bunnyEars2(1) == 2
  assert bunnyEars2(2) == 5
  

#P3:
import timeit
def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function()
@timer
def addition():
  total = 0
  for i in range(0,1000000):
    total += i
  return total







