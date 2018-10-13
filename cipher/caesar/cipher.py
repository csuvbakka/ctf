letters_in_alphabet = 26


def encrypt(text, shift):
    """Encrypts text using Caesar cipher with the given shift.

    :param string text: The text to encrypt.
    :param int shift: The shift to apply.
    :return: The encrypted text."""
    encrypted = [encrypt_char(c, shift) for c in text]
    return ''.join(encrypted)


def decrypt(text, shift):
    """Decrypts text using Caesar cipher with the given shift.

    :param string text: The text to decrypt.
    :param int shift: The shift to apply.
    :return: The decrypted text."""
    decrypted = [encrypt_char(c, shift * -1) for c in text]
    return ''.join(decrypted)


def brute_force(haystack, needle):
    """Tries to find the given string in a Caesar encrypted text.

    Decrypts haystack with shifts of -26 to +26 until it finds needle in the decrypted text.

    :param string haystack: The encrypted text.
    :param string needle: The string to find.
    :return: None if needle is not found in haystack.
             (int, string) where int is the shift which was used to decrypt haystack,
                           and string is the decrypted haystack.
    """
    for i in range(-1 * letters_in_alphabet, letters_in_alphabet):
        decrypted = decrypt(haystack, i)
        if needle in decrypted:
            return i, decrypted

    return None


def _do_encrypt(letter, shift):
    """Encrypts a letter using modular arithmetic.

    :param int letter: Index of a letter in the alphabet.
    :param int shift: The shift to apply.
    :return: The encrypted letter's index in the alphabet. """
    assert 0 <= letter <= letters_in_alphabet
    return (letter + shift) % letters_in_alphabet


def _correct_index(char, count):
    return ord(char) - count


def _encrypt_alpha(char, shift):
    assert char.isalpha()
    index_correction = ord('a') if char.islower() else ord('A')

    letter = _correct_index(char, index_correction)
    encrypted = _do_encrypt(letter, shift)

    encrypted += index_correction
    return chr(encrypted)


def encrypt_char(char, shift):
    """Applies the given shift to the the given character.

    :note The case of the character is preserved.

    :param char char: The character to encrypt.
    :param int shift: The shift to apply.
    :return The given char if it is not a letter from the alphabet.
            The given character shifted by the given shift otherwise."""
    if char.isalpha():
        return _encrypt_alpha(char, shift)
    else:
        return char
