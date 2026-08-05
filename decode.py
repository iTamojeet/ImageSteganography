from PIL import Image


def binary_to_text(binary):

    chars = []

    for i in range(0, len(binary), 8):

        byte = binary[i:i+8]

        chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def decode_image(image_path):

    img = Image.open(image_path)

    pixels = img.load()

    width, height = img.size

    binary_data = ""

    for y in range(height):

        for x in range(width):

            pixel = pixels[x, y]

            for i in range(3):

                binary_data += str(pixel[i] & 1)

    decoded = binary_to_text(binary_data)

    return decoded.split("#####")[0]


secret = decode_image("outputs\\output.png")

print("Hidden Message:")

print(secret)