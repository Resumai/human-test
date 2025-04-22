from zmogus import Zmogus
from os import system, name






def clear():
    system('cls' if name == 'nt' else 'clear')

clear()


def average(people : list[Zmogus]):
    sum_of_ages = sum(person.age for person in people)
    return sum_of_ages / len(people)

def create_person():
    print("--- Enter person's data---")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        
    return Zmogus(name, surname, age)

def show_people(people: list[Zmogus]):
    print("\n--- People List ---")
    print(f"{'No.':<4} {'Name':<15} {'Surname':<15} {'Age':<5}")
    print("-" * 45)

    for i, person in enumerate(people, start=1):
        print(f"{i:<4} {person.name:<15} {person.surname:<15} {person.age:<5}")

    print("-" * 45)
    print(f"Average age: {average(people):.1f} years\n")


def main():
    people = []
    while True:
        clear()
        person = create_person()
        people.append(person)
        clear()
        show_people(people)
        if input("Do you want to add another person? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()