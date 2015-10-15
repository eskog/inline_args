#!/usr/bin/python
import sys
import getopt


def main(argv):
    # Stuff before arguments
    grammar = "Default value"
    debug = 0
    try:
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-d':
            debug= 1
        elif opt in ("-g", "--grammar"):
            grammar = arg
        elif opt in (null):
            usage()
            sys.exit(4)
        print grammar
        print debug


def usage():
    usage = """
    -h --help           Prints this helpscreen.
    -d --Debug          Enables Debug mode.
    -g --grammar arg    Changes from default grammar to arg
    """
    print usage

if __name__ == "__main__":
    main(sys.argv[1:])