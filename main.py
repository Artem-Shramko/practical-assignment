                                          #Task 6.1
text = "Hello World113"

for char in text:
    if 'A' <= char <= 'Z':
        print(char, "- велика літера")
    elif 'a' <= char <= 'z':
        print(char, "- маленька літера")
    elif '0' <= char <= '9':
        print(char, "- цифра")
    else:
        print(char, "- пробіл")

                                        #Task 6.2
text = "Artem"

print("Введений рядок:", text)

left = 0
right = len(text)-1

is_palindrome = True

while left < right:
    a = text[left]
    b = text[right]

    if 'A' <= a <= 'Z':
        a = chr(ord(a) + 32)

    if 'A' <= b <= 'Z':
        b = chr(ord(b) + 32)

    if a != b:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
 print("Рядок вважається паліндромом")
else:
 print("Рядок не вважається паліндромом")