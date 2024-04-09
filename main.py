# Remove non-ASCII characters from a string in Python

import string


def remove_non_ascii(a_str):
    ascii_chars = set(string.printable)

    return ''.join(
        filter(lambda x: x in ascii_chars, a_str)
    )


print(remove_non_ascii('a€bñcá'))  # 👉️ 'abc'
print(remove_non_ascii('a_b^0'))  # 👉️ a_b^0