logged_in_user = None

def login_req(func):
    def wrapper():
        if logged_in_user:
            return func()
        else:
            print("Access denied. Please log in.")
    return wrapper

def login(username):
    global logged_in_user
    logged_in_user = username
    print(f"{username} logged in.")
    
@login_req
def dashboard():
    print(f"Welcome to your dashboard, {logged_in_user}!")

dashboard()
login("rishi")
dashboard()  