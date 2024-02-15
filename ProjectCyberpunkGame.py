### CODE TEST ###

# This is where I try my if, if-else, if-elif-else skills, and if with input statement skills.
#
#
# IF STATEMENTS
# if 5==5:
#    print("Valid entry")
#
#
# IF-ELSE STATEMENTS
# if 5==3:
#    print("I learned about if statements")
# else:
#    print("I also learned about else statements")
#
# if 1==1:
#     print("This is true")
# else:
#     print("This is not true")
#
#
# IF-ELIF-ELSE STATEMENTS
# if 2==9:
#    print("Hmmm")
# elif 3==0:
#    print("Maybe not")
# elif 3>=2.2:
#    print("This is correct")
# elif 4<=0:
#    print("Not likely")
# else:
#    print("Try again")
# 
# if "x"=="x":
#    print("This is different")
# elif "x"==0:
#    print("Maybe not")
# elif "x">=2.2:
#    print("This is correct")
# elif "x"<=0:
#    print("Not likely")
# else:
#    print("Try again")
# 
# 
# USING IF ELSE STATEMENTS WITH AN INPUT
# varMin5 = "You chose A and decided to destroy it for no reason at all"
#
# print("You came across a table. Do you: A) destroy it OR B)rework it and resell it to make a quick buck")
# input("Choose A or B and enter:")
#
# if "B"=="B":
#     print("you reworked it and met with a stranger online to sell it but when you met, you ended up being robbed of the table, your phone, and wallet. how unfortunate.")
# else:
#     print(varMin5)
# 
# 
# 



### GAME SCRIPT ###
### Number of Endings: 4
### Time to complete 1 game: approximately 6 minutes


#-----Title: Neon Streets: The Cybernetic Conspiracy



#-----Minute 1 INTRO:-----
# You find yourself standing on a rain-soaked street corner in the heart of the neon-lit city, Hypernet City. To your left, a shady alleyway beckons with the promise of intrigue. To your right, a sleek hovercar speeds by, its occupants casting curious glances your way. Do you:
#---Choices:
# Investigate the shady alleyway. --original path1--
# Hail a passing hovercab and follow it to its destination.

print("You find yourself standing on a rain-soaked street corner in the heart of the neon-lit city. To your left, a shady alleyway beckons with the promise of intrigue. To your right, a sleek hovercar speeds by, its occupants casting curious glances your way. Do you:")
print("A)Investigate the shady alleyway.")
print("OR")
print("B)Hail a passing hovercab and follow it to its destination.")
input("Choose 'A' or 'B' and enter:")

varMin2P1 = "You choose to investigate the shady alleyway and stumble upon a group of cybernetically enhanced street thugs conducting a clandestine deal. They don't seem to have noticed you yet. Do you:"
varMin2P2 = "You choose to hail a passing hovercab and follow it to its destination, hoping it will lead you to valuable information about the heist. The hovercab takes you deep into the heart of the city's bustling metropolis, finally coming to a stop outside a high-rise corporate building adorned with security cameras and armed guards. Do you:"

if "B"=="B":
     print(varMin2P2)
else:
     print(varMin2P1)
    


#-----Minute 2 PATH 1:-----
varMin2P1 = "You choose to investigate the shady alleyway and stumble upon a group of cybernetically enhanced street thugs conducting a clandestine deal. They don't seem to have noticed you yet. Do you:"
# original path1 - You choose to investigate the shady alleyway and stumble upon a group of cybernetically enhanced street thugs conducting a clandestine deal. They don't seem to have noticed you yet. Do you:
#---Choices:
# Sneak past the thugs to eavesdrop on their conversation.--original path1--
# Confront the thugs and demand to know what they're up to.--path1 bad end, continue to path 1.1--
print("A)Sneak past the thugs to eavesdrop on their conversation.")
print("OR")
print("B)Confront the thugs and demand to know what they're up to.")
input("Choose 'A' or 'B' and enter:")

