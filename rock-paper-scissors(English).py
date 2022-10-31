import random
print('Author of this procedure Lawrence Shi')
print('The stone, scissors or cloth produced in this program are completely random, refer to the code')
print('This procedure is for reference only')
print('Please input something (stone, scissors or paper)')
a=input()
b=random.randint(1,3)
if b==1:
	print('rock')
elif b==2:
	print('scissors')
else:
	print('paper')
if a=='rock' and b==1 or a=='scissors' and b==2 or a=='paper' and b==3:
	print('It ends in a draw')
elif a=='rock' and b==3 or a=='scissors' and b==1 or a=='paper' and b==2:
	print('I won. 🙂')
elif a=='rock' and b==2 or a=='scissors' and b==3 or a=='paper' and b==1:
	print('I am lost. 😢')
else:
	print('You lost the game wrong')
