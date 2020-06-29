import one

print("top level print statement in two.py")

one.func()


if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")