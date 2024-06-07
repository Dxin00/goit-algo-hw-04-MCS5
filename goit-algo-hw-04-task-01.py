import random
import timeit
import matplotlib.pyplot as plt
from tabulate import tabulate

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

def test_merge_sort(data):
    return timeit.timeit(lambda: merge_sort(data.copy()), number=1)

def test_insertion_sort(data):
    return timeit.timeit(lambda: insertion_sort(data.copy()), number=1)

def test_timsort(data):
    return timeit.timeit(lambda: sorted(data.copy()), number=1)

def print_results_table(sizes, merge_results, insertion_results, timsort_results):
    headers = ["Розмір набору даних", "Сортування злиттям", "Сортування вставками", "Timsort"]
    data = list(zip(sizes, merge_results, insertion_results, timsort_results))
    print(tabulate(data, headers=headers, tablefmt="grid"))

def run_tests(sizes):
    merge_results = []
    insertion_results = []
    timsort_results = []

    for size in sizes:
        data = generate_data(size)
        merge_time = test_merge_sort(data)
        insertion_time = test_insertion_sort(data)
        timsort_time = test_timsort(data)

        merge_results.append(merge_time)
        insertion_results.append(insertion_time)
        timsort_results.append(timsort_time)

    print_results_table(sizes, merge_results, insertion_results, timsort_results)

    plt.plot(sizes, merge_results, label='Сортування злиттям')
    plt.plot(sizes, insertion_results, label='Сортування вставками')
    plt.plot(sizes, timsort_results, label='Timsort')
    plt.xlabel('Розмір набору даних')
    plt.ylabel('Час виконання (сек)')
    plt.title('Порівняння алгоритмів сортування')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    run_tests(sizes)
