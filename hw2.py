#Program1

name=input("Hi, what is your Name? ")
print("Hello " + name + "!Let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")


count = 0
bottom = 1
top = 100
guess = "no"
while guess == "no":
	mid = (top+bottom)//2
	guess = input("Is it " + str(mid) +"?(yes/no)")
	count = count + 1
	if guess == "yes":
		print("Yeey! I got it in", count, "tries!")
	if guess == "no":
		larger=input("is the number larger than " + str(mid) +"?")
	if larger == "yes":
		bottom = mid+1
	else:
		top = mid
		
guess = "yes"
while guess == "yes":
	again=input('Do you want to play more?')
	if again == "yes":
		mid = (top+bottom)//2
		guess = input("Is it " + str(mid) +"?(yes/no)")
	if again == "no":
		print('Bye-bye')
	else:
		exit()

	




#Program2
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
result = [0]*len(s)
ls = list(s)

print(ls)
for i in range(len(s)):
	result[indices[i]] = ls[i]
print("". join(result))

  

      
  



