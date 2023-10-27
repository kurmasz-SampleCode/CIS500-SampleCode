import coin

def count_heads(trials):
    c = coin.Coin()
    num_heads = 0
    for i in range(0, trials):
        c.flip()
        if (c.is_heads()):
            num_heads += 1

    return num_heads

print(f"Num heads out of 1000 trials: {count_heads(1000)}")

def max_streak(trials):
    c = coin.Coin()
    current_streak = 0
    max_streak = 0
    for i in range(0, trials):
        c.flip()
        if (c.is_heads()):
            current_streak += 1
        else:
            max_streak = max(current_streak, max_streak)
            current_streak = 0
    max_streak = max(current_streak, max_streak)
    return max_streak     

print("Max Streak:")
for i in range(0, 1000000, 2500):
    print(f"{i:7d} {max_streak(i)}")