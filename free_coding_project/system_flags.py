import sys
os = sys.platform 
if os == 'linux' or os == 'darwin':
    win_os = False
    import pwd
else:
    win_os = True
    import win23net

flag_lst = [("-f", 1), ("-pwd", 1), ("-t", 3), ("-u", 0), ("-r", 1), ("-h", 0)]

def valid_argument(args):
    if len(args) > 0:
        for arg in args:
            for flag in flag_lst:
                if arg == flag[0]:
                    if len(args) >= flag[1]:
                        return flag
                    return False
    else:
        return False

def desktop_file(filename):
    ""

def passwd_gen(length):
    ""

def text_file(filename, file_path, msg):
    ""

def list_usrs():
    if not win_os:
        users = pwd.getpwall()

        for user in users:
            print(user)

    elif win_os:
        print("We be using windows")


def running_processes():
    ""


def process(flag, args):
    f = flag[0]

    if f == '-f':
        print(f"Creating file with the name {args[1]} on the desktop")
    elif f == '-pwd':
        if int(args[1]) < 4:
            print("Weak password ;)")
        print(f"Generating password {args[1]} characters long...")
    elif f == '-t':
        print("What do you want to write?")
        text = input()
    elif f == '-u':
        print("Listing users:")
        list_usrs()
    elif f == '-r':
        print("Currently running processes:")
    elif f == '-h':
        f = "-f : creates a file on the desktop"
        pwd = '-pwd : generates a password for you to use'
        t = "-t : create a text file with text you input"
        u = "-u : prints all users"
        r = "-r : returns a list of running processes"
        h = "-h : prints out a help command"
        print(f"Valid flags: --------\n{f}\n{pwd}\n{t}\n{u}\n{r}\n{h}")        