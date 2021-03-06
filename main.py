from prettytable import PrettyTable


class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def isAdult(self):
        if self.age >= 21:
            return True
        return False


def main():
    answer = 'y'
    people = []
    table = PrettyTable()
    table.field_names = ['Name', 'Surname', 'Age', 'Gender', 'Old to Work']

    while answer.lower() == 'y' or answer.lower() == 'yes':
        try:
            name = input('Name: ')
            surname = input('Surname: ')
            age = int(input('Age: '))
            gender = input('Gender: ')

            people.append(Person(name, surname, age, gender))
            answer = input('Continue? (Y/N): ')
        except Exception as e:
            print(e)

    for person in people:
        table.add_row(
            [person.name.title(), person.surname.title(), person.age, person.gender.title(), person.isAdult()])
    print(table)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
