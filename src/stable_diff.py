import cv2
import time
from diffusers import StableDiffusionUpscalePipeline
import torch
from io import BytesIO
from PIL import Image
import numpy as np

video_path = './media/name.mp4'

# load model and scheduler
model_id = "stabilityai/stable-diffusion-x4-upscaler"
pipeline = StableDiffusionUpscalePipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipeline = pipeline.to("cuda")

cap = cv2.VideoCapture(video_path)

cap.set(cv2.CAP_PROP_POS_FRAMES, 250)
success, frame = cap.read()

if success:
    with torch.no_grad():
        # use the super resolution model to upscale the image, timing how
        # long it takes
        small_frame = cv2.resize(frame, (frame.shape[1]//6, frame.shape[0]//6))
        img_array = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        print('IMAGE DIM:', img_array.shape)
        small_frame = Image.fromarray(img_array, 'RGB').convert('RGB')

        # run x4 upscaler
        start = time.time()
        prompt = "realistic, no wrinkle, vibrant, smooth"
        upscaled = pipeline(prompt=prompt, image=small_frame).images[0]
        end = time.time()
        print("[INFO] super resolution took {:.6f} seconds".format(
        end - start))

        # show results
        upscaled.save('test.png')
        print('UPSCALED SIZE:', upscaled.size)
        cv2.imwrite('original.png', frame)
        # cv2.imshow('Upscaled Frame', upscaled)
        # cv2.imshow('Original Frame', frame)
        # k = cv2.waitKey(10000)

        # if k == 27:         # If escape was pressed exit
        #     cv2.destroyAllWindows()

# while True:
#     success, frame = cap.read()
#     if success:
#         cv2.imshow('Frame', frame)

#         # Press Q on keyboard to  exit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#         break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()