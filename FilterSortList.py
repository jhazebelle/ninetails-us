user_input = input()
numbers = list(map(int, user_input.split()))

non_negative_numbers = [num for num in numbers if num >= 0]
non_negative_numbers.sort()

for num in non_negative_numbers:
    print(num, end=' ')
