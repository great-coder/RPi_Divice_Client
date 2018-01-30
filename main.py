__author__ = 'Mohammad Dehghan'

import sys
from services import net
from controllers.account_controller import login
from security import validation


def main():
    try:
        net.connectivity(10, 5)
        # Check if there is any token from before and check it's expiration, then do login
        if not validation.token_validation():
            login()
        else:
            # TODO: Connect to Chat Hub and broadcast a Hello message! Then go to idle state!!!
            print("Ex-provided token is still valid, use that.")
    except:
        error = sys.exc_info()[0]
        print("Exception occurred!")
        print(error)
        print("Shutting down system ...")
        sys.exit(0)


if __name__ == "__main__":
    main()
