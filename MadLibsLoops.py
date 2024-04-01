input_string1 = input()
input_string2 = input()

string1 = ''
integer1 = ''
for char in input_string1:
    if char.isdigit():
        integer1 += char
    else:
        string1 += char

string2 = ''
integer2 = ''
for char in input_string2:
    if char.isdigit():
        integer2 += char
    else:
        string2 += char

print(f"Eating {integer1} {string1}a day keeps the doctor away.")

if input_string1 == 'quit 0' or input_string2 == 'quit 0':
    exit() 
    
print(f"Eating {integer2} {string2}a day keeps the doctor away.")

    
while True:
    input_string = input()
    if input_string == 'quit 0':
        exit()
    else:
        print(f"Eating {integer1} {string1}a day keeps the doctor away.")

