def exact_change(user_total):
    num_dollars = user_total // 100  # number of dollars
    user_total %= 100  # exclude dollars
    num_quarters = user_total // 25  # number of quarters
    user_total %= 25  # exclude quarters
    num_dimes = user_total // 10  # number of dimes
    user_total %= 10  # exclude dimes
    num_nickels = user_total // 5  # number of nickels
    num_pennies = user_total % 5  # number of pennies
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__': 
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print('no change')
    else:
        if num_dollars > 0:
            print(num_dollars, 'dollar' if num_dollars == 1 else 'dollars')
        if num_quarters > 0:
            print(num_quarters, 'quarter' if num_quarters == 1 else 'quarters')
        if num_dimes > 0:
            print(num_dimes, 'dime' if num_dimes == 1 else 'dimes')
        if num_nickels > 0:
            print(num_nickels, 'nickel' if num_nickels == 1 else 'nickels')
        if num_pennies > 0:
            print(num_pennies, 'penny' if num_pennies == 1 else 'pennies')
