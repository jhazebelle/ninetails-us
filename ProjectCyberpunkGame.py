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
# output: This is different 
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
print("Neon Streets: The Cybernetic Conspiracy")
input("Press 'Enter' to begin:")


#-----Minute 1 INTRO:-----
# You find yourself standing on a rain-soaked street corner in the heart of the neon-lit city, Hypernet City. To your left, a shady alleyway beckons with the promise of intrigue. To your right, a sleek hovercar speeds by, its occupants casting curious glances your way. Do you:
#---Choices:
# Investigate the shady alleyway. --original path1--
# Hail a passing hovercab and follow it to its destination. --bad ending--option for part 2 hidden

print("You find yourself standing on a rain-soaked street corner in the heart of the neon-lit city. To your left, a shady alleyway beckons with the promise of intrigue. To your right, a sleek hovercar speeds by, its occupants casting curious glances your way. Do you:")
print("A)Investigate the shady alleyway.")
print("OR")
print("B)Hail a passing hovercab and follow it to its destination.")
choice = input("Choose 'A' or 'B' and enter:")

varMin2P1 = "You choose to investigate the shady alleyway and stumble upon a group of cybernetically enhanced street thugs conducting a clandestine deal. They don't seem to have noticed you yet. Do you:"
varMin2P2 = "You choose to hail a passing hovercab and follow it to its destination, hoping it will lead you to valuable information about the heist. The hovercab takes you deep into the heart of the city's bustling metropolis, finally coming to a stop outside a high-rise corporate building adorned with security cameras and armed guards. \n You choose to attempt to hack into the building's security systems from a remote location, believing it to be a safer and more discreet approach. However, as you delve into the corporate network, you unwittingly trigger an alarm that alerts the building's security team to your presence. Before you can react, security drones swarm your location, tracing your digital footprints back to your hideout. \n You opt to try to quickly cover your tracks and evade capture, but the security drones are relentless in their pursuit. Despite your best efforts to outmaneuver them, you're eventually cornered in a narrow alleyway with no means of escape. With nowhere left to run, you find yourself surrounded by armed security forces, their weapons trained on you. You choose to make a last-ditch attempt to fight your way out, but you're quickly overwhelmed by the sheer force of the security team's firepower. In the end, you're left battered and defeated, your dreams of uncovering the truth about the heist shattered. As you're dragged away in handcuffs, you realize that your quest for justice has come to a premature and tragic end."

if choice=="A":
     print(varMin2P1)#Continue to Path 1
else:
     print(varMin2P2)#bad ending
     input("GAME OVER:")
    






#-----Minute 2 PATH 1:-----
varMin2P1 = "You choose to investigate the shady alleyway and stumble upon a group of cybernetically enhanced street thugs conducting a clandestine deal. They don't seem to have noticed you yet. Do you:"
# original path1 - You choose to investigate the shady alleyway and stumble upon a group of cybernetically enhanced street thugs conducting a clandestine deal. They don't seem to have noticed you yet. Do you:
#---Choices:
# Sneak past the thugs to eavesdrop on their conversation.--original path1--
# Confront the thugs and demand to know what they're up to.--path1 bad ending 1--
print("A)Sneak past the thugs to eavesdrop on their conversation.")
print("OR")
print("B)Confront the thugs and demand to know what they're up to.")
choice = input("Choose 'A' or 'B' and enter:")

varMin3P1 = "You manage to sneak past the thugs and overhear snippets of conversation about a high-profile corporate heist planned for tonight. Before you can learn more, one of the thugs spots you and pulls out a weapon. Do you:"
varMin2P4 = "You confront the thugs and demand to know what they're up to. You wake up hours later in a dimly lit alleyway, bruised and broken, with no memory of how you got there. The heist goes ahead as planned, and the city falls victim to chaos and corruption as the stolen assets are used to further the agendas of powerful individuals and corporations. Your failure to intervene allows the cybernetic conspiracy to unfold unchecked, plunging the neon-lit streets into an era of darkness and despair."
if choice=="A":
     print(varMin3P1)# Continue to Minute 3 Path 1
