#imports
import random
from collections import deque
import string
details={
    "name":"",
    "email":"",
    "requests":[]
}
customer_deets=[]
customers_request_id=set() #a set to make sure there is no duplicated customer
request_line=deque()#initialisng a queue to process request
while True:
    type_of_customer = input("are you a new customer or an old customer? answer old or new ?  q for quit")
    if type_of_customer.strip().lower() == "new":
        details = {
            "name": "",
            "email": "",
            "requests": []
        }
        name = input("what is your name")
        email = input("what is your email?")
        details["name"] = name
        details["email"] = email
        request = input("what is your request? ")
        random_letter = random.choice(string.ascii_lowercase)
        random_number = str(random.randint(1, 101))
        request_id = random_letter + random_number

        request_format = {"request": request,
                          "request_id": request_id}
        details["requests"].append(request_format)
        customers_request_id.add(request_id)
        request_line.append(request_format)
        customer_deets.append(details)

    elif type_of_customer.strip().lower() == "old":
        name = input(
            "what is your name? ")  # ask for name and email and search for in already existing dict of customers details
        email = input("what is your email? ")
        new_email = input("is your email correct put it again? ")  # to make sure the email is correct
        request = input("what is your request? ")
        customer_found = False

        for i in customer_deets:
            if (name == i["name"]
                    and email == i["email"]
                    and email == new_email):
                customer_found=True
                random_letter = random.choice(string.ascii_lowercase)
                random_number = str(random.randint(1, 101))
                request_id = random_letter + random_number
                request_format = {"request": request,
                                  "request_id": request_id}
                i["requests"].append(request_format)
                customers_request_id.add(request_id)
                request_line.append(request_format)
        if not customer_found:
            print("Try again, details not found 🛑🛑")
    elif type_of_customer.strip().lower() =="q":
        print("ok bye 👋")
        break
    print(customer_deets)
    print(customers_request_id)
    print(request_line)




#processing the reuest

#llm takes request in order after a request is processed






