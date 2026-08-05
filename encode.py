from PIL import Image


def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


def encode_image(image_path, secret_message, output_path):

    img = Image.open(image_path)
    pixels = img.load()

    secret_message += "#####"

    binary_data = text_to_binary(secret_message)

    data_index = 0

    width, height = img.size

    for y in range(height):

        for x in range(width):

            pixel = list(pixels[x, y])

            for i in range(3):

                if data_index < len(binary_data):

                    pixel[i] = pixel[i] & ~1 | int(binary_data[data_index])

                    data_index += 1

            pixels[x, y] = tuple(pixel)

            if data_index >= len(binary_data):
                break

        if data_index >= len(binary_data):
            break

    img.save(output_path)

    print("Message Hidden Successfully!")


message = input("Enter Secret Message : ")

encode_image(
    "images\\input.png",
    message,
    "outputs\\output.png"
)