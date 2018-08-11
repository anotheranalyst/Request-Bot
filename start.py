'''
    File name: start.py
    Author: Adolfo Garza
    Date created: 08/11/2018
    Date last modified: 08/11/2018
    Python Version: 3.6
'''
from request_bot import RequestBot
from graduate import Graduate


def main():
    print("\n--------------------------------")
    print("Request Bot: Fetch Graduate Data")
    print("Coder: Adolfo Garza")
    print("Last updated: August, 11, 2018")
    print("--------------------------------\n")

    Graduate.launch_sequence(request_mechanism=RequestBot)


if __name__ == "__main__":
    main()
