def moving_average(values, window):
    averages = []
    for i in range(len(values) - window):
        subset = values[i:i + window]
        averages.append(sum(subset) / window)
    return averages


print(moving_average([10, 20, 30, 40], 2))
