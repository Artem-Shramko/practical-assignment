                                              #Task 11.1
import time
n = 500_000
target = 499_999

numbers_list = list(range(n))
numbers_set = set(numbers_list)

start = time.perf_counter()
result_list = target in numbers_list
list_time = time.perf_counter() - start

start = time.perf_counter()
result_set = target in numbers_set
set_time = time.perf_counter() - start

print("Task 11.1:")
print(f"List search: {list_time:.9f} сек")
print(f"Set search: {set_time:.9f} сек")

assert result_list is True
assert result_set is True

                                           #Task 11.2
def intersection_slow(array1, array2):
    result = []

    for element in array1:
        if element in array2 and element not in result:
            result.append(element)

    return result


def intersection_fast(array1, array2):
    set2 = set(array2)
    result = []

    for element in array1:
        if element in set2 and element not in result:
            result.append(element)

    return result


array1 = [1, 2, 3, 4, 5, 6]
array2 = [4, 5, 6, 7, 8, 9]

print("\nTask 11.2:")

start = time.perf_counter()
result_slow = intersection_slow(array1, array2)
slow_time = time.perf_counter() - start

start = time.perf_counter()
result_fast = intersection_fast(array1, array2)
fast_time = time.perf_counter() - start

print("Перетин масивів:", result_slow)
print(f"O(N * M): {slow_time:.9f} сек")
print(f"O(N + M): {fast_time:.9f} сек")

assert result_slow == [4, 5, 6]
assert result_fast == [4, 5, 6]
assert result_slow == result_fast

print("\nУсі автотести пройшли успішно!")
