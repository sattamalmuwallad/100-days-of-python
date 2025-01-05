import random 

rand_num = random.randint(1,10)
print(rand_num)

rand_num_0_1 = random.random()
print(rand_num_0_1)

ans = random.random() * 5
print(ans)

random_float = random.uniform(0,10)
print(random_float)


print("Welcome to Head or Tails")


random_head_tails = random.randint(0,1)
if random_head_tails == 0:
    print("You win")
else:
    print("You lose")