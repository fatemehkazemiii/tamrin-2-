day=input("enter a day of a week:")
match day:
    case"saturday":
        print("today is saturday")
    case"sunday":
        print("today is sunday")
    case"monday":
        print("today is monday")
    case"tuesday":
        print("today is tuesday")
    case"wednesday":
        print("today is wednesday")
    case"thursday":
        print("today is thursday")
    case"friday":
        print("today is friday")
    case _:
        print("please enter correct day")

