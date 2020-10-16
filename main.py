from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

NUM_ROLL = 1000

def main():
    die1 = Die()
    die2 = Die()
    results = []
    roll_dice(die1, die2, results)
    #print(results)

    max_value = die1.num_sides + die2.num_sides
    frequencies = analyze_freq(max_value, results)
    #print(frequencies)

    # visualize results using histogram
    x_values = list(range(2, max_value+1))  # make list [2... 13]
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}  # label tick mark
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Result of rolling one 6-side die 1000 times',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')


# analyze and return freq of numbers from rolls
def analyze_freq(max, results) :
    frequencies = []

    for num in range(2, max+1) :
        count = results.count(num)
        frequencies.append(count)
    return frequencies

# roll dice and return list of results of the roll
def roll_dice(die1, die2, results) :
    for num in range(NUM_ROLL) :
        result = die1.roll() + die2.roll()
        results.append(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
