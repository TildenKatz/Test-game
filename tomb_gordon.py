#JB
#01/13/19
#Tomb of Gordon the Wise

import random
import time

name = input ("Halt! Only a fool would approach an orc encampment alone. By what name do you call yourself?")

print ("Ah. Well, " + name +", your reputation precedes you. For too long have you roamed these hills unchecked. For too long have your kind enslaved the minds of the orc, wizard.")

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
branch = 0
key = 0

required = ("\nUse only A, B, or C\n")


def intro():
  print ("We know of the tomb in which you seek, "
  "the tomb of Gordon the Wise, first of his name, Knight Errant and Whisperer to the Wind. " 
  "Though your cause is noble, a wizard is always up to trickery, "
  "and I cannot deny that the opportunity to slay a wizard without his "
  "magical texts thrills me greatly. "
  "My Orc kin, draw swords! You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the lead orc
  B. Try to persuade the orcs with promises of gold in the tomb which you will share
  C. Run""")
  choice = input(">>> ") 
  if choice in answer_A:
       option_rock()
  elif choice in answer_B:
    print ("\nFoolish half-elf. We Orc have no need so great of gold from a desecrated tomb of a knight! Pray to whatever gods you think might hear your pitiful prayers."
    "\n\nYou are stabbed repeatedly, you body burned. All records of your travels to this land are wiped away as the crows pick at what remains.")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe orc is stunned, but regains control. As the other orcs take this as a challenge to one on one combat, he begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Beg for mercy
  C. Run up a nearby tree""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nThe orc shows no mercy " 
    "You are stabbed repeatedly, your body burned. All records of your travels to this land are wiped away as the crows pick at your corpse. "
    "What a pity. \n\nYou failed!")
  elif choice in answer_C:
    option_tree()
  else:
    print (required)
    option_rock()

def option_tree():
  print ("\nYou quickly climb the tree. "
  "One of the branches you grab breaks violently, as you fall to "
  "the ground. Do you arm yourself with the fallen branch? Y/N?")
  choice = input(">>> ")
  if choice in yes:
    branch = 1
  else:
    branch = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide behind the tree
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nThe orc easily spots you and "
    "mocks your pathetic attempt to leave battle. "
    "If there's one thing orcs hate more than wizards, it's a coward.\n\nYou are stabbed repeatedly, your body burned. All records of your travels to this land are wiped away as the crows pick at what remains.")
  elif choice in answer_B:
   if branch > 0:
    print ("\nYou wait for the orc to approach "
    "with his sword drawn. "
    "He swings swiftly down, in a mad rage. "
    "The orc, while much stronger, is not smart. "
    "His strike downward hits the ground, as you jump "
    "to the side at the last second. "
     "With his sword stuck in the mud, you begin to "
     "beat his skull in until he is clearly dead. "
     "\n\nYour victory has earned you the respect of "
     "the remaining orcs. You pass the rest of the clan in peace."
     " Not far from the encampment you notice an abandoned town. You decide to explore it.")
    option_town()
   else: 
     print ("\nYou dart past the orc. While your moves are swift, you are defenseless. He simply awaits the right time to strike. "
     "Eventually his sword lands right on your head, splitting your brain in half. \n\nYou are stabbed repeatedly, your body burned. All records of your travels to this land are wiped away as the crows pick at what remains.")
  elif choice in answer_C:
    print ("As the orc enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the orc turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the orc's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an orc. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nYou approach an old, abandoned town. "
  "As you explore some, you realize this is the place  "
  "you have been seeking. The tomb is nearby, and with it, "
  "your spellbooks! You reach a great hall and swing open the doors. "
  "Searching for any signs of the tomb's location, you find a strange "
  "key embedded in a crest above the throne. "
  "\nDo you take it? Y/N")
  choice = input(">>> ")
  if choice in yes:
    key = 1 #adds a key
  else:
    key = 0
  print ("Engraved over the throne, written in elvish: Quor was Al man, ernath sar emar him. "
    "A quick translation reads: Here was a man, under we honor him.")
  time.sleep(1)
  if key > 0:
    print ("\nAs soon as you remove the key, the throne breaks apart, "
    "revealing beneath it a descending staircase. "
    "Do you:")
    time.sleep(1)
    print (""" A. Go down the stairs 
    B. Keep looking for more clues""")
    choice = input(">>> ")
    if choice in answer_A:
      print ("You descend until you find a narrow hallway leading to a locked door. You insert the key and enter.")
      option_tomb()
    elif choice in answer_B:
        print ("\nEventually you decide there is no other option than to go down the stair. You soon approach a locked door and insert your key and enter.")
        option_tomb()
  else: #If the user didn't grab the key
     print ("\nYou wander throughout the town for a day or so, looking for the tomb. "
     "\n\nEventually hungry wolves track down your scent. As they rip you limb from limb, you wonder if that key had some significance.")

def option_tomb():
    print ("\nYou enter the room and find yet another door. Written above this door reads: Here lies the tomb of Gordon the Wise. "
    "Paying respect is the right thing to do. Enemies of this honored warrior beware. This tomb shall forever protect this honored Knight. "
    "Beyond this door lie three paths, your final test. Only dedicated friends of Gordon know the answer to this question. "
    "Which path will lead you to this Knight's final resting place? ")
    time.sleep(1)
    print (""" A. Head down the left hallway
    B. Head straight
    C. Head down the right hallway""")
    choice = input(">>>")
    if choice in answer_A:
      print ("You find a dead end. However, to you right is room with a painting of a woman smiling directly at you, like she knows a secret. As you approach to further investigate, a trap door underneath you opens and you fall into a pit of acid and die.")
    elif choice in answer_B:
      print ("You walk into what appears to be an armory. This equipment may prove useful in future journeys. As you approach a sword in the center of the rack, you step on a stone that activates a device which shoots you in the neck with a poisonous arrow. As you slowly die, you ponder why that sword was so well guarded.")
    elif choice in answer_C:
      print ("You approach a great chamber. Surely, this is the main section of Gordon's tomb.")
      option_record()
    else: 
     print (required)    

def option_record():
    print ("\nEntering the inner tomb, you see what appears to be Gordon's coffin. Beside the coffin, you see a text: Life and Records of Gordon the Wise. You also see your magical books! While you are relieved, you can't help but be curious as to who this Gordon was.")
    time.sleep(3)
    print (""" A. Take your books and leave
    B. Read the record""")
    choice = input(">>>")
    if choice in answer_A:
      print ("Thankful to have your spells back, you leave the tomb. Years later, an ancient evil is awoken and destroys the lands. None can stop this foe. As you prepare to make your final stand against certain death, you remember back to that day at the tomb of Gordon and wonder, would the knowledge within that old tomb have prevented this? You die like a warrior-poet. ")
    elif choice in answer_B:
      time.sleep(5)  
      print ("Herein lie the records of the life and times of Gordon the Wise, first of his name, Knight Errant and Whisperer to the Wind. "
        "\n\nIt is said by many of the commonfolk from where Gordon called home that he was born a demigod. One day, Celestian, god of stars and wanderers, "
        "came down from the heavens to explore the Forgotten Realms. During his travels he came upon a small village. On the outskirts of the hamlet was a young girl, "
        "Marianna. Though he dared not disturb the peace of the village, he met with the young girl down by the riverside every morning and evening. "
        "As these secret meetings became more common, Marianna soon realized she was with child. Thus, she gave birth to a son. "
        "Celestian, unwilling to accept fatherhood, cast the young girl to the realm of Vecna, god of evil secrets. There her tongue, eyes, and ears were removed, as she was left to roam helpless "
        "for the rest of her days. Taking pity on the young boy and somewhat frightened by the boy's eyes, Celestian took him to a larger city and abandoned him at a random doorstep, leaving only a note on the boy: "
        "He shall be called Gordon, a common name of his own people. "
        "\n\nHumans are prone to wild fantasies, and their recordkeeping is vastly inferior to that of the Elf. "
        "Through careful examination of census records, it came to pass that a wandering mystic named Eron was most likely the father of Gordon. As of the writing of these records, "
        "Eron's whereabouts are unknown. Marianna died at twenty years of age, victim of the pestilience. "
        "\n\nAs a boy, Gordon was a rebellious child. Prone to acts of trickery and violence against enemies, the youth was disciplined heavily. "
        "He was raised by a blacksmith and his barren wife. Unfortunately, our archivists could not retrieve the census records to determine their names. "
        "It is written that in his twelfth year, Gordon developed a keen interest in the magical arts, begging a local mage to teach him some amateur and harmless spells. "
        "A natural, Gordon cultivated this fascination of magic. Indeed, this interest is how the Elvish initially came to recognize him. "
        "\n\nEventually war came to his people. Kings fought for title, honor, and glory. Having no other profession of interest to the crown, he was conscripted into the military. "
        "During that Battle of Shattered Crowns, Gordon was stationed as an archer. As the days waned, both sides suffered significant losses. Records show that Gordon lost two toes during one bloody episode. "
        "On day thirty-five of the battle, Zebulon, Gordon's king, faced defeat at the hands of the opposing army. The aging king which he opposed decided to employ a band of orc mercenaries. Outnumbered and weak, Zebulon considered the fate of his army. "
        "Surely, he thought, this king would show no quarter to even his lowliest private. Too many of the nobility of both sides had been slain. This was not a war of honor. The final stand would be suicide by combat. "
        "\n\nOn the morning of the final battle, Gordon saw his king's face. The look was of a hopeless man. No grand speeches were given, no inspiration. Only orders. "
        "As soon as the battle began, Gordon saw the front lines faltering. It would not be long before they reached the archers just before the final blow upon Zebulon and his king's guard. "
        "Unwilling to die like a lamb being led to the slaughter, Gordon gathered his nearby archer comrades. In what appeared to the opposing king as the deserting archery line, Gordon traveled hard to through the thick forest to circumvent the entire bloody scene. "
        "Just as he had wagered, the opposing king, in an act of ego and lack of respect for Zebulon's forces, had left himself largely unarmed. "
        "Gordon ordered his fellow archers to fire, wiping out most of the king's guard. Then he led the charge on the king. Gordon ran up on the king, drew the man's own sword, and drove it through his heart. "
        "It was not long before the orcs noticed the massacre on the back line. These mercenaries would not work for free. Gordon grabbed a boy attending the horses and carts and ordered him to send word that Zebulon would pay the orcs handsomely to turn sides. "
        "As the orcs' only chance at receiving payment, they did so. And the battle was won. "
        "King Zebulon thanked Gordon for his services and named him Gordon the Wise. Ultimately ungrateful for this salvation, and angered that Gordon had indebted the crown to the orcs without his permission, Zebulon sent Gordon away. "
        "He was ordered to roam the country in pursuit of magical knowledge. And should he be called upon, he should return to Zebulon's service, all the wiser and greater the magical fighter. "
        "\n\nTexts still survive within this tomb that tell of Gordon's travels, but this is simply the core account of his life. Soon Gordon became a wandering Eldritch Knight, freed from service to any one Lord. "
        "We Elves have been unable to find any record as to the circumstances surrounding Gordon's death. This tomb and these accounts are to honor our friend. "
        "Long ago, Gordon the Wise saved many of our people, and we are humbly in his debt. "
        "\n\nIt is said that deep within these walls lies the answer to his resurrection. Human prophecies tell that one day, an ancient evil shall be awoken. "
        "Many a brave warrior and skilled spellcaster will attempt to silence this unholy villain. Should the day come where hope is lost and the free peoples of these lands should face certain doom, "
        "remember this place and this Knight. Remember his wanderings and his wisdom. Should the gods be the only ones to ever see this tomb, look favorably upon this imperfect man. "
        "Regard him not as a tyrant, nor a holy man. Remember him as one orphaned to the world, wise beyond this realm, and perhaps one whose tale is not over yet...") 
    

 
    else:
     print (required)

intro()