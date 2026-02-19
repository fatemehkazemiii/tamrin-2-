grades=[18,15,12,10]
grade=int(input("enter your grade:"))
match grade:
    case 18:
        print("excellent")
    case 15:
        print("good")
    case 12:
        print("acceptable")
    case 10:
        print("weak")
    case _:
        print("invalid grade")