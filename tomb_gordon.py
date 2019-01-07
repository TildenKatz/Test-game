# name: JB
# date: 06-01-2019
# text-based adventure game: Tomb of Gordon the Wise

import random
import time

def displayIntro():
	print("We've been expecting you, Neres.")
	time.sleep(2)
	print("Your reputation in wizardry precedes you.")
	time.sleep(2)
	print("For too long have you roamed these lands in search of the tomb")
	time.sleep(2)
	print("and for too long we have allowed you to pass through these lands...")
	time.sleep(4)
	print("unharmed...")


displayIntro()

def choosePath():
	path = ""
	while path != "1" and path != "2":
		path = input("How will you respond? Negotiate or attack? (1 or 2): ")
	
	return path

def checkPath(chosenPath):
	print("My life means nothing without my books. Take what you will, bandits!")
	time.sleep(2)
	print("The fruits of my labor will benefit many, my friends. Yourselves included.")
	time.sleep(2)
	print("You take your dagger out and prepare to attack.")
	print()
	time.sleep(2)

	correctPath = random.randint(1,2)

	if chosenPath == str(correctPath):
		print("Haha foolish half-elf. We have better foes to face than a wizard without his spells.")
		print("We shall trust that your mission is important, though we have our doubts that your passion may exceed your intellect.")
	else:
		print("You are weak, wizard. Say what prayers you will to your gods.")
		print("The orcs begin to surround you with their weapons raised.")
		print("You are stabbed repeatedly, your body burned. All records of your travels to this land are wiped away.")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
	displayIntro()
	choice = choosePath()
	checkPath(choice)
	playAgain = input("Do you want to play again?")