else:
     print(varMin2P4)# Bad ending 1
     input("GAME OVER:")








#---Minute 2 PATH 2: HIDE PATH 2 For now, script cannot branch out, it must run in order of the code.
# varMin2P2 = "You choose to hail a passing hovercab and follow it to its destination, hoping it will lead you to valuable information about the heist. The hovercab takes you deep into the heart of the city's bustling metropolis, finally coming to a stop outside a high-rise corporate building adorned with security cameras and armed guards. Do you:"
# branch path2 - You choose to hail a passing hovercab and follow it to its destination, hoping it will lead you to valuable information about the heist. The hovercab takes you deep into the heart of the city's bustling metropolis, finally coming to a stop outside a high-rise corporate building adorned with security cameras and armed guards. Do you:
#---Choices:
# Infiltrate the corporate building disguised as a maintenance worker to gather intel.--branch path2--
# Attempt to hack into the building's security systems from a remote location.--path2 bad end--
# print("A)Infiltrate the corporate building disguised as a maintenance worker to gather intel.")
# print("OR")
# print("B)Attempt to hack into the building's security systems from a remote location.")
# choice = input("Choose 'A' or 'B' and enter:")

# varMin3P2 = "You opt to infiltrate the corporate building disguised as a maintenance worker, blending in seamlessly with the bustling crowd of employees. As you navigate the labyrinthine corridors, you overhear snippets of conversation about the impending heist. However, your cover is at risk of being blown by an approaching security patrol. Do you:"
# varMin2P3 = "You choose to attempt to hack into the building's security systems from a remote location, believing it to be a safer and more discreet approach. However, as you delve into the corporate network, you unwittingly trigger an alarm that alerts the building's security team to your presence. Before you can react, security drones swarm your location, tracing your digital footprints back to your hideout. You opt to try to quickly cover your tracks and evade capture, but the security drones are relentless in their pursuit. Despite your best efforts to outmaneuver them, you're eventually cornered in a narrow alleyway with no means of escape. With nowhere left to run, you find yourself surrounded by armed security forces, their weapons trained on you. You choose to make a last-ditch attempt to fight your way out, but you're quickly overwhelmed by the sheer force of the security team's firepower. In the end, you're left battered and defeated, your dreams of uncovering the truth about the heist shattered. As you're dragged away in handcuffs, you realize that your quest for justice has come to a premature and tragic end."

# if choice=="A":
#     print(varMin3P2)#Continue to Path 2
# else:
#     print(varMin2P3)#Path 3 Bad End, variable is located above choice if statement
#     input("GAME OVER:")















#-----Minute 3 PATH 1:-----
varMin3P1 = "You manage to sneak past the thugs and overhear snippets of conversation about a high-profile corporate heist planned for tonight. Before you can learn more, one of the thugs spots you and pulls out a weapon. Do you:"
# original path1 - You manage to sneak past the thugs and overhear snippets of conversation about a high-profile corporate heist planned for tonight. Before you can learn more, one of the thugs spots you and pulls out a weapon. Do you:
#---Choices:
# Attempt to talk your way out of the situation. --path1 bad end--
# Draw your own weapon and prepare for a fight.--original path1--
print("A)Attempt to talk your way out of the situation.")
print("OR")
print("B)Draw your own weapon and prepare for a fight.")
choice = input("Choose 'A' or 'B' and enter:")

varMin3P1End = "You choose to attempt to talk your way out of the situation, hoping to defuse the tension and avoid violence. You raise your hands in a gesture of surrender and start to speak calmly, trying to reason with the thug. However, before you can finish your sentence, the thug opens fire, their weapon spraying bullets in your direction.\n Your attempt at negotiation fails miserably as the bullets find their mark, leaving you wounded and helpless on the rain-soaked pavement. As consciousness fades, you realize that sometimes words are not enough to quell the violence of the cybernetic underworld. Your quest to uncover the truth about the heist ends abruptly, buried beneath the relentless onslaught of gunfire."
varMin4P1 = "You choose to draw your weapon, and a fierce firefight erupts in the alleyway. After a tense exchange of gunfire, you emerge victorious but wounded. As you catch your breath, you notice a mysterious figure watching you from the shadows. Do you:"

