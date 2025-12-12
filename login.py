credentials = [                       # A list of tuples
    ("kate@gmail.com", "12345kkate"),
    ("pree@outlook.com", "12345pree")
]

attempts = 3

for attempt in range(attempts):                #the user only has 3 attempts 
    user_name = input("User name(email):")
    password_ = input("Password:")

    if (user_name, password_) in credentials:  #compare the user inputs with the tuples stored in the list
        print("Logged in")
        break
    else:
        print("Incorrect user name/password")

else:
    print("Maximum attempts reached. Acount locked.")


    