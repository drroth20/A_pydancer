





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
#create the screen class for the screen
class Screen:

	#Screen should instantiate with a size
	def __init__(self,size):
		self.size = size
		self.res = ['_']*self.size
		self.bg = ['_']*self.size
		

	#Screen should be able to redraw itself with updates	
	def Redraw_Screen(self,playerpos,playermarker):
		self.res = ['_']*self.size
		self.res[playerpos] = playermarker
		print('\n'*100)
		print(self.res)






#create a player class
class Player:


	#player object should instantiate with a starting position and a character that will represent them
	def __init__(self,position,marker='A'):

		self.position = position
		self.marker = marker

	
	def control_me(self,direction,screen):

			if direction[0].upper() == 'A':
				if self.position == 0:
					self.position = 1
				self.position -= 1
				
			elif direction[0].upper() == 'D':
				if self.position == 9:
					self.position = 8
				self.position += 1
			elif direction[0].upper() == 'Q':
				exit(0)
			screen.Redraw_Screen(self.position,self.marker)


new_screen = Screen(10)
pl = Player(4,'A')

while True:

	command = input('Which direction? A or D?').upper()
	if command.upper() == 'quit':
		break
	pl.control_me(command,new_screen)

