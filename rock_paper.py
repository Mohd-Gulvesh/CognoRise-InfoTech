#                      Task - 03  (" Rock Paper Scissor Game "

"""
rock vs paper-> paper wins
rock vs scissor-> rock wins
paper vs scissor-> scissor wins
"""

import random
l=["rock","scissor","paper"]

while True:
    Comcount=0
    ucount=0
    uc=int(input('''
Game Start.....
1 Yes
2 No | Exit 

          '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper
                                '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Comchoice=random.choice(l)
            print(uchoice)
            print(Comchoice)

            if Comchoice==uchoice:
                print("Computer Value",Comchoice)
                print("User Value",uchoice)
                print("Game-Draw")
                ucount=ucount+1
                Comcount=Comcount+1
            elif (uchoice=="rock" and Comchoice=="scissor") or ( uchoice 
                    =="paper" and Comchoice=="rock")or (uchoice=="scissor" and Comchoice=="paper"):
                print("Computer Value",Comchoice)
                print("User Value",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value",Comchoice)
                print("User Value",uchoice)
                print("Computer Win")
                Comcount=Comcount+1

        if ucount==Comcount:
            print("Final Game-Draw...")
            print("User Score",ucount)
            print("Computer Score",Comcount)
        elif ucount>Comcount:
            print("Final You win the Game...")
            print("User Score",ucount)
            print("Computer Score",Comcount)
        else:
            print("Final Computer win the Game...")
            print("User Score",ucount)
            print("Computer Score",Comcount)


        pass
    else:
        break

