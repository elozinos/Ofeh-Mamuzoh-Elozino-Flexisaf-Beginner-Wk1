while True:
    operation = int(input("""
    What do you want to do 

    1 to see your to do list
    2 to add to your todo list
    3 delete from your to do list """))

    if operation == 1:
        with open("file_handling.txt", "r") as file:
            content = file.read()
            print(content)
    elif operation == 2:
        string = input("what do you want to add")
        with open("file_handling.txt", "a") as file:
            file.write(string + "\n")
        with open("file_handling.txt", "r") as file:
            updated_content = file.read()

            print(updated_content)
    end=int(input("dp you wish to stop 1 yes, 2 no "))
    if end==1:
        break
    elif end==2:
        continue




