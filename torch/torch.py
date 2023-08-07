from stem import Signal
from stem.control import Controller
from api import get_info

USE_CURL = False
CONTROL_PORT = 49051


def print_ip(title, direct=False):
    ip, country = get_info(direct)
    print(f'{title} {ip} [{country}]')
    return ip, country


if __name__ == "__main__":
    print('Running...')
    try:
        with Controller.from_port(port=CONTROL_PORT) as controller:
            controller.authenticate()
            print_ip('direct: ', True)
            print_ip('socks5: ')
            if controller.is_newnym_available():
                controller.signal(Signal.NEWNYM)
                print_ip('new   : ')
            else:
                print('warn: NYM is not available.')

    except Exception as err:
        print('failed!')
        print(err)
        exit()
    finally:
        input('press any key to exit...')
