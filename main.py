from zmogus import Zmogus



def average(numbers):
    return sum(numbers) / len(numbers)



def create_person():
    while True:
        try:
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return Zmogus(name, surname, age)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    