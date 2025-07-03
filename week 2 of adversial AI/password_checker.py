attempt = 3
correct_username = "ali"
correct_password = "1234"

while attempt > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Access granted ")
        break
    else:
        attempt -= 1
        print(f"Invalid credentials. {attempt} attempts remaining ❌")

        if attempt == 0:
            print("Access blocked ")