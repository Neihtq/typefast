def update_console(row, col, text, color, console):
    console.addstr(row, col, text, color)
    console.refresh()


def update_console_and_position(row, position, text, key, color, user_input, console):
    update_console(row, position, text, color, console)
    position += 1
    user_input.append(key)

    return position