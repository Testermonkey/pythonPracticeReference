
def login():
    retry=0
    try:
        username = input("Enter Username")
        password = input("Enter Password")
    except Exception as e:
        print(e, type(e))

    if username == "hal" and password == "xyz":
        print(f"welcome {username}")
    else:
        print(f"Failed")
        if retry <= 3:
            login()
        else:
            print("close session")

login()