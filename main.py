import cv2.cv2 as cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
import PIL
from PIL import Image
import pytesseract
from matplotlib import pyplot as plt
img_file = ("venv/pp.png")
img = cv2.imread(img_file)


def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width = im_data.shape[:2]

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')
    plt.show()

    def grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image = grayscale(img)
    cv2.imwrite("venv/king/gray.jpg", gray_image)
    thresh, im_bw = cv2.threshold(gray_image, 210, 230, cv2.THRESH_BINARY)
    cv2.imwrite("venv/king/bw_image.jpg", im_bw)
    display("king/bw_image.jpg")




