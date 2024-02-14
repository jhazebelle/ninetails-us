first5 = input("Enter your first 5 syllable line:")
second7 = input("Enter your second 7 syllable line:")
third5 = input("Enter your third 5 syllable line:")
print(first5,"\n")
print(second7,"\n")
print(third5)

# In this project, I created a haiku template which you can use to input your poem
# line by line. At first, I had trouble finding a way to separate the lines because
# when the input is printed, it shows the inputs in one line. After a couple
# trial and error, I discovered that \n can be used as a line break but it must be
# contained in a string for it to work. 
# 
# 
# For future versions, I'd like to create a filter for the input which will detect
# whether or not the input has met the syllable limit. It may sound easy for now,
# but I suspect that I'd have to define vowels, create numerous if statements, set
# conditions for tricky words like "speed, little, female," and etc.