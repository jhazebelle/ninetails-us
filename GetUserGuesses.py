num_guesses = int(input())
user_guesses = []

for x in range(num_guesses):
    guess = int(input())
    user_guesses.append(guess)

print('user_guesses:', user_guesses)
