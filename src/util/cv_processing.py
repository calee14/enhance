import cv2
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import convolve
from skimage.filters import unsharp_mask
from PIL import Image, ImageFilter, ImageEnhance

def reduce_noise(image, h=5, hColor=5, templateWindowSize=5, searchWindowSize=20):
    # Apply image enhancements
    # Denoise the image
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, h, hColor, templateWindowSize, searchWindowSize)
    return denoised_image

def contrast_stretching(image, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1):
    # Perform contrast stretching
    contrast_stretched_image = cv2.normalize(image, None, alpha, beta, norm_type, dtype)
    return contrast_stretched_image


def unsharpen_image(image, radius=2, amount=2):
    # uses pillows unsharpen filter
    img_array = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(img_array, 'RGB').convert('RGB')
    for _ in range(1):
        image = image.filter(ImageFilter.UnsharpMask(radius=3, percent=196, threshold=5))
        # image = image.filter(ImageFilter.SHARPEN)
        for _ in range(1): # try 1-2
            image = image.filter(ImageFilter.SHARPEN)

        for _ in range(1): # try 1-5
            image = image.filter(ImageFilter.SMOOTH_MORE)

    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

def brightness(image, alpha=1, beta=3):
    # Brightness Adjustment
    brightness_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return brightness_image

def gamma_correction(image, gamma=1.5):
    # Gamma Correction
    lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    gamma_corrected_image = cv2.LUT(image, lookup_table)

    return gamma_corrected_image

def adjust_brightness_contrast(image, alpha=1.2, beta=13):
    return cv2.addWeighted(image, alpha, image, 0, beta)

def smooth_image(image, method='gaussian', kernel_size=(5, 5), sigma_x=0):
    if method == 'gaussian':
        return cv2.GaussianBlur(image, kernel_size, sigma_x)
    elif method == 'median':
        return cv2.medianBlur(image, kernel_size[0])
    elif method == 'bilateral':
        return cv2.bilateralFilter(image, kernel_size[0], sigma_x, sigma_x)


def default_process(image):
    # image = reduce_noise(image)
    image = contrast_stretching(image)
    image = unsharpen_image(image)
    image = smooth_image(image, method='gaussian')
    image = brightness(image)
    # image = gamma_correction(image, 1.0)
    return image
    