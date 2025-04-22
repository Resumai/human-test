from zmogus import Zmogus
from os import system, name

def clear():
    system('cls' if name == 'nt' else 'clear')

def average(numbers):
    return sum(numbers) / len(numbers)



def create_person():
    print("--- Enter person's data---")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    try:
        age = int(input("Enter age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
    
    return Zmogus(name, surname, age)



def main():
    while True:
        person = create_person()
        print(person)
        if input("Do you want to add another person? (y/n): ") != "y":
            break


main()