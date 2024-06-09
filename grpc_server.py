from concurrent import futures
import logging

import grpc
from protobuf.out import addressbook_pb2_grpc
from protobuf.out import addressbook_pb2

from protobuf.src import addressbook

addressbook_path = ".\\addressbook.txt"


def serve():
    logging.basicConfig()
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addressbook_pb2_grpc.add_PersonRequesterServicer_to_server(AddressBookAPI(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    input("press enter to quit")
    server.stop(10)


class AddressBookAPI(addressbook_pb2_grpc.PersonRequester):

    def AddPerson(self,
                  request: addressbook_pb2.Person,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        message: str = "Person added"

        try:
            addressbook.write(addressbook_path, request)
        except BaseException as e:
            message = repr(e)

        return addressbook_pb2.PersonResponse(message=message, person=None)

    def GetPerson(self,
                  request: addressbook_pb2.PersonId,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        person = None
        message = "Person retrieved"
        try:
            person = addressbook.get_person_by_id(addressbook_path, request.id)
        except BaseException as e:
            message = repr(e)

        return addressbook_pb2.PersonResponse(message=message, person=person)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
