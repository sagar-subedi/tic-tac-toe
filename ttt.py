# let's first print the board of ttt

# from turtle import screensize


import string
import os


gameArr = [' ']*9
ps = ['O', 'X']

str ="      |      |      \n   {}  |  {}   |   {}  \n______|______|______\n"*3

def playGame(gameArr):
   player = 1
   # //resets gameArr
   os.system('cls')
   displayGame(gameArr)
   for x in range(0,len(gameArr)):
      gameArr[x] = ' '
   # do it 9 times:
   for x in range(0, len(gameArr)):
      player = 1-player
      print("Turn: Player {}".format(player+1))
      slot = askSlot()

      gameArr[slot] = ps[player]
      os.system('cls')
      displayGame(gameArr)
      
   #    #Player, enter the desired slot: as slot number
   #    update gameArr'slot number' with ps[player]
   #    clear screen
   #    displayGame
   #    switch player
   #    next

   # afther the माथिको फर लुप
   # play one again
   playAgain = againAsk()
   if playAgain == 'Y': playGame(gameArr)
   elif playAgain == 'N': pass
   else: againAsk() #askagain
      # if yes: call the function once again
      # else exit the function

def askSlot():
   slotNo = int((input("Enter the desired slot number: ")))  
   if (slotNo in range(0, 9)) and (gameArr[slotNo] not in ['O', 'X']):
      return slotNo
   else:
      if (slotNo not in range(0,9)): print("Input out of range, enter again")
      elif (gameArr[slotNo] in ['O', 'X']): print("Slot already occupied, enter another one")
      return askSlot()

def againAsk():
   ans = (input("Do you want to play again Y or N")).upper()
   if  ans in ['Y', 'N']: return ans
   else:
      print("Invalid respose, enter Y or N?")
      return againAsk()


 
def displayGame(gameArr):
   print(str.format(gameArr[0], gameArr[1], gameArr[2], gameArr[3], gameArr[4], gameArr[5], gameArr[6], gameArr[7], gameArr[8]))


playGame(gameArr)