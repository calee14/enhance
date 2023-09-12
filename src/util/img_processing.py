import cv2
import numpy as np

def histogram_equalization(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_image = cv2.equalizeHist(gray_image)
    return equalized_image

def contrast_stretching(image):
    image_min = np.min(image)
    image_max = np.max(image)
    return (image - image_min) * (255 / (image_max - image_min))

def smooth_image(image, method='gaussian', kernel_size=(5, 5), sigma_x=0):
    if method == 'gaussian':
        return cv2.GaussianBlur(image, kernel_size, sigma_x)
    elif method == 'median':
        return cv2.medianBlur(image, kernel_size[0])
    elif method == 'bilateral':
        return cv2.bilateralFilter(image, kernel_size[0], sigma_x, sigma_x)
    
def median_filter(image, kernel_size=5):
    return cv2.medianBlur(image, kernel_size)

def inpaint_image(image, mask, method='telea', radius=3):
    if method == 'navier_stokes':
        return cv2.inpaint(image, mask, radius, cv2.INPAINT_NS)
    else:
        return cv2.inpaint(image, mask, radius, cv2.INPAINT_TELEA)
    
def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)