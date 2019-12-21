from typing import List


def check_message(message: str):
    """Check that message contains only russian letters ans spaces."""
    for letter in message:
        low = letter.lower()
        if not (low.isspace() or ord('а') <= ord(low) <= ord('я') or low == 'ё'):
            return False
    return True


def get_serial_number(character: str):
    """For russian letter returns its serial number and 0 for space."""
    if character.isspace():
        return 0
    low = character.lower()
    if low == 'ё':
        return 7
    code = ord(low)
    if code < ord('а') or code > ord('я'):
        raise ValueError("Can only get serial number of Russian letter or space.")
    addition = 2 if code > ord('е') else 1
    return addition + code - ord('а')


def get_letter(serial_number: int):
    """Return capital russian letter by it serial number or space if serial number is 0."""
    if serial_number < 0 or serial_number > 33:
        raise ValueError("Invalid serial number: {:d}.".format(serial_number))
    if serial_number == 0:
        return " "
    if serial_number == 7:
        return 'ё'
    addition = 2 if serial_number > 7 else 1
    return chr(ord('А') + serial_number - addition)


def encode_message(message: str):
    """
    Encode message by using using the following method:
    1)For each character get it 6 bit code: for letter it is its serial number, for space the code is 000000.
    2)Split message in pairs of characters. If there is odd number of characters,
    space will be added to the end of message.
    3)In each pair concatenate 6bit codes. Gotten sequences of 12 bit numbers is result of encoding.
    """
    if not check_message(message):
        raise ValueError("Message should contains only russian letters or spaces.")
    result = []
    length = len(message)
    for i in range(1, length, 2):
        first = get_serial_number(message[i - 1])
        second = get_serial_number(message[i])
        result.append(64 * first + second)
    if length % 2 == 1:
        result.append(64 * get_serial_number(message[length - 1]))
    return result


def decode_message(encoded_sequence: List[int]):
    """Decode message encoded by @encode_message function."""
    result = []
    for element in encoded_sequence:
        first = element // 64
        second = element % 64
        result.append(get_letter(first))
        result.append(get_letter(second))
    return "".join(result)


if __name__ == '__main__':
    print(encode_message("СЕРВЕР"))
