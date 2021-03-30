# Global scope variable:
someVariable = "World"


def print_function():
    print("In function: %s" % someVariable)


print("Global: %s" % someVariable)

print_function()

someVariable = "Lorem ipsum"

print_function()
