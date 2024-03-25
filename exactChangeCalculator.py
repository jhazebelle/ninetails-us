total_change = int(input( ))

dollar_value = 100
quarter_value = 25
dime_value = 10
nickel_value = 5
penny_value = 1

if total_change <= 0:
    print("No change")
else:
    dollars = total_change // dollar_value
    total_change %= dollar_value

    quarters = total_change // quarter_value
    total_change %= quarter_value

    dimes = total_change // dime_value
    total_change %= dime_value

    nickels = total_change // nickel_value
    total_change %= nickel_value

    pennies = total_change // penny_value

    if dollars > 0:
        print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
    if quarters > 0:
        print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
    if dimes > 0:
        print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
    if nickels > 0:
        print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
    if pennies > 0:
        print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")
