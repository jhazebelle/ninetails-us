user_input = input()
short_names = user_input.split()

del short_names[0]

short_names[2] = 'Joe'

print(short_names)
