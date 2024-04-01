num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces


for row in range(1, num_rows + 1):
    for col in range(ord('A'), ord('A') + num_cols):
        print(f"{row}{chr(col)}", end=' ')

print()
