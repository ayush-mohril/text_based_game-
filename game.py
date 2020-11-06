def running():
	print ("you are running in the dark hallway")
def door_room2():
	pass
def stair_room2():
	pass
def death():
	print ("the monster killed you")

def err():
	print("sorry wrong choice")
    
def hallway():
	print ('you are in a dark hallway and there is a errie hooting comming from behind you')
	answer = input(" what do you do?   ")
	room1.get(answer,err)()
	if (answer == 'run'):
		fl [0]= 1

def room2():
	print("you entered into a room ")
	print("you have a door to the right ")
	print("and a stair to the left ")
	answer2= input('where do you go now : >>>>>')
	room2dict.get(answer2,err)()
	if (answer2 == 'right'):
		fl[1]=1
room1 = {
	
	'run' : running,
	'wait' : death
}
room2dict = {

	'right' : door_room2,
	'left' : stair_room2
}
fl = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print ('                                Welcome to this world')
hallway()
if (fl[0]==1):
	room2()
if (fl[1]==0):
	print("you went to the second floor of the buliding and there is a window in fornt of you where you can see a mountain ")
if (fl[1]==1):
	print("the door is closed, you have to find a key to the door")
	room2()	
#x= room1[answer]
#x()

for i in range(len(fl)):
	print(fl[i])