if choice=="A":
     print(varMin3P1End)# Bad ending 1
     input("GAME OVER:")
else:
     print(varMin4P1) #Continue to Minute 4 Path 1








#---Minute 3 PATH 2: HIDE PATH 2 For now, script cannot branch out, it must run in order of the code.
# varMin3P2 = "You opt to infiltrate the corporate building disguised as a maintenance worker, blending in seamlessly with the bustling crowd of employees. As you navigate the labyrinthine corridors, you overhear snippets of conversation about the impending heist. However, your cover is at risk of being blown by an approaching security patrol. Do you:"
# branch path2 - You opt to infiltrate the corporate building disguised as a maintenance worker, blending in seamlessly with the bustling crowd of employees. As you navigate the labyrinthine corridors, you overhear snippets of conversation about the impending heist. However, your cover is at risk of being blown by an approaching security patrol. Do you:
#---Choices:
# Attempt to talk your way out of the situation. --path2 bad end--
# Draw your own weapon and prepare for a fight.--branch path2--
# print("A)Attempt to talk your way out of the situation.")
# print("OR")
# print("B)Draw your own weapon and prepare for a fight.")
# input("Choose 'A' or 'B' and enter:")








#-----Minute 4 PATH 1:-----
varMin4P1 = "You choose to draw your weapon, and a fierce firefight erupts in the alleyway. After a tense exchange of gunfire, you emerge victorious but wounded. As you catch your breath, you notice a mysterious figure watching you from the shadows. Do you:"
# original path1 - You choose to draw your weapon, and a fierce firefight erupts in the alleyway. After a tense exchange of gunfire, you emerge victorious but wounded. As you catch your breath, you notice a mysterious figure watching you from the shadows. Do you:
#---Choices:
# Approach the mysterious figure and demand answers.--original path1--
# Ignore the figure and tend to your wounds before they worsen.--path1 bad end--
print("A)Approach the mysterious figure and demand answers.")
print("OR")
print("B)Ignore the figure and tend to your wounds before they worsen.")
choice = input("Choose 'A' or 'B' and enter:")

varMin5P1 = "You cautiously approach the mysterious figure, who reveals themselves to be a rogue hacker with valuable information about the corporate heist. They offer to help you infiltrate the corporate headquarters where the heist is planned to take place. Do you:"
varMin4P1End = "You choose to ignore the mysterious figure and prioritize tending to your wounds before they worsen. With adrenaline still coursing through your veins, you hastily patch up your injuries as best as you can, ignoring the nagging feeling of unease at the presence of the mysterious figure. \n As you focus on your wounds, you fail to notice the approach of additional assailants lurking in the shadows. Suddenly, you're ambushed by a second wave of attackers, catching you off guard and overwhelming you with their numbers. \n Despite putting up a valiant fight, you're ultimately outnumbered and outmatched. Your quest to uncover the truth about the heist comes to a bitter end as you succumb to your injuries, alone and defeated in the dark alleyway. The mysterious figure watches silently from the shadows, their intentions forever remaining a mystery as your consciousness fades into oblivion."

if choice=="A":
     print(varMin5P1) # Continue to Minute 5 Path 1
else:
     print(varMin4P1End) # Bad ending 1
     input("GAME OVER:")





#---Minute 4 PATH 2: HIDE PATH 2 For now, script cannot branch out, it must run in order of the code.
# varMin4P2 = "You choose to confront the security patrol and attempt to bluff your way past them. However, they seem suspicious of your presence and demand to see your identification. Do you:"
# branch path 2 - You choose to confront the security patrol and attempt to bluff your way past them. However, they seem suspicious of your presence and demand to see your identification. Do you:
#---Choices:
# Try to bribe the security patrol with credits or valuable information. --path2 bad end--
# Make a run for it and try to lose them in the maze-like corridors of the corporate building.--branch path2--








