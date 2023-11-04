import coin
import math
import matplotlib.pyplot as plt

def count_heads(trials):
    c = coin.Coin()
    num_heads = 0
    for i in range(0, trials):
        c.flip()
        if (c.is_heads()):
            num_heads += 1

    return num_heads

# print(f"Num heads out of 1000 trials: {count_heads(1000)}")

def plot_num_heads(trials, points):
    num_heads = [count_heads(trials) for p in range(0, points)]
    
    fig, ax = plt.subplots()
    ax.hist(num_heads, bins=100)
    plt.show()

plot_num_heads(500000,  1000)


def max_streak(flips):
    c = coin.Coin()
    current_streak = 0
    max_streak = 0
    for i in range(0, flips):
        c.flip()
        if (c.is_heads()):
            current_streak += 1
        else:
            max_streak = max(current_streak, max_streak)
            current_streak = 0
    max_streak = max(current_streak, max_streak)
    return max_streak     

def average_max_streak(flips, trials):
    total = 0
    for i in range(0, trials):
        total += max_streak(flips)
    return total / trials

def plot_max_streak(start, stop, step, trials):
    y = []
    x = []
    for i in range(start, stop, step):
        avg = average_max_streak(i, trials)
        print(f"{i:6d} {avg}")
        x.append(i)
        y.append(avg)

    print(x)
    print(y)
    plt.plot(x, y)
    plt.plot(x, [math.log(i)/math.log(2) for i in x]) 
    plt.show()  

# plot_max_streak(50000, 1000000, 50000, 15)
#plot_max_streak(500, 10000, 500, 10)