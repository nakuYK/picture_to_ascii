from PIL import Image
import argparse

def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return " "
    gary = (2126 * r + 7152 *g + 722 * b) / 10000
    ascii_char = list("$@B%8&WM#*oahkbdpwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")
    x = int((gary / (alpha + 1.0)) * len(ascii_char))
    return ascii_char[x]

def write_file(out_file_name, content):
    with open(out_file_name, "w") as f:
        f.write(content)

def main(file_name="test.jpg", width=80, height=40, out_file_name="out_file"):
    text = ""
    im = Image.open(file_name)
    im = im.resize((width, height),Image.NEAREST)
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j, i))
            text += get_char(*content)
        text += "\n"
    print(text)
    write_file(out_file_name, text)

if __name__=='__main__':
    main(file_name="picture.jpg")