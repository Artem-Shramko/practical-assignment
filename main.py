                                   #Task 10.1
def fast_power(base, exponent):
    if exponent == 0:
        return 1

    if exponent < 0:
        return 1 / fast_power(base, -exponent)

    half = fast_power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half

    return base * half * half


assert fast_power(2, 10) == 1024
assert fast_power(3, 3) == 27
assert fast_power(5, 0) == 1
assert fast_power(2, -2) == 0.25

                                 #Task 10.2
def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)

    return result


assert generate_parentheses(1) == ["()"]
assert generate_parentheses(2) == ["(())", "()()"]
assert len(generate_parentheses(3)) == 5


print("Task 10.1:")
print("2^10 =", fast_power(2, 10))
print("3^3 =", fast_power(3, 3))
print("5^0 =", fast_power(5, 0))

print("\nTask 10.2:")
print("n = 2:", generate_parentheses(2))
print("n = 3:", generate_parentheses(3))

print("\nУсі автотести пройшли успішно!")