#Program1

name=input("Hi, what is your Name? ")
print("Hello " + name + "!Let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")


bottom = 1
top = 100
guess = "no"
while guess == "no":
	mid = (top+bottom)//2
	guess = input("Is it " + str(mid) +"?(yes/no)")
	if guess == "yes":
		print("Yeey! I got it in", 7, "tries!")
	more=input("Do you want to play more?(yes/no)")
	if more == "yes":
	return true
	else:
	print("Bye-bye")
	return false

	if guess == "no":
		larger=input("is the number larger than " + str(mid) +"?")
	if larger == "yes":
		bottom = mid+1
	else:
		top = mid


	






#Program2
l=list("Hello")
l
"".join(l)
" ".join(l)
"_".join(l)

  

      
  



