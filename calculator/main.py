#assumes python3.
from subprocess import Popen,PIPE

def main():
    p = Popen([r'C:\Program Files\nodejs\npm.cmd', 'start'], stdout=PIPE, stderr=PIPE)


if __name__ == "__main__":
    main()