def hello(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!")

def main():
    print("This message is printed when 'greetings.py' is run directly.")
    hello("Jay")
    goodbye("Jay")


# This statement is being used to check whether the script is being run
# directly or imported as a module
if __name__ == "__main__":
    main()
