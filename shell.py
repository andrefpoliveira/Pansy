from lib.interpreter import run
import sys

def main(run_test=None):
    keep_run = True
    while keep_run:
        if run_test != None:
            keep_run = False
            text = run_test
        else:
            text = input('Pansy> ')

        if text == "exit": break
        if text.strip() == '': continue
        result, error = run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            """
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
            """

if __name__ == '__main__':
    if len(sys.argv) != 1:
        main(sys.argv[1])
    else:
        main()