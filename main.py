from zmogus import Zmogus
from os import system, name



# Added 
def clear():
    system('cls' if name == 'nt' else 'clear')

clear()


def average(people : list[Zmogus]):
    sum_of_ages = 0

    for person in people:
        sum_of_ages += person.age
    return sum_of_ages / len(people)


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
    people = []
    while True:
        clear()
        person = create_person()
        people.append(person)
        print(f"Average age: {average(people)}")
        if input("Do you want to add another person? (y/n): ") != "y":
            break

main()