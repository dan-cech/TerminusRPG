#=== /// TEXT COLOR /// ===#
def black(a):
    return (f"\033[30m{a}\033[0m")
def red(a):
    return (f"\033[31m{a}\033[0m")
def green(a):
    return (f"\033[32m{a}\033[0m")
def yellow(a):
    return (f"\033[33m{a}\033[0m")
def blue(a):
    return (f"\033[34m{a}\033[0m")
def purple(a):
    return (f"\033[35m{a}\033[0m")
def azure(a):
    return (f"\033[36m{a}\033[0m")
def white(a):
    return (f"\033[37m{a}\033[0m")

#=== /// TEXT BACKGROUND COLOR /// ===#
def blackbg(a):
    return (f"\033[40m{a}\033[0m")
def redbg(a):
    return (f"\033[41m{a}\033[0m")
def greenbg(a):
    return (f"\033[42m{a}\033[0m")
def yellowbg(a):
    return (f"\033[43m{a}\033[0m")
def bluebg(a):
    return (f"\033[44m{a}\033[0m")
def purplebg(a):
    return (f"\033[45m{a}\033[0m")
def azurebg(a):
    return (f"\033[46m{a}\033[0m")
def whitebg(a):
    return (f"\033[47m{a}\033[0m")

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(n):
    import sys
    from time import sleep
    
    anim = ["[-----]","[#----]","[##---]","[###--]","[####-]","[#####]",]
    for _ in range(1):
        for frame in anim:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            sleep(n/6)
    sys.stdout.write(f"   ")
    sys.stdout.flush()
    clear()