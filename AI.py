# 2023 0331 發包

# CharGPT AI
# ChatGPT-3 AI (CodeX 特徵比對工具)
# Bing    AI
# Curs    AI
# GitHub  Copilos AI
# GitHub  Copilos AI

#============================================================
# 2023 0331 CharGPT AI :   程式名稱:cls_ai() /  功能:MAC /Windows 清除畫面
import os
def cls_ai():
    os.system('cls' if os.name == 'nt' else 'clear') 
    #使用 Python 的 os 模組，其中包含了一個名為 system 的函式。函式的作用是執行作業系統的命令
#===============================================================================
# 2023 0331 CharGPT AI :   程式名稱:Greeting_ai() / 功能:say_hello
class Greeting_ai:
    @classmethod  # 使用类方法装饰器标记该方法为类方法
    def say_hello(cls):  # cls 表示类本身，可以用于调用类的其他方法或属性
        name = input("What's your name? ")  # 从命令行读取用户输入的名称
        print(f"Hello, {name}!")  # 输出问候语

Greeting_ai.say_hello()  # 直接调用 Greeting 类的类方法 say_hello() 来执行问候语的输出
#=================================================================================
