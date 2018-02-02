__author__ = 'Mohammad Dehghan'

import sys
from controllers.account_controller import manage


def main():
    try:
        manage()
        # TODO: Connect Chat Hub
    except:
        error = sys.exc_info()[0]
        print("Exception occurred!")
        print(error)
        print("Shutting down system ...")
        sys.exit(0)


if __name__ == "__main__":
    main()
