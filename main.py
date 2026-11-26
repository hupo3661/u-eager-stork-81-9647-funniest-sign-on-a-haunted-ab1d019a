"""Funniest Sign on a Haunted House — make.fun entry.

Writes one funny haunted-house sign (120 characters or fewer)
to /output/entry.txt for the judge to read. The sign reads like a
real warning taped to a haunted front door: do not reboot the ghost,
he has been stuck at 99% since 2003 and now takes it out on the Wi-Fi.
"""

TEXT = "DO NOT REBOOT THE GHOST. He's been stuck at 99% since 2003 and now takes it out on the Wi-Fi."

OUTPUT_PATH = '/output/entry.txt'
MAX_CHARS = 120


def write_entry(text):
    """Write the sign to the output file, exactly one trailing newline."""
    assert len(text) <= MAX_CHARS, 'entry over 120 characters'
    # One line, one trailing newline, nothing else: the gate checks
    # the file is 1 to 120 characters of UTF-8 text.
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(text + '\n')


def main():
    write_entry(TEXT)


if __name__ == '__main__':
    main()
