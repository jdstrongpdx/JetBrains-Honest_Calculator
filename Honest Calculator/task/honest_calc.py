MEMORY = 0


def main():
    """Main function to call other functions"""

    # get user input and error check
    x, oper, y = get_input()

    # generate print messages
    check(x, oper, y)

    # check divide by zero
    div_zero(oper, y)

    # calculate number and print
    num = (calculate(x, oper, y))
    print(float(num))

    # ask to store in memory
    remember(num)


def get_input():
    """ Gets user input and validates returning calculation subcomponents
        :return (int) x: the first element of an equation
        :return (int) y: the second element of an equation
        :return (str) oper: the operation symbol for the equation
    """

    # repeat loop until input validation is met
    while True:
        try:
            global MEMORY

            # ask user for input as "x operator y"
            calc = input(get_message(0))

            # split calc into variables
            split_calc = calc.split(" ")

            # if x == "M" replace M with global memory value
            if split_calc[0] == "M":
                x = MEMORY

            # type check x value for if int or if float
            else:
                if "." in split_calc[0]:
                    x = float(split_calc[0])
                    if x == int(x):
                        x = int(x)
                else:
                    x = int(split_calc[0])

            # if y == "M" replace M with global memory value
            if split_calc[2] == "M":
                y = MEMORY

            # type check y value for if int or if float
            else:
                if "." in split_calc[2]:
                    y = float(split_calc[2])
                    if y == int(y):
                        y = int(y)
                else:
                    y = int(split_calc[2])

            # store mathematical operator (as str)
            oper = (split_calc[1])

            # check if operator is valid
            allowed_oper = ["+", "-", "*", "/"]
            if oper not in allowed_oper:
                print(get_message(2))
                break

            # if validations pass, return values
            return x, oper, y

        # error checking if x and y are numbers
        except ValueError:
            print(get_message(1))
            pass


def div_zero(oper, y):
    """ Checks if there is division by zero and if so, cancels the current process and re-runs main
        :parameter (int) y: the second element in the math equation
        :parameter (str) oper: the operation symbol in the math equation
    """

    # check if zero division
    while oper == "/" and y == 0:
        print(get_message(3))
        main()
        exit()
    else:
        return


def check(x, oper, y):
    """ Using requested logic, appends pre-determined message strings to print final statement
        :parameter (int) x: the first element in the math equation
        :parameter (int) y: the second element in the math equation
        :parameter (str) oper: the operator in the math equation
    """

    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + get_message(6)
    if x == 1 or y == 1 and oper == "*":
        msg = msg + get_message(7)
    if x == 0 or y == 0 and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + get_message(8)
    if msg != "":
        msg = get_message(9) + msg
        print(msg)
    return


def is_one_digit(v):
    """ Checks if a value is a single digit integer
        :parameter (int) v: checks if v is a single digit integer
        :rtype: bool
    """

    if float(v) == int(v):
        if -10 < v < 10 and type(v):
            return True
    return False


def calculate(x, oper, y):
    """ Takes individual elements for a math equation and outputs a calculation of those elements
        :parameter (int) x: the first element in the math equation
        :parameter (int) y: the second element in the math equation
        :parameter (str) oper: the operator in the math equation
        :return (int/float): returns the calculation of the math equation as float or int
    """

    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/":
        return x / y


def get_message(p):
    """ Matches requested message and returns string
        :parameter (int) p: the integer value of the message case to print
        :return (str): returns the string that matches the value of p
    """

    match p:
        case 0:
            return "Enter an equation"
        case 1:
            return "Do you even know what numbers are? Stay focused!"
        case 2:
            return "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        case 3:
            return "Yeah... division by zero. Smart move..."
        case 4:
            return "Do you want to store the result? (y / n):"
        case 5:
            return "Do you want to continue calculations? (y / n):"
        case 6:
            return " ... lazy"
        case 7:
            return " ... very lazy"
        case 8:
            return " ... very, very lazy"
        case 9:
            return "You are"
        case 10:
            return "Are you sure? It is only one digit! (y / n)"
        case 11:
            return "Don't be silly! It's just one number! Add to the memory? (y / n)"
        case 12:
            return "Last chance! Do you really want to embarrass yourself? (y / n)"


def remember(num):
    """ Function to store a value into global memory
        :parameter (int) num: the value to store in global memory
    """

    msg_4 = input(get_message(4))
    if msg_4 == "y":
        global MEMORY
        if is_one_digit(num):
            msg_index = 10
            while msg_index < 13:
                choice = input(get_message(msg_index))
                if choice == "y":
                    msg_index += 1
                else:
                    break
            else:
                MEMORY = num
        else:
            MEMORY = num
    msg_5 = input(get_message(5))
    if msg_5 == "y":
        main()


if __name__ == "__main__":
    main()
