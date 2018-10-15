





'''
screen = ['_','_','_','_','_','_','_','_','_','_']
background = ['_']*10


for i in range(10):
	screen[i] = background[i]

#the index on the screen that the player will appear
playerpos = 4
#draws the player at the index on the screen list
screen[playerpos] = 'A'
#shows the character on the screen
print(screen)



#erases the character
screen[playerpos] = background[playerpos]
#moves the character
playerpos = playerpos - 1
#Redraws the character at their new position
screen[playerpos] = 'A'

#clears page and redraws character at new position on new screen

print('\n'*100)
print(screen)
'''
class Screen:

	def __init__(self, size):

		self.size = size
		screen = ['_']*size
		background = ['_']*size

	def Draw_Screen():
		print('\n')*100
		print(screen)







class Player:

	marker = 'A'

	def __init__(self,position):

		self.position = position

	def Blit_Player():
	
		orders = ['W','A','S','D']
		
		direction = Receive_Command(orders)

		if direction == 'A':
			self.position = position - 1

		elif direction == 'D':
			self.positon = position + 1

	def Receive_Command(direction):

		choice = input('Which direction? WASD ').upper()

		if choice in direction:
			return choice

		elif choice == 'QUIT':
			exit(0)

		else:
			return Receive_Command(direction)

	def Report_Position():
		return self.position





Character = Player(4)
Playspace = Screen(10)

Playspace.Draw_Screen



	