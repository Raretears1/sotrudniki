import pickle
import random


# utilities

def input_integer(text, error):
    num = input(text)
    while not num.isnumeric():
        print(error)
        num = input(text)

    return int(num)


def find_employee_by_name(personal, age):
    for elem in personal:
        if elem["name"] == age:
            return elem
        return None


# start


def f_add(personal):
    print("Function ADD")

    name = input("Enter name: ")
    age = input_integer("Enter age: ", "age must be numeric")

    new_employee = {"name": name,
                    "age": age
                    }

    personal.append(new_employee)

    return personal


def f_del(personal):
    print("Function DELETE")

    name = input("Enter name: ")

    elem = find_employee_by_name(personal, name)
    if elem:
        personal.remove(elem)
    else:
        print("Nothing found")
    return personal


def f_redact(personal):
    print("Function REDACT")
    name = input("Enetr name: ")
    employee = find_employee_by_name(personal, name)

    new_name = input("Enter new name: ")
    new_age = input_integer("Enter new age: ", "Age must be == numeric")

    employee["name"] = new_name
    employee["age"] = new_age
    return personal


def f_show(personal):
    print("Function SHOW")
    print()
    for elem in personal:
        print(f'{elem["name"]},{elem["age"]}')
        print()
    return


def binar_search(personal, elem, key):
    print(sort_by(personal, key=key))

    start = 0
    end = len(personal) - 1
    count = 0
    while start <= end:
        count += 1
        midle = (end + start) // 2

        if key(personal[midle]) > elem:
            end = midle - 1
        elif key(personal[midle]) < elem:
            start = midle + 1
        elif key(personal[midle]) == elem:
            return midle
    print(f'iter = {count}')
    return -1


def sort_by(personal, key):
    for i in range(len(personal)):
        min_idx = i
        for j in range(i, len(personal)):
            if key(personal[j]) < key(personal[min_idx]):
                min_idx = j
        personal[i], personal[min_idx] = personal[min_idx], personal[i]
    return personal


def random_add(personal):
    rand_employee = ["Sasha", "Illya", "Lebron"]
    add = input("Enter how employee add ")
    add = int(add)

    new_employee = {"name": random.choice(rand_employee),
                    "age": random.randint(18, 45)
                    }
    personal.append(new_employee)

    return personal


def main():
    personal = [
        {"name": "Vlad Shevchuk",
         "age": 19,
         }, {"name": "Vlad Shevchuk",
             "age": 18,
             }
    ]
    print(personal)

    while True:
        x = input("Choose your action: \n1 - Add\n 2 - Delete \n 3 - redaction \n"
                  " 4 - Show \n 5 - BINAR SEARCH \n 6 - Save info\n 7 - SORT \n 8 - Random add "
                  "\n 0 - Exit  \n ENTER: ")

        if x == "1":
            personal = f_add(personal)
        if x == "2":
            personal = f_del(personal)
        if x == "3":
            personal = f_redact(personal)
        if x == "4":
            f_show(personal)
        if x == "5":
            print("Index - ", binar_search(personal, 19, key=lambda x: x["age"]))
        if x == "6":
            with open('personal.pickle', 'wb') as save_p:
                pickle.dump(personal, save_p)
        if x == "7":
            print(sort_by(personal, key=lambda x: x["age"]))
        if x == "8":
            personal = random_add(personal)

        if x == "0":
            print("By")
            with open('personal.pickle', 'wb') as save_p:
                pickle.dump(personal, save_p)
            break
        else:
            print("TRY AGAIN: ")


main()
