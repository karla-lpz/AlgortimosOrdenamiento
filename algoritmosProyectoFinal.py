import math
import random
import time

dash_div = ("-" * 67)
dash_divb = ("-" * 93)


selection_sort_iterations = 0
selection_sort_swaps = 0
selection_sort_comparisons = 0
selection_sort_time = time.time()


def selection_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    if debug:
        print("             " + str(array_copy))

    n = len(array_copy)
    global selection_sort_iterations
    selection_sort_iterations = 0
    global selection_sort_swaps
    selection_sort_swaps = 0
    global selection_sort_comparisons
    selection_sort_comparisons = 0
    initial_time = time.time()
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            is_smaller = array_copy[j] < array_copy[smallest]
            selection_sort_comparisons += 1
            if is_smaller:
                smallest = j
            selection_sort_iterations += 1
            if debug:
                print("Iteration " + str(selection_sort_iterations) + ": " + str(array_copy))

        if not smallest == i:
            array_copy[i], array_copy[smallest] = array_copy[smallest], array_copy[i]
            selection_sort_swaps += 1
    final_time = time.time()
    global selection_sort_time
    selection_sort_time = final_time - initial_time
    if debug:
        analize_selection_sort(n, selection_sort_comparisons, selection_sort_swaps, selection_sort_time)
    return array_copy


def analize_selection_sort(n, comparisons, shifts, exec_time):
    o_notation = n ** 2
    complexity = int((n - 1) * n / 2)

    comparisons_o = "n^2 = " + str(o_notation)
    swap_o = "n = " + str(n)
    comparisons_c = "((n-1)n)/2 = " + str(complexity)
    shifts_c = "n = [0," + str(complexity) + "]"
    comparisons_r = str(comparisons)
    shifts_r = str(shifts)
    analize_algorithm(comparisons_o, swap_o, comparisons_c, shifts_c, comparisons_r, shifts_r, exec_time)


insertion_sort_iterations = 0
insertion_sort_swaps = 0
insertion_sort_comparisons = 0
insertion_sort_time = time.time()


def insertion_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    if debug:
        print("             " + str(array_copy))

    n = len(array_copy)
    global insertion_sort_iterations
    insertion_sort_iterations = 0
    global insertion_sort_swaps
    insertion_sort_swaps = 0
    global insertion_sort_comparisons
    insertion_sort_comparisons = 0
    initial_time = time.time()

    for i in range(1, n):
        for j in reversed(range(1, i + 1)):
            insertion_sort_iterations += 1
            is_bigger = array_copy[j - 1] > array_copy[j]
            insertion_sort_comparisons += 1
            if is_bigger:
                array_copy[j], array_copy[j - 1] = array_copy[j - 1], array_copy[j]
                insertion_sort_swaps += 1
            if debug:
                print("Iteration " + str(insertion_sort_iterations) + ": " + str(array_copy))

    global insertion_sort_time
    insertion_sort_time = time.time() - initial_time
    if debug:
        analize_insertion_sort(n, insertion_sort_comparisons, insertion_sort_swaps, insertion_sort_time)
    return array_copy


def analize_insertion_sort(n, comparisons, swaps, exec_time):
    o_notation = n ** 2
    complexity = int((n - 1) * n / 2)

    comparisons_o = "n^2 = " + str(o_notation)
    swap_o = "n^2 = " + str(o_notation)
    comparisons_c = "((n-1)n)/2 = " + str(complexity)
    shifts_c = "((n-1)n)/2 = [0," + str(complexity) + "]"
    comparisons_r = str(comparisons)
    shifts_r = str(swaps)
    analize_algorithm(comparisons_o, swap_o, comparisons_c, shifts_c, comparisons_r, shifts_r, exec_time)


bubble_sort_iterations = 0
bubble_sort_swaps = 0
bubble_sort_comparisons = 0
bubble_sort_time = time.time()


