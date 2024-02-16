varMin5 = "You chose A and decided to destroy it for no reason at all"

print("You came across a table. Do you: A) destroy it OR B)rework it and resell it to make a quick buck")

choice = input("Choose A or B and enter:")

if choice == "A":
    print(varMin5)  
else:
    print("You reworked it and met with a stranger online to sell it, but when you met, you ended up being robbed of the table, your phone, and wallet. How unfortunate.")





#choice = "B" and "A"

#match choice:
#     case "A":
#          print(varMin5)
#     case _:
#          print("you reworked it and met with a stranger online to sell it but when you met, you ended up being robbed of the table, your phone, and wallet. how unfortunate.")







# How to Change the Value of an item in an Array - using strings in Arrays do not work! Use lists!
#import array as arr
#choices = arr.array('u',[abc,def])
#choices[0] = testing
#print(choices[0])
#output 50

# Creating a List of strings and accessing
# using index
#List = ["Test", "For", "Test"]
#print("\nList Items: ")
#print(List[0])
#print(List[2])


# How to Change the Value of an item in an Array - numbers
#import array as arr
#choices = arr.array('i',[10,20,30,40])
#choices[0] = 50
#print(choices[0])
#output 50

# How to access items in an Array using Negative Indexing
#import array as arr 
#numbers = arr.array('i',[10,20,30])
#print(numbers[-1]) #gets last item
#print(numbers[-2]) #gets second to last item
#print(numbers[-3]) #gets first item


#How to access individual items in an Array
#import array as arr 
#numbers = arr.array('i',[10,20,30])
#print(numbers[0]) 
#print(numbers[1]) 
#print(numbers[2])



#Find the length of an array
#import array as arr 
#numbers = arr.array('i',[10,20,30])
#print(len(numbers))


#varMin5 = "You chose A and decided to destroy it for no reason at all"

#print("You came across a table. Do you: A) destroy it OR B)rework it and resell it to make a quick buck")
#input("Choose A or B and enter:")

#if "B"=="B":
#    print("you reworked it and met with a stranger online to sell it but when you met, you ended up being robbed of the table, your phone, and wallet. how unfortunate.")
#else:
#    print(varMin5)

#TYPECODE	C TYPE	PYTHON TYPE	SIZE
#'b'	signed char	int	1
#'B'	unsigned char	int	1
#'u'	wchar_t	Unicode character	2
#'h'	signed short	int	2
#'H'	unsigned short	int	2
#'i'	signed int	int	2
#'I'	unsigned int	int	2
#'l'	signed long	int	4
#'L'	unsigned long	int	4
#'q'	signed long long	int	8
#'Q'	unsigned long long	int	8
#'f'	float	float	4
#'d'	double	float	8