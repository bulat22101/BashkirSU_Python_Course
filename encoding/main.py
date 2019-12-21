from typing import List


def check_message(message: str):
    for letter in message:
        low = letter.lower()
        if not (low.isspace() or ord('а') <= ord(low) <= ord('я') or low == 'ё'):
            return False
    return True


def get_serial_number(letter: str):
    if letter.isspace():
        return 0
    low = letter.lower()
    if low == 'ё':
        return 7
    code = ord(low)
    if code < ord('а') or code > ord('я'):
        raise ValueError("Can only get serial number of Russian letter.")
    addition = 2 if code > ord('е') else 1
    return addition + code - ord('а')


def get_letter(serial_number: int):
    if serial_number < 0 or serial_number > 33:
        raise ValueError("Invalid serial number: {:d}.".format(serial_number))
    if serial_number == 0:
        return " "
    if serial_number == 7:
        return 'ё'
    addition = 2 if serial_number > 7 else 1
    return chr(ord('А') + serial_number - addition)


def encode_message(message: str):
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
    result = []
    for element in encoded_sequence:
        first = element // 64
        second = element % 64
        result.append(get_letter(first))
        result.append(get_letter(second))
    return "".join(result)


if __name__ == '__main__':
    print(encode_message("СЕРВЕР"))
