print("What to Wear Application")

print("This application takes your input on today's weather, then interprets it to give you a recommendation on what to wear today.")
input("Press 'Enter' to start:")


print("It is ____ outside")
choice = input("Fill in the blank:")

match choice:
     case "sunny":
          print("Wear a hat, short sleeves, and shorts")
     case "wet":
          print("Wear a hoodie or raincoat and bring an umbrella")
     case "raining":
          print("Wear a hoodie or raincoat and bring an umbrella")
     case "rainy":
          print("Wear a hoodie or raincoat and bring an umbrella")
     case "windy":
          print("Wear a windbreaker")
     case "snowy":
          print("Dress in your snowjacket, thick pants, boots, gloves, and beanie")
     case _:
          print("Wear your usual outfit")