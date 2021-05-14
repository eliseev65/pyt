number = 23
running = True

while running:
    guess = int(input('Enter number : '))

    if guess == number:
        print("Year")
        running = False
    elif guess < number:
        print('less')
    else:
        print('more')
else:
    print('END')

print('ending...')
