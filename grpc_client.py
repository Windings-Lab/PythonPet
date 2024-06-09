from __future__ import print_function

import logging

import grpc
from protobuf.out import addressbook_pb2_grpc
from protobuf.out import addressbook_pb2


def run():
    logging.basicConfig()
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    person = addressbook_pb2.Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = addressbook_pb2_grpc.PersonRequesterStub(channel)
        add_response = stub.AddPerson(person)
        retrieve_response = stub.GetPerson(addressbook_pb2.PersonId(id=1))
    print(f"Add: {add_response.message}\nRetrieve: {retrieve_response.message}")
    input("press enter to exit")


if __name__ == "__main__":
    run()
