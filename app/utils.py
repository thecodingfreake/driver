# utils.py

import requests
import json
from PIL import Image
from io import BytesIO
def mirror_image(image):
    # Open the uploaded image using Pillow
    img = Image.open(image)
    
    # Mirror the image horizontally
    mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    
    # Convert the mirrored image back to BytesIO
    mirrored_img_io = BytesIO()
    mirrored_img.save(mirrored_img_io, format='JPEG')
    mirrored_img_io.seek(0)
    
    return mirrored_img_io
def upload_to_imgbb(image):
    api_key = 'c0f297de797430cc9d7de342f37144d6'

    try:
        with open(image.path, 'rb') as file:
            response = requests.post(
                'https://api.imgbb.com/1/upload',
                data={'key': api_key},
                files={'image': mirror_image(file)}
            )
            data = response.json()
            if data['data']:
                return data['data']['url']
    except Exception as e:
        print(f"Error uploading image to ImgBB: {str(e)}")
        return None
