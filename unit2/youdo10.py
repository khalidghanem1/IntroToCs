import random
rounds = int(input("enter num of roudns: "))

for i in range(rounds):
    nums = [str(random.randint(1, rounds)) for _ in range(rounds)]
    print(f"round {i+1}: " + ", ".join(nums))
