from zmogus import Zmogus



def average(numbers):
    return sum(numbers) / len(numbers)



def create_person():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")
    return Zmogus(name, surname, age)