varMin3P1 = "You manage to sneak past the thugs and overhear snippets of conversation about a high-profile corporate heist planned for tonight. Before you can learn more, one of the thugs spots you and pulls out a weapon. Do you:"
varMin2P11 = "You decide to confront the thugs and demand to know what they're up to, hoping to gather valuable information about the heist. However, before you can utter another word, the thugs react with hostility, drawing their weapons and surrounding you. It becomes evident that they are not willing to negotiate or share their secrets. Do you:"
if "B"=="B":
     print(varMin2P11)
else:
     print(varMin3P1)




#---Minute 2 PATH 2:
varMin2P2 = "You choose to hail a passing hovercab and follow it to its destination, hoping it will lead you to valuable information about the heist. The hovercab takes you deep into the heart of the city's bustling metropolis, finally coming to a stop outside a high-rise corporate building adorned with security cameras and armed guards. Do you:"
# branch path2 - You choose to hail a passing hovercab and follow it to its destination, hoping it will lead you to valuable information about the heist. The hovercab takes you deep into the heart of the city's bustling metropolis, finally coming to a stop outside a high-rise corporate building adorned with security cameras and armed guards. Do you:
#---Choices:
# Infiltrate the corporate building disguised as a maintenance worker to gather intel.--branch path2--
# Attempt to hack into the building's security systems from a remote location.--path2 bad end--
print("A)Sneak past the thugs to eavesdrop on their conversation.")
print("OR")
print("B)Confront the thugs and demand to know what they're up to.")
input("Choose 'A' or 'B' and enter:")

if "B"=="B":
     print("")
else:
     print(varMin3P1)



#-----Minute 3 PATH 1:-----
varMin3P1 = "You manage to sneak past the thugs and overhear snippets of conversation about a high-profile corporate heist planned for tonight. Before you can learn more, one of the thugs spots you and pulls out a weapon. Do you:"
# original path1 - You manage to sneak past the thugs and overhear snippets of conversation about a high-profile corporate heist planned for tonight. Before you can learn more, one of the thugs spots you and pulls out a weapon. Do you:
#---Choices:
# Attempt to talk your way out of the situation. --path1 bad end--
# Draw your own weapon and prepare for a fight.--original path1--
print("A)Attempt to talk your way out of the situation.")
print("OR")
print("B)Draw your own weapon and prepare for a fight.")
input("Choose 'A' or 'B' and enter:")

if "A"=="A":
     print("")
else:
     print(varMin4P2)

#---Minute 3 PATH 2:
varMin3P2 = "You opt to infiltrate the corporate building disguised as a maintenance worker, blending in seamlessly with the bustling crowd of employees. As you navigate the labyrinthine corridors, you overhear snippets of conversation about the impending heist. However, your cover is at risk of being blown by an approaching security patrol. Do you:"
# branch path2 - You opt to infiltrate the corporate building disguised as a maintenance worker, blending in seamlessly with the bustling crowd of employees. As you navigate the labyrinthine corridors, you overhear snippets of conversation about the impending heist. However, your cover is at risk of being blown by an approaching security patrol. Do you:
#---Choices:
# Attempt to talk your way out of the situation. --path2 bad end--
# Draw your own weapon and prepare for a fight.--branch path2--
print("A)Attempt to talk your way out of the situation.")
print("OR")
print("B)Draw your own weapon and prepare for a fight.")
input("Choose 'A' or 'B' and enter:")



#-----Minute 4 PATH 1:-----
varMin4P1 = "You choose to draw your weapon, and a fierce firefight erupts in the alleyway. After a tense exchange of gunfire, you emerge victorious but wounded. As you catch your breath, you notice a mysterious figure watching you from the shadows. Do you:"
# original path1 - You choose to draw your weapon, and a fierce firefight erupts in the alleyway. After a tense exchange of gunfire, you emerge victorious but wounded. As you catch your breath, you notice a mysterious figure watching you from the shadows. Do you:
#---Choices:
# Approach the mysterious figure and demand answers.--original path1--
# Ignore the figure and tend to your wounds before they worsen.--path1 bad end--
print(varMin4P1)
print("A)Approach the mysterious figure and demand answers.")
print("OR")
print("B)Ignore the figure and tend to your wounds before they worsen.")
input("Choose 'A' or 'B' and enter:")