def bubble_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    if debug:
        print("             " + str(array_copy))

    n = len(array_copy)
    global bubble_sort_iterations
    bubble_sort_iterations = 0
    global bubble_sort_swaps
    bubble_sort_swaps = 0
    global bubble_sort_comparisons
    bubble_sort_comparisons = 0
    initial_time = time.time()
    for i in range(n - 1):
        for j in range(n - 1 - i):
            is_bigger = array_copy[j + 1] < array_copy[j]
            bubble_sort_comparisons += 1
            if is_bigger:
                array_copy[j], array_copy[j + 1] = array_copy[j + 1], array_copy[j]
                bubble_sort_swaps += 1
            bubble_sort_iterations += 1
            if debug:
                print("Iteration " + str(bubble_sort_iterations) + ": " + str(array_copy))
    global bubble_sort_time
    bubble_sort_time = time.time() - initial_time
    if debug:
        analize_bubble_sort(n, bubble_sort_comparisons, bubble_sort_swaps, bubble_sort_time)
    return array_copy


def analize_bubble_sort(n, comparisons, swaps, exec_time):
    o_notation = n ** 2
    complexity = int((n - 1) * n / 2)

    comparisons_o = "n^2 = " + str(o_notation)
    swap_o = "n^2 = " + str(o_notation)
    comparisons_c = "((n-1)n)/2 = " + str(complexity)
    shifts_c = "((n-1)n)/2 = [0," + str(complexity) + "]"
    comparisons_r = str(comparisons)
    shifts_r = str(swaps)
    analize_algorithm(comparisons_o, swap_o, comparisons_c, shifts_c, comparisons_r, shifts_r, exec_time)


merge_sort_iterations = 0
merge_sort_swaps = 0
merge_sort_comparisons = 0
merge_sort_time = time.time()


def init_merge_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    if debug:
        print("             " + str(array_copy))

    n = len(array_copy)
    global merge_sort_iterations
    merge_sort_iterations = 0
    global merge_sort_comparisons
    merge_sort_comparisons = 0
    global merge_sort_swaps
    merge_sort_swaps = 0
    initial_time = time.time()
    merge_sort(array_copy, debug)
    global merge_sort_time
    merge_sort_time = time.time() - initial_time
    if debug:
        analize_merge_sort(n, merge_sort_comparisons, merge_sort_swaps, merge_sort_time)
    return array_copy


def merge_sort(unsorted_array, debug):
    global merge_sort_iterations
    merge_sort_iterations += 1
    if debug:
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

    if debug:
        print("Divide:\t" + str(unsorted_array) + " -> " + str(left) + " " + str(right))
    left = merge_sort(left, debug)
    right = merge_sort(right, debug)

    return merge(left, right, debug)


def merge(left, right, debug):
    result = []
    if debug:
        message = "Merge: " + str(left) + " " + str(right) + " -> "

    while len(left) > 0 and len(right) > 0:
        is_smaller = left[0] <= right[0]
        global merge_sort_comparisons
        merge_sort_comparisons += 1
        if is_smaller:
            result.append(left.pop(0))
        else:
            global merge_sort_swaps
            merge_sort_swaps += 1
            result.append(right.pop(0))

    while len(left) > 0:
        result.append(left.pop())
    while len(right) > 0:
        result.append(right.pop())

    if debug:
        print(message + str(result))
    return result


def analize_merge_sort(n, comparisons, swaps, exec_time):
    o_notation = round(n * math.log2(n), 2)
    complexity = round(n * math.log2(n), 2)

    comparisons_o = "nlog(n) = " + str(o_notation)
    swap_o = "nlog(n) = " + str(o_notation)
    comparisons_c = "nlog(n) = " + str(complexity)
    shifts_c = "nlog(n) = [0," + str(complexity) + "]"
    comparisons_r = str(comparisons)
    shifts_r = str(swaps)
    analize_algorithm(comparisons_o, swap_o, comparisons_c, shifts_c, comparisons_r, shifts_r, exec_time)


quick_sort_iterations = 0
quick_sort_swaps = 0
quick_sort_comparisons = 0
quick_sort_time = time.time()


def init_quick_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    if debug:
        print("             " + str(array_copy))

    n = len(array_copy)
    global quick_sort_iterations
    quick_sort_iterations = 0
    global quick_sort_comparisons
    quick_sort_comparisons = 0
    global quick_sort_swaps
    quick_sort_swaps = 0
    initial_time = time.time()
    quick_sort(array_copy, 0, n - 1, debug)
    global quick_sort_time
    quick_sort_time = time.time() - initial_time
    if debug:
        analize_quick_sort(n, quick_sort_comparisons, quick_sort_swaps, quick_sort_time)
    return array_copy


