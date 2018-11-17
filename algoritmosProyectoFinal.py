from heapq import heappush, heappop
from random import randrange
from time import time
import os

dash_div = ("-" * 67)


def selection_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    print("             " + str(array_copy))

    n = len(array_copy)
    iterations = 0
    swaps = 0
    comparisons = 0

    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            is_smaller = array_copy[j] < array_copy[smallest]
            comparisons += 1
            if is_smaller:
                smallest = j
            iterations += 1
            print("Iteration " + str(iterations) + ": " + str(array_copy))

        if not smallest == i:
            array_copy[i], array_copy[smallest] = array_copy[smallest], array_copy[i]
            swaps += 1

    # print("Comparisons: " + str(comparisons))
    # print("Swaps: " + str(swaps))
    if debug:
        analize_selection_sort(n, comparisons, swaps)
    return array_copy


def analize_selection_sort(n, comparisons, shifts):
    comparisonsO = "n^2 = " + str(n ** 2)
    shiftsO = "n^2 = "
    comparisonsC = "((n-1)n)/2 = " + str((n - 1) * n / 2)
    shiftsC = "((n-1)n)/2 = [0," + str((n - 1) * n / 2) + "]"
    comparisonsR = str(comparisons)
    shiftsR = str(shifts)
    analize_algorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR)


def insertion_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    print("             " + str(array_copy))

    n = len(array_copy)
    iterations = 0
    swaps = 0
    comparisons = 0

    for i in range(n):
        j = i
        while j > 0 and array_copy[j] < array_copy[j - 1]:
            comparisons += 1
            array_copy[j], array_copy[j - 1] = array_copy[j - 1], array_copy[j]
            swaps += 1
            iterations += 1
            print("Iteration " + str(iterations) + ": " + str(array_copy))
            j -= 1

    # print("Comparisons: " + str(comparisons))
    # print("Swaps: " + str(swaps))
    if debug:
        analize_insertion_sort(n, comparisons, swaps)
    return array_copy


def analize_insertion_sort(n, comparisons, swaps):
    comparisonsO = "n^2 = " + str(n ** 2)
    shiftsO = "n^2 = "
    comparisonsC = "((n-1)n)/2 = " + str((n - 1) * n / 2)
    shiftsC = "((n-1)n)/2 = [0," + str((n - 1) * n / 2) + "]"
    comparisonsR = str(comparisons)
    shiftsR = str(swaps)
    analize_algorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR)


def bubble_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    print("             " + str(array_copy))

    n = len(array_copy)
    iterations = 0
    swaps = 0
    comparisons = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            is_bigger = array_copy[j + 1] < array_copy[j]
            comparisons += 1
            if is_bigger:
                array_copy[j], array_copy[j + 1] = array_copy[j + 1], array_copy[j]
                swaps += 1
            iterations += 1
            print("Iteration " + str(iterations) + ": " + str(array_copy))

    # print("Comparisons: " + str(comparisons))
    # print("Swaps: " + str(swaps))
    if debug:
        analize_bubble_sort(n, comparisons, swaps)
    return array_copy


def analize_bubble_sort(n, comparisons, swaps):
    comparisonsO = "n^2 = " + str(n ** 2)
    shiftsO = "n^2 = "
    comparisonsC = "((n-1)n)/2 = " + str((n - 1) * n / 2)
    shiftsC = "((n-1)n)/2 = [0," + str((n - 1) * n / 2) + "]"
    comparisonsR = str(comparisons)
    shiftsR = str(swaps)
    analize_algorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR)


merge_sort_iterations = 0
merge_sort_swaps = 0
merge_sort_comparisons = 0


def init_merge_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    print("             " + str(array_copy))

    n = len(array_copy)
    global merge_sort_iterations
    merge_sort_iterations = 0
    global merge_sort_comparisons
    merge_sort_comparisons = 0
    global merge_sort_swaps
    merge_sort_swaps = 0
    merge_sort(array_copy)
    # print("Comparisons: " + str(merge_sort_comparisons))
    # print("Swaps: " + str(merge_sort_swaps))
    if debug:
        analize_merge_sort(n, merge_sort_comparisons, merge_sort_swaps)
    return array_copy


def merge_sort(unsorted_array):
    global merge_sort_iterations
    merge_sort_iterations += 1
    print("Iteration " + str(merge_sort_iterations) + ": " + str(unsorted_array))

    n = len(unsorted_array)
    if n <= 1:
        return unsorted_array

    left = []
    right = []
    middle = n / 2

    for i in range(n):
        if i < middle:
            left.append(unsorted_array[i])
        else:
            right.append(unsorted_array[i])

    print("Divide:\t" + str(unsorted_array) + " -> " + str(left) + " " + str(right))
    merge_sort(left)
    merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        is_smaller = left[0] < right[0]
        global merge_sort_comparisons
        merge_sort_comparisons += 1
        if is_smaller:
            result.append(left.pop())
        else:
            global merge_sort_swaps
            merge_sort_swaps += 1
            result.append(right.pop())

    while len(left) > 0:
        result.append(left.pop())
    while len(right) > 0:
        result.append(right.pop())

    print("Merge: " + str(result))
    return result


