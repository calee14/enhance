import cv2
import time
from diffusers import StableDiffusionUpscalePipeline
import torch
from io import BytesIO
from PIL import Image

video_path = './media/name.mp4'

# load model and scheduler
model_id = "stabilityai/stable-diffusion-x4-upscaler"
pipeline = StableDiffusionUpscalePipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipeline = pipeline.to("cuda")

cap = cv2.VideoCapture(video_path)

cap.set(cv2.CAP_PROP_POS_FRAMES, 200)
success, frame = cap.read()
if success:
    # use the super resolution model to upscale the image, timing how
    # long it takes
    small_frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))
    byte_data = BytesIO(small_frame)
    small_frame = Image.open(small_frame).convert("RGB")
    start = time.time()
    prompt = "hot sexy 4k"
    upscaled = pipeline(prompt=prompt, image=frame).images[0]
    end = time.time()
    print("[INFO] super resolution took {:.6f} seconds".format(
	end - start))
    cv2.imshow('Upscaled Frame', upscaled)
    cv2.imshow('Original Frame', frame)
    k = cv2.waitKey(10000)

    if k == 27:         # If escape was pressed exit
        cv2.destroyAllWindows()
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