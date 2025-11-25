import random
import sys
os = sys.platform 
if os == 'linux' or os == 'darwin':
    win_os = False
    import pwd
else:
    win_os = True
    # import win32

    

flag_dc = {"-f": 1, "-pwd": 1, "-t": 1, "-u": 0, "-r": 1, "-h": 0}

def valid_argument(args):
    if len(args) > 0:
        for arg in args:
            if arg in flag_dc:
                if len(args) >= flag_dc[arg]:
                    return arg
                return False
    else:
        return False


def desktop_file(filename):
    ""


def passwd_gen(length):
    assert isinstance(length, int), "Must include an integer(ex. 4, 5, 6...)"
    
    hex_digit = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                      10: 'a',
                      11: 'b',
                      12: 'c',
                      13: 'd',
                      14: 'e',
                      15: 'f'}

    password = ''
    for i in range(length):
        d1 = random.randint(2, 7)
        d2 = random.randint(0, 15)
        hex_char = f'{d1}{hex_digit[d2]}'
        char = bytes.fromhex(hex_char).decode('utf-8')
        password += char
    return f'{password}\n'


def text_file(filename):
    assert isinstance(filename, str)
    txt = input("What do you want to write: \n")
    with open(filename, 'w') as f:
        f.write(txt)
    

def list_usrs():
    if not win_os:
        users = pwd.getpwall()

        for user in users:
            print(user)

    elif win_os:
        print("Sorry, we are still cleaning Windows. They are dirty")


def running_processes():
    ""


def process(flag, args):
    if flag == '-f':
        print(f"Creating file with the name {args[0]} on the desktop")
    elif flag == '-pwd':
        assert args[0] > 0, "Please put a number greater than 0"

        if int(args[0]) < 4:
            print("Weak password: X(")
        print(f"Generating password {args[0]} characters long...")
        print(passwd_gen(args[0]))
    elif flag == '-t':
        text_file(args[0])
        print("File created")
    elif flag == '-u':
        print("Listing users:")
        list_usrs()
    elif flag == '-r':
        print("Currently running processes:")
    elif flag == '-h':
        f = "-f : creates a file on the desktop"
        pwd = '-pwd : generates a password for you to use'
        t = "-t : create a text file with text you input"
        u = "-u : prints all users"
        r = "-r : returns a list of running processes"
        h = "-h : prints out a help command"
        print(f"Valid flags: --------\n{f}\n{pwd}\n{t}\n{u}\n{r}\n{h}")        