# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class emp(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("Call method is called...", args, **kwargs)
        return ''

    def __str__(self):
        return 'Hello Emp'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    e = emp()
    x = e()
    print(e)
    # print(dir(e))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
