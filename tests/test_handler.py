import pytest
from protobuf.out.addressbook_pb2 import Person
from protobuf.src import addressbook

addressbook_path = ".\\addressbook.txt"


@pytest.fixture(autouse=True, scope='session')
def setup_teardown():
    print('setup')
    yield
    print('teardown')


def test_redirector():
    from selenium_tutorial.redirector import redirector_test

    redirector_test()


def test_checkbox():
    from selenium_tutorial.checkboxes import checkbox_test

    checkbox_test(True, True)
    checkbox_test(True, False)
    checkbox_test(False, True)
    checkbox_test(False, False)


def test_person():
    person = Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = Person.PHONE_TYPE_HOME

    assert person.IsInitialized()


@pytest.mark.xfail(raises=BaseException)
def test_write_to_addressbook():
    person = Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = Person.PHONE_TYPE_HOME

    addressbook.write(addressbook_path, person)


@pytest.mark.xfail(raises=BaseException)
def test_read_addressbook():
    addressbook.read(addressbook_path)

