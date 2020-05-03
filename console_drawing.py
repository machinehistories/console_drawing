X_COUNT = 4  # set resolution of array in x
Y_COUNT = 4  # set resolution of array in y
XY_COUNT = X_COUNT * Y_COUNT  # set array count
X_INDEX = X_COUNT - 1  # helper for index in X_COUNT
XY_INDEX = XY_COUNT - 1  # helper for index in XY_COUNT
prev_position = 0  # used to store the previous position
states = [0] * XY_COUNT  # set the states array to XY_COUNT
# dictionary of keys, the basic idea is to use the keys to move your position and draw with strings
key_values = {
    "a": -1,
    "s": X_COUNT,
    "d": 1,
    "w": X_COUNT * -1,
    "Q": (X_COUNT * -1) - 1,
    "E": X_INDEX * -1,
    "A": X_INDEX,
    "D": X_COUNT + 1,
}


def instructions():
    width = 30
    print("=" * width)
    print("CONSOLE DRAWING".center(width, " "))
    print("=" * width)
    print("use these keys to draw".center(width, " "))
    print("-" * width)
    print("type a key and press enter".center(width, " "))
    print("-" * width)
    print("🠔 🠖 🠕 🠗".center(width, " "))
    print("a d w s".center(width, " "))
    print("⭦ ⭧ ⭨ ⭩".center(width, " "))
    print("Q E A D".center(width, " "))
    print("0 ↦ 1".center(width, " "))
    print(" x ".center(width, " "))


instructions()


def get_char():
    # Get char input.
    values = input()
    try:
        value = values[0]
    except IndexError:  # checks for exceptions
        value = "null"
    except NameError:
        print("")
    if values in key_values:  # checks if "item" is a *key* in the dict
        key_value = key_values[value]  # store the *value* for the *key* "item"
    else:
        key_value = 0
    return key_value


def toggle_state(position):
    current_state = states[position]  # gets the current state at a given position
    states[position] = (current_state + 1) % 2


def clear():
    print("{}[2J{}[;H".format(chr(27), chr(27)))


def set_position(prev_position, key_value):
    position = prev_position + key_value
    if position > XY_INDEX:
        position = XY_COUNT - position
    elif position < XY_INDEX * -1:
        position = position + XY_COUNT
    return position


def print_console():
    for i in range(XY_COUNT):
        if i % X_COUNT == 0:
            print(" ".join(map(str, states[i : i + X_COUNT])))


while True:
    key_value = get_char()
    position = set_position(prev_position, key_value)
    toggle_state(position)
    clear()
    print_console()
    prev_position = position
