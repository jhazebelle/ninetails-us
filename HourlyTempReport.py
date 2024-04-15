user_input = input()
hourly_temperature = user_input.split()

output_string = ' -> '.join(hourly_temperature)  # Join elements with "->"

# Add a space after the last element
output_string += ' '

print(output_string)
