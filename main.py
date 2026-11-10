                              #Task 7.1
size = 17

for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f"{i * j:4}", end="")
    print()
                             #Task 7.2
n = 17

if n <= 0:
    result = 0
elif n == 1:
    result = 1
else:
    a, b = 0, 1
    count = 2
    while count <= n:
        a, b = b, a + b
        count += 1
    result = b

print(f"{n} число Фібоначчі: {result}")