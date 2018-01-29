import sys
from services import net
from controllers.account_controller import login


def main():
    try:
        net.connectivity(10, 5)
        login()
    except:
        error = sys.exc_info()[0]
        print("Exception occurred!")
        print(error)
        print("Shutting down system ...")
        sys.exit(0)


if __name__ == "__main__":
    main()
