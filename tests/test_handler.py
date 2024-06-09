import pytest
from protobuf.out import addressbook_pb2


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
    person = addressbook_pb2.Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

    assert person.IsInitialized()
