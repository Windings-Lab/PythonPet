from protobuf.out.addressbook_pb2 import AddressBook
from protobuf.out.addressbook_pb2 import Person


def write(path: str, person: Person):
    address_book = AddressBook()
    try:
        with open(path, 'rb') as f:
            address_book.ParseFromString(f.read())
    except IOError:
        print(f"{path}: Could not open file. Creating a new one.")

    address_book.people.append(person)

    with open(path, 'wb') as f:
        f.write(address_book.SerializeToString())


def write_with_prompt(path: str):
    address_book = AddressBook()
    try:
        with open(path, 'rb') as f:
            address_book.ParseFromString(f.read())
    except IOError:
        print(f"{path}: Could not open file. Creating a new one.")

    prompt_for_address(address_book.people.add())

    with open(path, 'wb') as f:
        f.write(address_book.SerializeToString())


def read(path: str):
    address_book = AddressBook()
    with open(path, 'rb') as f:
        address_book.ParseFromString(f.read())

    list_people(address_book)


def list_people(address_book: AddressBook):
    for person in address_book.people:
        print("Person ID:", person.id)
        print("  Name:", person.name)
        if person.email != "":
            print("  E-mail address:", person.email)

        for phone_number in person.phones:
            if phone_number.type == Person.PhoneType.PHONE_TYPE_MOBILE:
                print("  Mobile phone #: ", end="")
            elif phone_number.type == Person.PhoneType.PHONE_TYPE_HOME:
                print("  Home phone #: ", end="")
            elif phone_number.type == Person.PhoneType.PHONE_TYPE_WORK:
                print("  Work phone #: ", end="")
            print(phone_number.number)


# This function fills in a Person message based on user input.
def prompt_for_address(person: Person):
    person.id = int(input("Enter person ID number: "))
    person.name = input("Enter name: ")

    email = input("Enter email address (blank for none): ")
    if email != "":
        person.email = email

    while True:
        number = input("Enter a phone number (or leave blank to finish): ")
        if number == "":
            break

        phone_number = person.phones.add()
        phone_number.number = number

        phone_type = input("Is this a mobile, home, or work phone? ")
        if phone_type == "mobile":
            phone_number.type = Person.PhoneType.PHONE_TYPE_MOBILE
        elif phone_type == "home":
            phone_number.type = Person.PhoneType.PHONE_TYPE_HOME
        elif phone_type == "work":
            phone_number.type = Person.PhoneType.PHONE_TYPE_WORK
        else:
            print("Unknown phone type; leaving as default value.")
