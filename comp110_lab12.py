"""
Module: comp110_lab12

Lab 12: Image convolution
"""

import comp110_image


def apply_kernel(img, img_copy, x, y, kernel):
    red_sum = 0
    green_sum = 0
    blue_sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            # To do: Get the correct neighborhood pixel

            # To do: add to red_sum, green_sum, and blue_sum based on
            # multiplication of pixel
            pass

    # To do: set the pixel in img to the sums

def convolution(img, kernel):
    img_copy = img.copy()

    # To Do: modify range to avoid border pixels
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            # To Do: call your function here
            pass

def main():
    # Do not modify this function

    cat_img = comp110_image.Picture(filename="cute-cat.gif")
    cat_img.show()
    convolution(cat_img, [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    cat_img.show()


""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
