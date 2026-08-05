from PIL import Image


END_MARKER = "#####"


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def encode_image(image, secret_message):

    img = image.convert("RGB")

    pixels = img.load()

    secret_message += END_MARKER

    binary_data = text_to_binary(secret_message)

    data_index = 0

    width, height = img.size

    for y in range(height):

        for x in range(width):

            pixel = list(pixels[x, y])

            for i in range(3):

                if data_index < len(binary_data):

                    pixel[i] = (pixel[i] & ~1) | int(binary_data[data_index])

                    data_index += 1

            pixels[x, y] = tuple(pixel)

            if data_index >= len(binary_data):
                return img

    return img


def decode_image(image):

    img = image.convert("RGB")

    pixels = img.load()

    width, height = img.size

    binary_data = ""

    for y in range(height):

        for x in range(width):

            pixel = pixels[x, y]

            for i in range(3):

                binary_data += str(pixel[i] & 1)

    text = binary_to_text(binary_data)

    return text.split(END_MARKER)[0]