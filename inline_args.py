#!/usr/bin/python
import sys, getopt

grammar = "default grammar"

def main(argv):
    #Stuff before arguments
    grammar = "nej"
    debugvar = 0
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
            debugvar= 1
        elif opt in ("-g", "--grammar"):
            grammar = arg
        print grammar
        print debugvar


def usage():
    print "This is the helpscreen.  Please do the needfull"
    print "Usage: inline_args.py -h -g -d"

if __name__ == "__main__":
    main(sys.argv[1:])