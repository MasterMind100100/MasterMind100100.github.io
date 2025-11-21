"""This page is to call the other pages
    Also have a nice welcome page"""
import system_flags
import sys

test = True
if test:
    args = ['welcom_page.py', '-u']
else:
    args = sys.argv[1:]


def main():
    welcome_message = r"""
     _________________________
    |//         _____   __  \\|
    |/ |    |  |       |__|  \|
    |  |____|  |____    __    |
    |  |    |  |       |  |   |
    |  |    |  |_____  |__|   |
    |_________________________|
            Tervetuloa
"""

    print(welcome_message)
    print("Processing request...\n")
    checker = system_flags.valid_argument(args)

    if checker:
        system_flags.process(checker, args)
    else:
        print("Invalid Argument")


if __name__=="__main__":
    main()