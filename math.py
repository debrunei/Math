from random import randint
outer_count = 0
while outer_count < 5:
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    product = num_1 * num_2
    print(f"Question {outer_count + 1}: What is {num_1} x {num_2}")
    inner_count = 0
    while inner_count < 5:
        guess = input("What's your answer")
        guess = int(guess)
        if guess == product:
            print("Correct")
            break
        else:
            print("Incorrect. Try again.")
            inner_count += 1
    outer_count += 1