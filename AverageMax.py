user_input = input()
numbers = list(map(int, user_input.split()))

average = int(sum(numbers) / len(numbers))
maximum = max(numbers)

print(f'{average} {maximum}')
