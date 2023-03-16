import random
import math

dictionary = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
              'Ф',
              'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8',
              '9']


def find_public_key(lower_value, upper_value):
    simple_numbers = []
    for number in range(lower_value, upper_value + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                simple_numbers.append(number)

    random_index1 = random.randint(0, len(simple_numbers) - 1)
    random_index2 = random.randint(0, len(simple_numbers) - 1)
    if random_index2 == random_index1:
        while random_index2 == random_index1:
            random_index2 = random.randint(0, len(simple_numbers) - 1)
    if random_index2 < random_index1:
        t = random_index2
        random_index2 = random_index1
        random_index1 = t

    p = simple_numbers[random_index1]
    q = simple_numbers[random_index2]
    n = p * q
    fi_n = (p - 1) * (q - 1)  # количество целых положительных чисел, не превосходящих n и взаимно простых с n

    array = []
    for x in range(1, n):
        if math.gcd(x, fi_n) == 1:
            array.append(x)

    index = random.randint(0, len(array) - 1)
    e = array[index]
    open_key = [e, n]

    return [open_key, fi_n, e, n]


def is_int(value):
    return float(value).is_integer()


def find_private_key(fi_n, e, n):
    k = 0
    d = int((k * fi_n + 1) / e)
    while not is_int((k * fi_n + 1) / e):
        k = k + 1
    else:
        d = int((k * fi_n + 1) / e)
    private_key = [d, n]

    return private_key


def encode(public_key, message):
    e = public_key[0]
    n = public_key[1]
    encode_message = []
    for x in message:
        for char in dictionary:
            if x == char:
                encode_char = pow(dictionary.index(char), e) % n
                encode_message.append(encode_char)

    return encode_message


def decode(private_key, encode_message):
    d = private_key[0]
    n = private_key[1]
    decode_message = []

    for x in encode_message:
        index = pow(int(x), d) % n
        k = dictionary[index]
        decode_message.append(k)

    decode_msg = ''.join(map(str, decode_message))
    return decode_msg


if __name__ == '__main__':
    message = "КАФСИ КАФСИ 123456789 123456789 123456789"
    find_key = find_public_key(10, 30)
    open_key = find_key[0]
    print("Public key is ", open_key)

    private_key = find_private_key(find_key[1], find_key[2], find_key[3])
    # print("Private key: ", private_key)

    encode_msg = encode(open_key, message)
    print("Encode message: ", encode_msg)
    print("Decode message: ", decode(private_key, encode_msg))
