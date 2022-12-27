from io import BytesIO
from PIL import Image
from django.core.files import File


# Image compression method
def compress_image(image, size=(1000, 1000)):
    temp_image = Image.open(image).convert('RGB')
    temp_image.thumbnail(size)
    temp_image_io = BytesIO()
    temp_image.save(temp_image_io, 'png', quality=80)
    new_image = File(temp_image_io, name=image.name)
    return new_image

# size=(1000, 1000)
# -> 원본 비율을 유지하면서 가로 세로 중 큰 값을 1000px 로 리사이즈