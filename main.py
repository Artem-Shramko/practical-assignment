                                     #Task 4.1
READ = 0b0001
WRITE = 0b0010
EXECUTE = 0b0100
ADMIN = 0b1000

user_permissions = READ | WRITE

has_read = (user_permissions & READ) != 0
has_execute = (user_permissions & EXECUTE) != 0

user_permissions = user_permissions | EXECUTE
has_execute_after_add = (user_permissions & EXECUTE) != 0

user_permissions = user_permissions & ~WRITE
has_write_after_remove = (user_permissions & WRITE) != 0

print(f"Початкові права: {bin(READ | WRITE)}")
print(f"Право на читання?: {has_read}")
print(f"Право на виконання?: {has_execute}")
print(f"Право на виконання після додавання?: {has_execute_after_add}")
print(f"Право на запис після видалення?: {has_write_after_remove}")

                                  #Task 4.2
number = 13

is_even = (number & 1) == 0
is_power_of_two = (number > 0) & ((number & (number - 1)) == 0)
lowest_set_bit = number & -number
bit_count = number.bit_count()

print(f"Аналізоване число: {number} ({bin(number)})")
print(f"Число є парним?: {is_even}")
print(f"Число є степенем двійки?: {is_power_of_two}")
print(f"Молодший встановлений біт (значення): {lowest_set_bit} ({bin(lowest_set_bit)})")
print(f"Кількість встановлених бітів: {bit_count}")