def quick_sort(unsorted_array, lo, hi, debug):
    global quick_sort_iterations
    quick_sort_iterations += 1
    if debug:
        print("Iteration " + str(quick_sort_iterations) + ": " + str(unsorted_array))
    if lo < hi:
        p = partition(unsorted_array, lo, hi)
        quick_sort(unsorted_array, lo, p - 1, debug)
        quick_sort(unsorted_array, p + 1, hi, debug)


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


def analize_quick_sort(n, comparisons, swaps, exec_time):
    o_notation = round(n * math.log2(n), 2)
    complexity = round(n * math.log2(n), 2)

    comparisons_o = "nlog(n) = " + str(o_notation)
    swap_o = "nlog(n) = " + str(o_notation)
    comparisons_c = "nlog(n) = " + str(complexity)
    shifts_c = "nlog(n) = [0," + str(complexity) + "]"
    comparisons_r = str(comparisons)
    shifts_r = str(swaps)
    analize_algorithm(comparisons_o, swap_o, comparisons_c, shifts_c, comparisons_r, shifts_r, exec_time)


heap_sort_iterations = 0
heap_sort_swaps = 0
heap_sort_comparisons = 0
heap_sort_time = time.time()


def i_parent(i):
    return math.floor((i - 1) / 2)


def i_left_child(i):
    return 2 * i + 1


def i_right_child(i):
    return 2 * i + 2


def init_heap_sort(unsorted_array, debug):
    array_copy = unsorted_array.copy()
    if debug:
        print("             " + str(array_copy))

    n = len(array_copy)
    global heap_sort_iterations
    heap_sort_iterations = 0
    global heap_sort_comparisons
    heap_sort_comparisons = 0
    global heap_sort_swaps
    heap_sort_swaps = 0
    initial_time = time.time()
    heap_sort(array_copy, debug)
    global heap_sort_time
    heap_sort_time = time.time() - initial_time
    if debug:
        analize_heap_sort(n, heap_sort_comparisons, heap_sort_swaps, heap_sort_time)
    return array_copy


def heap_sort(a, debug):
    count = len(a)
    heapify(a, count, debug)

    end = count - 1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        global heap_sort_swaps
        heap_sort_swaps += 1
        if debug:
            print("Iteration " + str(heap_sort_iterations) + ": " + str(a))
        end -= 1
        sift_down(a, 0, end, debug)


def heapify(a, count, debug):
    start = i_parent(count - 1)

    while start >= 0:
        sift_down(a, start, count - 1, debug)
        start -= 1


def sift_down(a, start, end, debug):
    global heap_sort_iterations
    global heap_sort_comparisons
    root = start

    while i_left_child(root) <= end:
        heap_sort_iterations += 1
        child = i_left_child(root)
        swap = root

        if a[swap] < a[child]:
            heap_sort_comparisons += 1
            swap = child
        if child + 1 <= end and a[swap] < a[child + 1]:
            heap_sort_comparisons += 1
            swap = child + 1
        if swap == root:
            return
        else:
            a[root], a[swap] = a[swap], a[root]
            root = swap
            global heap_sort_swaps
            heap_sort_swaps += 1
            if debug:
                print("Iteration " + str(heap_sort_iterations) + ": " + str(a))


def analize_heap_sort(n, comparisons, swaps, exec_time):
    o_notation = round(n * math.log2(n), 2)
    complexity = round(n * math.log2(n), 2)

    comparisons_o = "nlog(n) = " + str(o_notation)
    swap_o = "nlog(n) = " + str(o_notation)
    comparisons_c = "nlog(n) = " + str(complexity)
    shifts_c = "nlog(n) = [0," + str(complexity) + "]"
    comparisons_r = str(comparisons)
    shifts_r = str(swaps)
    analize_algorithm(comparisons_o, swap_o, comparisons_c, shifts_c, comparisons_r, shifts_r, exec_time)

def recolect_bubble_data(comparisions, swaps):
    print("|\tBUBBLESORT\t\t\t|\t" + comparisions + "\t|" + swaps + "\t\t\t|")

