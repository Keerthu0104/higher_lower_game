import random
from art import logo,vs
from game_data import data

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description}, {account_country}"

def isCoorect(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess =="a"
    else:
        return user_guess=="b"


score = 0
account_b = random.choice(data)
flag = False
print(logo)
while not flag:
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)

        print(f"compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        user = input("Who has more followers A or B : ").lower()
        print("\n" * 50)
        print(logo)

        count_a = account_a["follower_count"]
        count_b = account_b["follower_count"]

        result = isCoorect(user, count_a, count_b)
        if result:
            score+=1
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry, that's Wrong. Final Score : {score}")
            flag=True

