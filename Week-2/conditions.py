
age = 16
gender = "female"

if (age < 18 ):
    print("You are still young ")
else:
    print("You should get an ID")

    #compound /multiple conditions

    if((age > 30) & (gender == "female")):
        print("You qualify for a loan")
    else:
        print("No loan for you")

        fav_color = "grey"
        age = 22
    if (fav_color == 'grey') | (age <= 20):
        print("Happy birthday to you")
    else:
        print("No birthday present for you")

