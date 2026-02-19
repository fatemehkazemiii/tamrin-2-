fruits = ["apple", "banana", "orange"]
fruit_name= input("enter your fruit:")
match fruit_name:
    case "apple" | "banana" | "orange":
        print("this fruit is in the list")
    case _:
        print("this fruit is not in the list")
