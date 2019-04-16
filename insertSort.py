import numpy as np
import matplotlib.pyplot as plt


def get_random_table(length_of_table, max_number):
    random_table = np.random.randint(1, max_number, length_of_table)
    return random_table


def insert_sort(table):
    table_file = open("table_file.txt", "w")
    print("nieposortowana ", table, file=table_file, end='\n\n')
    comparisons  = 0
    for i in range(0, len(table)):
        comparisons = comparisons + 1
        tmp = table[i]
        while i > 0 and tmp < table[i-1]:
            comparisons  = comparisons + 1
            table[i] = table[i-1]
            print("PIERWSZA", table, file=table_file)
            i = i - 1
        table[i] = tmp
        if tmp < table[i-1]:
            print("DRUGA   ", table, file=table_file)
    print("posortowana ", table, file=table_file, end='\n\n')
    print('liczba porównań: ', comparisons, file=table_file)
    table_file.close()
    return table, comparisons


def get_data_for_histogram(number_of_data_sets):
    table_of_comparisons = []
    for i in range(0, number_of_data_sets):
        sorted_table, comparisons = insert_sort(get_random_table(100, 10))
        table_of_comparisons.append(comparisons)
    return table_of_comparisons

def plot_histogram(table):
    plt.hist(table, edgecolor='black', bins=20)
    plt.title('Histogram liczby porównań')
    plt.ylabel('Liczba wystąpień danej liczby porównań')
    plt.xlabel('Liczba porównań')
    plt.grid(linestyle='--')
    plt.show()

def plot_number_of_comparison_in_function_of_table_length():
    table_of_comparisons = []
    xaxis = []
    for i in range(100, 1100, 100):
        table, comparisons = insert_sort(get_random_table(i, 10))
        table_of_comparisons.append(comparisons)
        xaxis.append(i)
    plt.plot(xaxis, table_of_comparisons)
    plt.title('Wykres zależności liczby porównań w funkcji długości tablicy')
    plt.ylabel('liczba porównań')
    plt.xlabel('długość tablicy')
    plt.grid(linestyle='--')
    plt.show()


def main():
    plot_histogram(get_data_for_histogram(500))
    #plot_number_of_comparison_in_function_of_table_length()
    #insert_sort(get_random_table(14,20))

main()
