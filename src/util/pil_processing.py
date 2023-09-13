from PIL import ImageEnhance, Image
import cv2
import numpy as np

def adjust_brightness_contrast(image, alpha=1.2, beta=13):
    return cv2.addWeighted(image, alpha, image, 0, beta)

def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def adjust_contrast(image, factor=1.5):
    if image is not Image:
        img_array = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print('IMAGE DIM:', img_array.shape)
        image = Image.fromarray(img_array, 'RGB').convert('RGB')

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(factor)
    image = np.array(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    return image

def default_process(image):
    image = adjust_brightness_contrast(image)
    image = sharpen_image(image)
    image = adjust_contrast(image)
    return image