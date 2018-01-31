
"""==================================================================

 A PROGRAM FOR TIC TAC TOE GAME WITH AI MOVES
________________coded by Mr ari
"""


# here is all  Functions definitions

import random

#Function to print the array

def update(array):
    i=7
    while i>=1:
        print (" "*25,array[i],"|",array[i+1],"|",array[i+2])
        if i==7 or i == 4:
            print (" "*25,"---------")
        i=i-3


#function which checks win ,,,, if win return 1 otherwise return 0

def checkWinning(array,letter):

    if (array[7]==letter and array[8]==letter and array[9]==letter) or (array[4]==letter and array[5]==letter and array[6]==letter) or (array[1]==letter and array[2]==letter and array[3]==letter) or (array[1]==letter and array[7]==letter and array[4]==letter) or (array[2]==letter and array[5]==letter and array[8]==letter) or (array[3]==letter and array[6]==letter and array[9]==letter) or (array[7]==letter and array[3]==letter and array[5]==letter) or (array[1]==letter and array[5]==letter and array[9]==letter):
        return 1
    else :
        return 0


#getRandom generate a random number which is not in the given list

def getRandom(track_XY):
    while True:
        r = random.randint(0,8)
        if r not in track_XY:
            return r



#---------------------------------------------------------------------------------

#                           Funtions for AI

#---------------------------------------------------------------------------------

"""   AI moves  ____________
_______________ 1 . First check if cpu can win in the next move or not if it can then it will return the postion for the next move.
_______________2.It checks whether in the next move user can win or not if user can win
                  then go for a defensive move.
_______________3.if any defensive move or attacking move not available then go for
                  a random space ------------ precision is ****  1.corner
                                                                 2.side
                                                                 3.center
"""

def DefenceOponent(array,letter):
    for i in range (4):
        if i == 0:
            j=7
            while j >= 1 :
                if array[j]==letter and array [j+1]==letter:
                    return j+2

                elif array[j+1]==letter and array [j+2]==letter:
                    return j
                elif array[j]==letter and array [j+2]==letter:
                    return j+1
                j=j-3

        elif i==1:
            j=3
            while j>=1:
                if array[j]==letter and array [j+3]==letter:
                    return j+6
                elif array[j+3]==letter and array [j+6]==letter:
                    return j
                elif array[j]==letter and array [j+6]==letter:
                    return j+3
                j=j-1

        elif i==2:

            j=3
            if array[j]==letter and array [j+2]==letter:
                return j+4
            elif array[j+2]==letter and array [j+4]==letter:
                return j
            elif array[j]==letter and array [j+4]==letter:
                return j+2


        elif i==3:

            j=1
            if array[j]==letter and array [j+4]==letter:
                return j+8
            elif array[j+4]==letter and array [j+8]==letter:
                return j
            elif array[j]==letter and array [j+8]==letter:
                return j+4


    return 0


def CheckWinNext(array,letter):
    for i in range (4):
        if i == 0:
            j=7
            while j >= 1 :
                if array[j]==letter and array [j+1]==letter:
                    return j+2

                elif array[j+1]==letter and array [j+2]==letter:
                    return j
                elif array[j]==letter and array [j+2]==letter:
                    return j+1
                j=j-3

        elif i==1:
            j=3
            while j>=1:
                if array[j]==letter and array [j+3]==letter:
                    return j+6
                elif array[j+3]==letter and array [j+6]==letter:
                    return j
                elif array[j]==letter and array [j+6]==letter:
                    return j+3
                j=j-1

        elif i==2:

            j=3
            if array[j]==letter and array [j+2]==letter:
                return j+4
            elif array[j+2]==letter and array [j+4]==letter:
                return j
            elif array[j]==letter and array [j+4]==letter:
                return j+2


        elif i==3:

            j=1
            if array[j]==letter and array [j+4]==letter:
                return j+8
            elif array[j+4]==letter and array [j+8]==letter:
                return j
            elif array[j]==letter and array [j+8]==letter:
                return j+4

    return 0


def CheckCorner(tracker):
    for i in range (8):
        corners =[7,9,3,1]
        choice = random.choice(corners)
        if choice not in tracker :
            return choice

    return 0

def CheckSide(tracker):
    for i in range (8):
        corners =[8,6,2,4]
        choice = random.choice(corners)
        if choice not in tracker :
            return choice

    return 0



def Simple_AI(array,tracker,letter,letter_cpu):
	win = CheckWinNext(array,letter_cpu)
	if win != 0 and win not in tracker:
         return win
	else:
		defence = DefenceOponent(array,letter)
		if defence != 0 and defence not in tracker:
		    return defence
		else:
			corner = CheckCorner(tracker)
			if corner != 0:
				return corner
			else:
				side = CheckSide(tracker)
				if side != 0:
					return side
				else :
					return 5



#------------------------------------------------------------------------------



def swap_TF(boolianValue):
    return not boolianValue

def TF_generator(inp):
    if inp == 'X':
        return 0
    else:
        return 1



"""-----------------------------------------------------------------------------
                             Main Function
-----------------------------------------------------------------------------"""


print ("TIC - TAC - TOE Game")
print()

userInput= "YES"
FirstC = input ("Enter what you choose first X or O: ").upper()
loop = TF_generator(FirstC)
userWin = 0
compWin = 0
#while loop for play again and again

while userInput == "YES" or userInput == "Y":

    #Variable declarations

    array = [" "," "," "," "," "," "," "," "," "," "]
    if (loop%2)==0:
        update(array)
    checkX =0
    checkY =0
    XY_track=[]
    #--------------------------------------------------------
    while len (XY_track)<=8 and checkX == 0 and checkY == 0:

        if loop%2 == 0:
            inp = int(input("Enter the position you want to enter 'X' "))
            array[inp]='X'
            XY_track.append(inp)
            checkX=checkWinning(array,'X')

        else :
            random_num= Simple_AI(array,XY_track,'X','O')
            XY_track.append(random_num)
            array[random_num]='O'
            checkY=checkWinning(array,'O')
            update(array)
        loop=loop+1

    if checkX == 1:
        print()
        print("-----------------------------You win-----------------------------")
        update(array)
        userWin = userWin + 1
        if (userWin >compWin ):
            print("You are winning by",userWin,"-",compWin)
        elif userWin<compWin :
            print ("Computer is winning by",userWin,"-",compWin)
        else :
            print ("MAtch is draw by",userWin,"-",compWin)
    elif checkY==1:
        print ()
        print("-------------------------Computer win------------------------------")
        update(array)
        compWin = compWin + 1
        if (userWin > compWin):
            print("You are winning by",userWin,"-",compWin)
        elif userWin<compWin:
            print ("Computer is winning by",userWin,"-",compWin)
        else :
            print ("MAtch is draw by",userWin,"-",compWin)

    else :
        print()
        print("____________________________Draw_____________________________")
        update(array)
        if (userWin > compWin):
            print("You are winning by",userWin,"-",compWin)
        elif userWin<compWin :
            print ("Computer is winning by",userWin,"-",compWin)
        else :
            print ("Match is draw by",userWin,"-",compWin)


    print()
    userInput = input ("Do you want to play again ? ").upper()

"""--------------------------------------------------------------------------"""
