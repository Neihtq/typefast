import curses

from cli.game import run
from cli.menu import countdown
from text_acquisition.quote_acquisition import get_quote
from text_acquisition.text_loader import load_text


def main(console):
    from utils.colors import colors
    quote = "To be honest, it was slavery. Nobody should have any romantic ideas about working underground. It's very, very dangerous. You always knew you were living in danger. You were on your hands and knees half the day."
    author = 'someone'

    curses.cbreak()
    row, seen = 0, {None}
    data = load_text(seen)
    while True:
        (quote, author) = data.pop()
        row, duration = run(quote, console, colors, author)
        countdown(row, console, duration)


if __name__ == '__main__':
    curses.wrapper(main)
