def func():
    print("func() in one.py")

# Lots more functions

print("top level print statement in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into in another module")

# # also use for organizing code
# if __name__ == "__main__":
#     # if script being run directly run all the functions
#     print("file being run directly so all code will run")
#     # call all functions
#     func()
