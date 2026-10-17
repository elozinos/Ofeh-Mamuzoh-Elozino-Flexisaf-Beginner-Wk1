#this is a number guessing game

hidden_number=3

while True:
    number=int(input("Guess that number i can't say "))
    if number==hidden_number:
        print("you got it 🎉🎉🎉🎉")
        break

    else:
        print("try again")
        continue