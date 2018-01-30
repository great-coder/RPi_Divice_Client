__author__ = 'Mohammad Dehghan'

import sys
from services.net import connectivity
from controllers.account_controller import manage


def main():
    try:
        connectivity(20, 5)
        manage()
    except:
        error = sys.exc_info()[0]
        print("Exception occurred!")
        print(error)
        print("Shutting down system ...")
        sys.exit(0)


if __name__ == "__main__":
    main()
