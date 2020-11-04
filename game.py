def running():
	print ("you are running in the dark hallway")

def death():
	print ("the monster killed you")

room1 = {
	
	'run' : running,
	'wait' : death
}
print ('                                Welcome to this world')
print ('you are in a dark hallway and there is a errie hooting comming from behind you')

answer = input(" what do you do?   ")
x= room1[answer]
x()
y= input()