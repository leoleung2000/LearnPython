#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－编程题
# Programed List 5-Test Programme
# 第五章　编程题　５．１～５．５５

import random
import time

'''
# 5.1 （统计正数和负数的个数然后计算这些数的平均值）
positive_Number = 0
negative_Number = 0
average = 0
total = 0
number = eval(input("Enter an integer, the input ends if it is 0: "))
while number != 0:
    if number > 0:
        positive_Number += 1
    else:
        negative_Number += 1
    total = total + number
    number = eval(input("Enter an integer, the input ends if it is 0: "))
average = total / (positive_Number + negative_Number)
print("Positive Number: ", positive_Number)
print("Negative Number: ", negative_Number)
print("Total: ", total)
print("Average: ", average)

# 5.2 （累加）
correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 5 # Constant

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS:
    # 1. Generate two random single-digit integers
    number1 = random.randint(1, 16)
    number2 = random.randint(1, 16)

    # 2. Prompt the student to answer "what is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " + " +
        str(number2) + "? "))

    # 5. Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong.\n", number1, "+",
            number2, "should be", (number1 + number2))

    # Increase the count
    count += 1

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of",
    NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
'''
# 5.3 （公斤转换成磅）

# 5.4 （英里转换成公里）

# 5.5 （公斤转换成磅，磅转换成公斤）

# 5.6 （将英里转换成公里，公里转换成英里）

# 5.7 （使用三角函数）

# 5.8 （使用函数）

# 5.9 （财务应用程序：计算未来学费）

# 5.10 （找出最高分）

# 5.11 （找出两个最高分）

# 5.12 （找出可被５和６同时整除的数）

# 5.13 （找出可被５或６整除但又不能被它俩同时整除的数）

# 5.14 （找出最小的ｎ满足ｎ的平方大于１２０００）

# 5.15 （找出最大的ｎ满足ｎ的立方小于１２０００）

# 5.16 （计算最大公约数）

# 5.17 （显示ＡＳＣＩＩ字符表）

# 5.18 （找出一个整数的所有因子）

# 5.19 （显示一个金字塔）

# 5.20 （使用循环显示四种模式）

# 5.21 （在金字塔模式中显示数字）

# 5.22 （显示在２和１０００之间的素数）

# 5.23 （财务应用程序：比较不同利率的贷款）

# 5.24 （财务应用程序：贷款摊销时间表）

# 5.25 （演示消除错误）

# 5.26 （数列求和）

# 5.27 （计算Ｐｉ）

# 5.28 （计算ｅ）

# 5.29 （显示闰年）

# 5.30 （显示每个月的第一天）

# 5.31 （显示日历）

# 5.32 （财务应用程序：复合值）

# 5.33 （财务应用程序：计算ＣＤ值）

# 5.34 （游戏：彩票）

# 5.35 （完全数）

# 5.36 （游戏：石头、剪刀、布）

# 5.37 （求和）

# 5.38 （模拟：时钟倒计时）

# 5.39 （财务应用程序：找出销售额）

# 5.40 （模拟：硬币正反面）

# 5.41 （最大数字的出现）

# 5.42 （蒙特卡罗模拟）

# 5.43 （数学问题：组合）

# 5.44 （十进制到二进制）

# 5.45 （十进制到十六进制）

# 5.46 （统计方面：计算均值和标准方差）

# 5.47 （：绘制随机球）

# 5.48 （：绘制圆）

# 5.49 （：显示乘法口诀表）

# 5.50 （：显示三角形图案的数字）

# 5.51 （：显示一个格子）

# 5.52 （：绘制ｓｉｎ函数）

# 5.53 （：绘制ｓｉｎ函数和ｃｏｓ函数）

# 5.54 （：绘制平方函数）

# 5.55 （：棋盘）
