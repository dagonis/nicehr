import sys

import nicehr

def main():
    print("This is an example script for nicehr. Here is a simple * line.")
    print(nicehr.nice_hr("*"))
    print("Here is a sample line with a message in the middle of the line.")
    print(nicehr.nice_hr("*", " Look at this Line "))
    print("Here is a red version of the line above.")
    print(nicehr.nice_hr("*", " Look at this Line ", color="red"))
    print("Here is a black version of the line above.")
    print(nicehr.nice_hr("*", " Look at this Line ", color="black"))
    print("Finally, here is a rainbow version!")
    print(nicehr.nice_hr("*", " Look at this Line ", colorful=True))
    print("Thank you for taking a look.")

if __name__ == '__main__':
    sys.exit(main())