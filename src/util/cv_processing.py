import cv2
import numpy as np

def reduce_noise(image, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21):
    # Apply image enhancements
    # Denoise the image
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, h, hColor, templateWindowSize, searchWindowSize)
    return denoised_image

def contrast_stretching(image, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1):
    # Perform contrast stretching
    contrast_stretched_image = cv2.normalize(image, None, alpha, beta, norm_type, dtype)
    return contrast_stretched_image

def sharpen_image(image, kernel=None):
    # Image Sharpening
    if not kernel:
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    sharpened_image = cv2.filter2D(image, -1, kernel=kernel)
    return sharpened_image

def brightness(image, alpha=1, beta=5):
    # Brightness Adjustment
    brightness_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return brightness_image

def gamma_correction(image, gamma=1.5):
    # Gamma Correction
    lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    gamma_corrected_image = cv2.LUT(image, lookup_table)
    return gamma_corrected_image