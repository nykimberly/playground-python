# monkey with a typewriter

import random


def monkeyAuthor():
    # Create alphabets
    alphalower = "abcdefghijklmnopqrstuvwxyz "
    alphaupper = alphalower.upper()
    alphabet = alphalower + alphaupper
    alpharange = len(alphalower)

    # Grab user input and verify string contains correct characters
    goal = input("Please type goal string here ")
    for char in goal:
        assert char in alphabet, "Input should be of \
        'abcdefghijklmnopqrstuvwxyz ' characters."

    # Convert goal string to mutal goal list
    goal_list = list(goal)

    # Initialize output array and count metric
    output = []
    count = 0

    for n, goal_char in enumerate(goal_list):
        # Seed each char with first guess
        index = random.randrange(alpharange)
        output.append(alphabet[index])
        count += 1
        # Adjust guess
        while(output[n] != goal_char):
            index = random.randrange(alpharange)
            if goal_char == goal_char.upper():
                output[n] = alphaupper[index]
            else:
                output[n] = alphalower[index]
            count += 1

    # Convert list back into string
    output = "".join(output)

    # Print and return results
    print("it took %d tries but here we are! %r" % (count, output))
    return output

monkeyAuthor();