def analize_merge_sort(n, comparisons, swaps):
    comparisonsO = "n^2 = " + str(n ** 2)
    shiftsO = "n^2 = "
    comparisonsC = "((n-1)n)/2 = " + str((n - 1) * n / 2)
    shiftsC = "((n-1)n)/2 = [0," + str((n - 1) * n / 2) + "]"
    comparisonsR = str(comparisons)
    shiftsR = str(swaps)
    analize_algorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR)


quick_sort_iterations = 0
quick_sort_swaps = 0
quick_sort_comparisons = 0


def init_quick_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    print("             " + str(array_copy))

    n = len(array_copy)
    global quick_sort_iterations
    quick_sort_iterations = 0
    global quick_sort_comparisons
    quick_sort_comparisons = 0
    global quick_sort_swaps
    quick_sort_swaps = 0
    quick_sort(array_copy, 0, n - 1)
    # print("Comparisons: " + str(merge_sort_comparisons))
    # print("Swaps: " + str(merge_sort_swaps))
    if debug:
        analize_merge_sort(n, quick_sort_comparisons, quick_sort_swaps)
    return array_copy


def quick_sort(unsorted_array, lo, hi):
    global quick_sort_iterations
    quick_sort_iterations += 1
    print("Iteration " + str(quick_sort_iterations) + ": " + str(unsorted_array))

    if lo < hi:
        p = partition(unsorted_array, lo, hi)
        quick_sort(unsorted_array, lo, p - 1)
        quick_sort(unsorted_array, p + 1, hi)


def partition(array, lo, hi):
    global quick_sort_swaps
    global quick_sort_comparisons

    pivot = array[hi]
    i = (lo - 1)

    for j in range(lo, hi):
        is_smaller = array[j] < pivot
        quick_sort_comparisons += 1
        if is_smaller:
            if not i == j:
                i += 1
                array[i], array[j] = array[j], array[i]
                quick_sort_swaps += 1

    i += 1
    array[i], array[hi] = array[hi], array[i]
    quick_sort_swaps += 1
    return i


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp





def menu():
    print((":" * 7) + " ORDENAMIENTOS " + (":" * 7))
    print("a) Ingresa los datos")
    print("b) Ingresa un rango")
    option = ""
    while not option == "a" and not option == "b":
        option = input("Elige una opción: ")
    return option


def analize_algorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR):
    print(dash_div)
    print("\t\t\t|\tCOMPARACIONES\t\t|\t\tINTERCAMBIOS")
    print("Notación O\t|\t\t" + comparisonsO + "\t\t\t|\t\t\t" + shiftsO)
    print("Complejidad\t|\t" + comparisonsC + "\t|\tde 0 a " + shiftsC)
    print(dash_div)
    print("Realizadas\t|\t\t" + comparisonsR + "\t\t\t\t|\t\t\t" + shiftsR)


def userInput():
    dataLength = input("¿Cuántos datos?: ")
    numbers = []

    if int(dataLength) > 0:
        strInput = input("Da los " + dataLength + " datos separados por un espacio: ").split(" ")
        for i in range(int(dataLength)):
            numbers.append(int(strInput[i]))

    # print((":" * 7) + " HEAPSORT " + (":" * 7))
    # print("             " + str(numbers))
    # heapSort(numbers)

    print((":" * 7) + " SELECTIONSORT " + (":" * 7))
    selection_sort(numbers, True)

    print((":" * 7) + " INSERTIONSORT " + (":" * 7))
    insertion_sort(numbers, True)

    print((":" * 7) + " BUBBLESORT " + (":" * 7))
    bubble_sort(numbers, True)

    print((":" * 7) + " MERGESORT " + (":" * 7))
    init_merge_sort(numbers, True)

    print((":" * 7) + " QUICKSORT " + (":" * 7))
    init_quick_sort(numbers, True)


def genInput():
    rango = input("Introduce el rango: ")
    print("|" + (" " * 3) + "Ordenamiento" + (" " * 3) + "|" + (" " * 3) + "Comparaciones" + (" " * 3) + "|" + (" " * 3) + "Intercambios/desplazamientos" + (" " * 3) +
          "|" + (" " * 3) + ("Tiempo") + (" " * 3) + "|")


def main():
    os.system('cls')

    option = menu()

    if option == "a":
        userInput()
    elif option == "b":
        genInput()
    # a = [5,7,2,3,9,1]
    # print(selectionSort(a, False))
main()