#-----Minute 5 PATH 1:-----
varMin5P1 = "You cautiously approach the mysterious figure, who reveals themselves to be a rogue hacker with valuable information about the corporate heist. They offer to help you infiltrate the corporate headquarters where the heist is planned to take place. Do you:"
# original path1 - You cautiously approach the mysterious figure, who reveals themselves to be a rogue hacker with valuable information about the corporate heist. They offer to help you infiltrate the corporate headquarters where the heist is planned to take place. Do you:
#---Choices:
#Accept the hacker's offer and team up to pull off the heist.--original path1--
#Decline the hacker's offer and attempt to thwart the heist on your own terms. --bad end--
print(varMin5P1)
print("A)Accept the hacker's offer and team up to pull off the heist.")
print("OR")
print("B)Decline the hacker's offer and attempt to thwart the heist on your own terms.")
choice = input("Choose 'A' or 'B' and enter:")

varMin5P1End = "You cautiously approach the mysterious figure, but ultimately decide to decline the hacker's offer. You thank them for their offer but explain that you prefer to operate alone. The hacker nods understandingly and disappears into the shadows, leaving you to pursue your own path.\n Without the hacker's assistance, you find yourself ill-prepared to thwart the heist on your own terms. As you attempt to infiltrate the corporate headquarters, you quickly realize that you underestimated the security measures in place. Caught off guard by a sophisticated alarm system, you trigger an alert that alerts the authorities to your presence. \n Cornered by security forces, you're left with no choice but to surrender. As you're handcuffed and escorted away, you reflect on the missed opportunity to team up with the hacker and the consequences of your decision to go it alone. Your quest to stop the heist ends in failure, overshadowed by the harsh reality of the cybernetic underworld."
varMin6P1 = "You accept the hacker's offer and together, you orchestrate a daring infiltration of the corporate headquarters. Using their hacking skills and your combat expertise, you navigate through security systems and guards to reach the heart of the facility. As you stand before the vault containing the coveted prize, you realize that your choices will determine the fate of the city. Do you:"

if choice=="A":
     print(varMin6P1) # Continue to Minute 6 Path 1
else:
     print(varMin5P1End) # Bad ending 1
     input("GAME OVER")









#---Minute 5 PATH 2: HIDE PATH 2 For now, script cannot branch out, it must run in order of the code.
# varMinP2 = "You opt to make a run for it, darting through the corridors of the corporate building with the security patrol hot on your heels. As you reach a dead-end, you realize you're trapped with nowhere left to run. Suddenly, a mysterious figure emerges from the shadows and offers you a way out through a hidden ventilation shaft. Do you:"
# branch path 2 - You opt to make a run for it, darting through the corridors of the corporate building with the security patrol hot on your heels. As you reach a dead-end, you realize you're trapped with nowhere left to run. Suddenly, a mysterious figure emerges from the shadows and offers you a way out through a hidden ventilation shaft. Do you:
#---Choices:
# Trust the mysterious figure and follow them into the ventilation shaft.--branch path2--
# Refuse the offer and surrender to the security patrol, hoping to negotiate your way out of trouble.--path2 bad end--
# print("A)Trust the mysterious figure and follow them into the ventilation shaft.")
# print("OR")
# print("B)Refuse the offer and surrender to the security patrol, hoping to negotiate your way out of trouble.")
# input("Choose 'A' or 'B' and enter:")








