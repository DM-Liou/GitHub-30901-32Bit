import random

def guess_number():
    secret_number = random.randint(1, 100)
    while True:
        user_guess = int(input("請猜一個1到100之間的數字："))
        if user_guess == secret_number:
            print("恭喜你！你猜對了！")
            break
        elif user_guess < secret_number:
            print("太小了，請再猜一次。")
        else:
            print("太大了，請再猜一次。")

guess_number()