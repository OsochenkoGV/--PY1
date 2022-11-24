import random
def get_unique_list_numbers() -> list[int]:
        numbers = set()
        while len(numbers) < 10:
            numbers.add(random.randint(-10, 10))
        return list(numbers)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
