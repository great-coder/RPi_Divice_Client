import sys


def main():
    print("Inside main")


if __name__ == "__main__":
    print("Calling main")
    try:
        main()
    except:
        error = sys.exc_info()[0]
        print("Exception occurred!")
        print(error)
    finally:
        print("finally clause")
