import argparse


class CommandLineInterface:

    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def main(self):
        parser = self.parser
        parser.add_argument(
            'square',
            type=int,
            help="display a square of a given number")

        parser.add_argument(
            "--verbose",
            action='store_true',
            help="increase output verbosity")

        args = parser.parse_args()
        answer = args.square**2

        if args.verbose:
            print("the square of {} equals {}".format(args.square, answer))
        else:
            print(answer)

cli = CommandLineInterface()
cli.main()
