def fizzbuzz(number):
    """
    Fizz buzz is a counting game where each player speaks a number from 1 to n
    in sequence, but with a few exceptions:
    - if the would-be spoken number is divisible by 3 the player must say fizz
    instead
    - if the would-be spoken number is divisible by 5 the player must say buzz
    instead
    - if the would-be spoken number is divisible by 3 and 5 the player must say
    fizzbuzz instead
    """
    number = int(number)
    if number < 1:
        raise ValueError()

    output = []
    for i in range(1, number + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                value = 'fizzbuzz'
            else:
                value = 'fizz'
        elif i % 5 == 0:
            value = 'buzz'
        else:
            value = i
        output.append(value)
    return output