#---Minute 4 PATH 2:
varMin4P2 = "You choose to confront the security patrol and attempt to bluff your way past them. However, they seem suspicious of your presence and demand to see your identification. Do you:"
# branch path 2 - You choose to confront the security patrol and attempt to bluff your way past them. However, they seem suspicious of your presence and demand to see your identification. Do you:
#---Choices:
# Try to bribe the security patrol with credits or valuable information. --path2 bad end--
# Make a run for it and try to lose them in the maze-like corridors of the corporate building.--branch path2--





#-----Minute 5 PATH 1:-----
varMin5P1 = "You cautiously approach the mysterious figure, who reveals themselves to be a rogue hacker with valuable information about the corporate heist. They offer to help you infiltrate the corporate headquarters where the heist is planned to take place. Do you:"
# original path1 - You cautiously approach the mysterious figure, who reveals themselves to be a rogue hacker with valuable information about the corporate heist. They offer to help you infiltrate the corporate headquarters where the heist is planned to take place. Do you:
#---Choices:
#Accept the hacker's offer and team up to pull off the heist.--original path1--
#Decline the hacker's offer and attempt to thwart the heist on your own terms.
print(varMin5P1)
print("A)Accept the hacker's offer and team up to pull off the heist.")
print("OR")
print("B)Decline the hacker's offer and attempt to thwart the heist on your own terms.")
input("Choose 'A' or 'B' and enter:")

#---Minute 5 PATH 2:
varMinP2 = "You opt to make a run for it, darting through the corridors of the corporate building with the security patrol hot on your heels. As you reach a dead-end, you realize you're trapped with nowhere left to run. Suddenly, a mysterious figure emerges from the shadows and offers you a way out through a hidden ventilation shaft. Do you:"
# branch path 2 - You opt to make a run for it, darting through the corridors of the corporate building with the security patrol hot on your heels. As you reach a dead-end, you realize you're trapped with nowhere left to run. Suddenly, a mysterious figure emerges from the shadows and offers you a way out through a hidden ventilation shaft. Do you:
#---Choices:
# Trust the mysterious figure and follow them into the ventilation shaft.--branch path2--
# Refuse the offer and surrender to the security patrol, hoping to negotiate your way out of trouble.--path2 bad end--
print("A)Trust the mysterious figure and follow them into the ventilation shaft.")
print("OR")
print("B)Refuse the offer and surrender to the security patrol, hoping to negotiate your way out of trouble.")
input("Choose 'A' or 'B' and enter:")




#-----Minute 6 PATH 1:-----
varMin6P1 = "You accept the hacker's offer and together, you orchestrate a daring infiltration of the corporate headquarters. Using their hacking skills and your combat expertise, you navigate through security systems and guards to reach the heart of the facility. As you stand before the vault containing the coveted prize, you realize that your choices will determine the fate of the city. Do you:"
# original path1 - You accept the hacker's offer and together, you orchestrate a daring infiltration of the corporate headquarters. Using their hacking skills and your combat expertise, you navigate through security systems and guards to reach the heart of the facility. As you stand before the vault containing the coveted prize, you realize that your choices will determine the fate of the city. Do you:
#---Choices:
#Proceed with the heist and claim the valuable assets within the vault.--original path1--
#Have a change of heart and sabotage the heist, opting to protect the city from further corporate exploitation.--original path1.1--
print(varMin6P1)
print("A)Proceed with the heist and claim the valuable assets within the vault.")
print("OR")
print("B)Have a change of heart and sabotage the heist, opting to protect the city from further corporate exploitation.")
input("Choose 'A' or 'B' and enter:")

#---Minute 6 PATH 2 ENDINGS:
varMinP2A = "You choose to trust the mysterious figure and follow them into the ventilation shaft, narrowly escaping the clutches of the security patrol. As you emerge onto the rooftops of the city, the mysterious figure reveals themselves to be a rogue hacker with valuable information about the heist. Together, you form an unlikely alliance to thwart the heist and bring the perpetrators to justice."
varMinP2B = "You decide to refuse the offer and surrender to the security patrol, hoping to negotiate your way out of trouble. Unfortunately, your attempts at negotiation fall on deaf ears, and you find yourself detained in a holding cell awaiting interrogation. The fate of the heist and the city's future now hang in the balance as time ticks away."