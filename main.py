from protobuf.src import addressbook_api


def main():
    addressbook_path = ".\\addressbook.txt"
    addressbook_api.read(addressbook_path)


if __name__ == '__main__':
    main()