def createTable():
    print(dash_divb)
    print(("|\tORDENAMIENTO\t\t|\tCOMPARACIONES\t|\tINTERCABIOS/DESPLAZAMIENTOS\t\t|\tTIEMPO\t"))
    print(dash_divb)
    print("|\tSELECTIONSORT\t\t|\t\t" + str(selection_sort_comparisons) + "\t\t|\t\t\t\t" + str(selection_sort_swaps) + "\t\t\t\t\t|\t" + str(selection_sort_time) + "ms")
    print(dash_divb)
    print("|\tINSERTIONSORT\t\t|\t\t" + str(insertion_sort_comparisons) + "\t\t|\t\t\t\t" + str(insertion_sort_swaps) + "\t\t\t\t|\t" + str(insertion_sort_time) + "ms")
    print(dash_divb)
    print("|\tBUBBLESORT\t\t\t|\t\t" + str(bubble_sort_comparisons) + "\t\t|\t\t\t\t" + str(bubble_sort_swaps) + "\t\t\t\t|\t" + str(bubble_sort_time) + "ms")
    print(dash_divb)
    print("|\tMERGESORT\t\t\t|\t\t" + str(merge_sort_comparisons) + "\t\t\t|\t\t\t\t" + str(merge_sort_swaps) + "\t\t\t\t\t|\t" + str(merge_sort_time) + "ms")
    print(dash_divb)
    print("|\tQUICKSORT\t\t\t|\t\t" + str(quick_sort_comparisons) + "\t\t\t|\t\t\t\t" + str(quick_sort_swaps) + "\t\t\t\t\t|\t" + str(quick_sort_time) + "ms")
    print(dash_divb)
    print("|\tHEAPSORT\t\t\t|\t\t" + str(heap_sort_comparisons) + "\t\t\t|\t\t\t\t" + str(heap_sort_swaps) + "\t\t\t\t\t|\t" + str(heap_sort_time) + "ms")
    print(dash_divb)


def menu():
    print((":" * 7) + " ORDENAMIENTOS " + (":" * 7))
    print("a) Ingresa los datos")
    print("b) Ingresar cantidad de datos")
    option = ""
    while not option == "a" and not option == "b":
        option = input("Elige una opción: ")
    return option


def analize_algorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR, exec_time):
    print(dash_div)
    print("\t\t\t|\tCOMPARACIONES\t\t|\t\tINTERCAMBIOS\t\t|")
    print("Notación O\t|\t\t" + comparisonsO + "\t\t|\t\t\t" + shiftsO + "\t\t\t|")
    print("Complejidad\t|\t" + comparisonsC + "\t|\tde 0 a " + shiftsC)
    print(dash_div)
    print("Realizadas\t|\t\t" + comparisonsR + "\t\t\t\t|\t\t\t" + shiftsR + "\t\t\t|")
    print(dash_div)
    print("Tiempo de ejecución: " + str(exec_time) + "ms")


def userInput():
    dataLength = input("¿Cuántos datos?: ")
    numbers = []

    if int(dataLength) > 0:
        strInput = input("Da los " + dataLength + " datos separados por un espacio: ").split(" ")
        for i in range(int(dataLength)):
            numbers.append(int(strInput[i]))

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

    print((":" * 7) + " HEAPSORT " + (":" * 7))
    init_heap_sort(numbers, True)


def file_creating(random_numbers):
    file = 'numbers.txt'
    with open(file, 'w') as numbers:
        numbers.write("[")
        for i in range(len(random_numbers)):
            numbers.write(str(random_numbers[i]))
            if i != len(random_numbers) - 1:
                numbers.write(",")
        numbers.write("]")


def gen_input():
    numbers = int(input("Ingrese cuantos numeros aleatorios desea obtener: "))
    random_numbers = [random.randint(0, 1000) for _ in range(numbers)]
    file_creating(random_numbers)
    print("Arreglo: " + str(random_numbers))

    selection_sort(random_numbers, False)
    insertion_sort(random_numbers, False)
    bubble_sort(random_numbers, False)
    init_merge_sort(random_numbers, False)
    init_quick_sort(random_numbers, False)
    init_heap_sort(random_numbers, False)

    createTable()


def main():
    option = menu()

    if option == "a":
        userInput()
    elif option == "b":
        gen_input()
    # a = [5,7,2,3,9,1]
    # print(selectionSort(a, False))


main()
