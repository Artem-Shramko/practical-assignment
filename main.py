                                   #Task 9.1
def get_mean_score(scores):
    if not scores:
        return 0.0
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def get_max_score(scores):
    if not scores:
        return None
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def process_test_results(scores):
    mean_val = get_mean_score(scores)
    max_val = get_max_score(scores)
    return mean_val, max_val

test_scores = [75,88, 92, 60, 95, 81]
mean_result, max_result = process_test_results(test_scores)

print(f"Опрацьовані бали: {test_scores}")
print(f"Середній результат: {mean_result:.2f}")
print(f"Максимальний бал: {max_result}")
                                 #Task 9.2
def validate_currency_input(amount, rate):
    if not isinstance(amount, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("Сума та курс мають бути числами")
    if amount < 0:
        raise ValueError("Сума для конвертації не може бути від'ємною")
    if rate <= 0:
        raise ValueError("Курс валюти має бути більшим за нуль")

def convert_currency(amount, rate):
    validate_currency_input(amount, rate)
    converted_amount = amount * rate
    return converted_amount

initial_amount = 250.50
exchange_rate = 41.25

result_sum = convert_currency(initial_amount, exchange_rate)

print("Модуль конвертації валют")
print(f"Початкова сума у валюті відправлення: {initial_amount:.2f}")
print(f"Актуальний курс обміну: {exchange_rate}")
print(f"Результат конвертації: {result_sum:.2f} гривень")