def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        print(tortoise, hare, minutes)
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

# when the number of minute at which they meet first is not an integer, the program will continue to run, which is erroneous.
# 如果后来两者在某整数分钟时相遇则答案错误 否则无限运行