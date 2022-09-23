secret_number = 9
guess_count = 0
while guess_count < 3:
    guess = int(input("What's the secret number? "))
    guess_count += 1
    if guess == secret_number:
        print("Congrats! The secret number is 9!")
        break
    elif guess_count <= 2:
        print(f"Oops, keep going~ ({3-guess_count} chance(s) left)")
else:
    print("You failed")