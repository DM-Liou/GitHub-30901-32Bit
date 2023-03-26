import random

print("1.歡迎來到猜大小遊戲！")
print("2.請輸入一個1到100之間的整數，猜猜看電腦出的數字是多少？")

number = random.randint(1, 100)
guess = int(input("3.請輸入你的猜測："))

while guess != number:
    if guess > number:
        print("4.你猜的數字太大了！")
    else:
        print("5.你猜的數字太小了！")
    guess = int(input("6.請重新輸入你的猜測："))

print("7.恭喜你猜對了！答案就是", number)