score=int(input("What is your score? "))

if score>=70 and score<=100:
    grade = "A"
    print(grade)

elif score>=60 and score<70:
    grade="B"
    print(grade)
elif score>=50 and score<60:
    grade="C"
    print(grade)
elif score>=40 and score<50:
    grade="D"
    print(grade)
elif score>=20 and score<40:
    grade="F"
    print(grade)
else:
    print( f"how can you have {score}")