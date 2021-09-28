#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is math_program


def main():

    loop_counter = 0
    answer = 0
    # input
    integer = input("Enter any pisitive number: ")
    print("")

    # process & output
    try:
        number = int(integer)
        while loop_counter <= number:
            print("{0} + {1} = {2}".format(answer, loop_counter, answer + loop_counter))
            answer = answer + loop_counter
            loop_counter = loop_counter + 1

    except Exception:
        print("Please follow the instructions! Use numbers")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
