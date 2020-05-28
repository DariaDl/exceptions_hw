documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
             {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def command_p(documents):
    number = input('Введите номер документа: ')
    res = 0
    for document in documents:
        if number == document['number']:
            print(f"Владельца данного документа зовут {document['name']}")
            res = 1
    if res == 0:
        print('Такого документа нет')


def command_l(documents):
    print('Список всех документов: ')
    for document in documents:
        res = document['type'] + " \"" + document['number'] + "\" " + "\"" + document['name'] + "\""
        print(res)


def command_s(directories):
    number = input('Введите номер документа: ')
    res = 0
    for key in directories:
        if number in directories[key]:
            print('Данный документ находится на полкe #', key)
            res = 1
    if res == 0:
        print('Такого документа нет')


def command_a(documents, directories):
    type_document = input('Введите тип документа: ')
    number = input('Введите номер: ')
    name_p = input('Введите имя: ')
    shelf_number = input('Введите номер полки: ')
    new_document = {"type": type_document, "number": number, "name": name_p}
    documents.append(new_document)
    if shelf_number not in directories:
        directories[shelf_number] = list([number])
    else:
        directories[shelf_number] = directories[shelf_number] + list([number])
    print(directories)
    print(documents)

def command_n(documents):
    try:
        print('Список всех владельцев документов:')
        for document in documents:
            res = document['name']
            print(res)
    except KeyError:
        print('Не у всех документов есть поле "name" ')


while True:
    command = input('Введите команду: ')
    if command == 'p':
        command_p(documents)
    elif command == 'l':
        command_l(documents)
    elif command == 's':
        command_s(directories)
    elif command == 'a':
        command_a(documents, directories)
    elif command == 'n':
        command_n(documents)
    elif command == 'exit':
        break
main()

