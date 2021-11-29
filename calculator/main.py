#assumes python3.
import subprocess
import socket
from time import sleep


def check_port(port, host="127.0.0.1"):
    """
    Return True if we can't connect
    False if we can't connect

    :param port:
    :param host:
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = 1
    try:
        result = sock.connect_ex((host, port))
    except (socket.gaierror, socket.timeout, socket.herror):
        return True
    finally:
        sock.close()
    return result != 0


def main():
    args = ["npm.cmd","start","run"]
    proc = subprocess.Popen(args, stderr=subprocess.STDOUT)
    while check_port(3000):
        sleep(1)
    proc.kill()

if __name__ == "__main__":
    main()