import random
number = random.randint(-10000, 10000)

if number > 1:
    nums = str(number)
    last_num = nums[-1]
    last_num = int(last_num)
else:
    nums = str(number)
    last_num = nums[-1]
    last_num = int(last_num)
    last_num = -abs(last_num)
    
if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is zero")
elif last_num < 6 and last_num != 0:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")