#-----Minute 6 PATH 1:-----
varMin6P1 = "You accept the hacker's offer and together, you orchestrate a daring infiltration of the corporate headquarters. Using their hacking skills and your combat expertise, you navigate through security systems and guards to reach the heart of the facility. As you stand before the vault containing the coveted prize, you realize that your choices will determine the fate of the city. Do you:"
# original path1 - You accept the hacker's offer and together, you orchestrate a daring infiltration of the corporate headquarters. Using their hacking skills and your combat expertise, you navigate through security systems and guards to reach the heart of the facility. As you stand before the vault containing the coveted prize, you realize that your choices will determine the fate of the city. Do you:
#---Choices:
#Proceed with the heist and claim the valuable assets within the vault.--original path1--
#Have a change of heart and sabotage the heist, opting to protect the city from further corporate exploitation.--original path1.1--
print("A)Proceed with the heist and claim the valuable assets within the vault.")
print("B)Have a change of heart and sabotage the heist, opting to protect the city from further corporate exploitation.")
print("OR")
print("C)Betray the hacker and claim all the assets within the vault.")
choice = input("Choose 'A' or 'B' and enter:")

varMin6P1GoodEnding1 = "With adrenaline coursing through your veins, you make the bold decision to proceed with the heist and claim the valuable assets within the vault. As you crack the intricate security measures and lay your hands on the coveted prize, a sense of triumph washes over you. However, in the midst of your victory, a realization dawns upon you - the power within the vault could be used to reshape the city for the better, rather than falling into the wrong hands. \n You make a vow to use the assets not for personal gain, but to fund initiatives that uplift the marginalized and empower the downtrodden. With the hacker by your side, you become a force for positive change in the cybernetic underworld, fighting against corporate exploitation and bringing hope to the city's inhabitants. Your daring heist becomes the catalyst for a brighter future, and your legacy as a champion of justice and equality endures for generations to come."
varMin6P1GoodEnding2 = "In a moment of clarity, you realize the magnitude of the decision before you and choose to have a change of heart. With unwavering resolve, you sabotage the heist, opting to protect the city from further corporate exploitation. As alarms blare and security forces descend upon the facility, you and the hacker make a swift escape into the shadows. \n Despite the risks, you know that you've made the right choice. With the hacker's help, you disseminate the information about the corporate plot, exposing the truth to the public and rallying the citizens to demand accountability from those in power. Your selfless act of defiance sparks a revolution, leading to sweeping reforms that dismantle the corrupt system and pave the way for a new era of transparency and justice in the city. \n In the end, your courage and sacrifice become the catalyst for positive change, ensuring a brighter future for all who call the neon-lit streets their home."
varMin6P1BadEnding1 = "In a moment of greed and temptation, you succumb to the allure of riches and power, opting to stun the hacker with your powerful stungun and claim the valuable assets within the vault. As you crack open the vault and lay your hands on the coveted prize, a rush of exhilaration floods your senses. \n However, your triumph is short-lived as the alarms blare, and security forces swarm the facility. Caught in the act, you and the hacker are cornered by heavily armed guards, their weapons trained on you. With no means of escape, you realize too late the consequences of your actions. \n As you're apprehended and led away in handcuffs, you come to terms with the reality of your betrayal. Your once noble quest ends in disgrace and imprisonment, a cautionary tale of the corrupting influence of greed and ambition in the neon-lit streets of the city."
if choice =="A":
     print(varMin6P1GoodEnding1)
     print("Ending 1 of 3")
elif choice =="B":
     print(varMin6P1GoodEnding2)
     print("Ending 2 of 3")
else:
     print(varMin6P1BadEnding1)
     print("Ending 3 of 3")
     input("GAME OVER:")

print("\n The End. Thanks for playing!")







#---Minute 6 PATH 2 ENDINGS: HIDE PATH 2 For now, script cannot branch out, it must run in order of the code.
# varMinP2A = "You choose to trust the mysterious figure and follow them into the ventilation shaft, narrowly escaping the clutches of the security patrol. As you emerge onto the rooftops of the city, the mysterious figure reveals themselves to be a rogue hacker with valuable information about the heist. Together, you form an unlikely alliance to thwart the heist and bring the perpetrators to justice."
# varMinP2B = "You decide to refuse the offer and surrender to the security patrol, hoping to negotiate your way out of trouble. Unfortunately, your attempts at negotiation fall on deaf ears, and you find yourself detained in a holding cell awaiting interrogation. The fate of the heist and the city's future now hang in the balance as time ticks away."