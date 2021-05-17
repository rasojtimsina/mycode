#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
      print('You see a ', list(rooms[currentRoom]['item'].keys()))
    #print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")


  if 'east' in rooms[currentRoom]:
      print(f"The item on your east is {rooms[currentRoom]['east']}")
  if 'west' in rooms[currentRoom]:
      print(f"The item on your west is {rooms[currentRoom]['west']}")
  if 'north' in rooms[currentRoom]:
      print(f"The item on your north is {rooms[currentRoom]['north']}")
  if 'south' in rooms[currentRoom]:
      print(f"The item on your south is {rooms[currentRoom]['south']}")


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Bedroom',
                  'north' : 'Guestroom',
                  'item'  : {'key': 'You can open the door now','lock': 'You can lock the door'}
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : {'monster': 'I am a monster'},
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : {'potion': 'Dont know what its used for'},
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'east'  : 'Guestroom',
                  'item'  : {'horse': 'Lets win this battle'}
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : {'cookies': 'num num'},
               },
            'Bedroom' : {
                    'east' : 'Hall',
                    'item' : {'sword': 'I am a ninja'}
               },
            'Guestroom' : {
                    'south' : 'Hall',
                    'item'  : {'map': 'I know where to go'}                    
            }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory

      inventory += [move[1]]

      #display a helpful message
      print(move[1] + ' got!')
      print(rooms[currentRoom]['item'][move[1]])

        #delete added item

      del rooms[currentRoom]['item'][move[1]]

      #delete the item from the room
      if len(rooms[currentRoom]['item'])<1:
          del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'sword' in inventory and 'horse' in inventory:
    print('You were able to beat the enemy in warrior style.. YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

