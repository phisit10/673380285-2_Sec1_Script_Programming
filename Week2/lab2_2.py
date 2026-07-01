
num = int(input("Enter your age: "))

if 0 <= num < 5 : 
    print("You're too young for movies! Enjoy cartoons.")
elif 5 <= num <= 12:
    print("G-rated or PG-rate movies.")
elif 13 <= num <= 17:
    print("PG-13 or R-rated(with parential guidance).")
elif num >= 18:
    print("PG-13 or R-rated(with parential guidance).")

    question = str(input("do you like action movies? (yes/no) : "))

    if question == "yes":
            print("You might enjoy the latest action blockbuster")
    elif question == "no":
            print("Oh, Okey")
elif num < 0 :
    print("you cant have neative age")
else:
    print("invalid age")

