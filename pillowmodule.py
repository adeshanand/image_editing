# installation of pillow library
# change the image extension
# resize image files
# resize multiple images using for loop
# ------------------------------------------
# installation of pillow library
# pip install Pillow
# ------------------------------------------
# change the image extension
# from PIL import Image
# img1 = Image.open('puppy1.jpg')
# img1.save('puppy1.png')
# img1.show() # uses the default image viewer and shows the image
# ------------------------------------------
# from PIL import Image
# MAX_SIZE = (250,250)
# img1 = Image.open('puppy1.jpg')
# img1.thumbnail(MAX_SIZE)
# img1.save('dog1small.jpg')
# ------------------------------------------
# import os
# from PIL import Image
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         file_name, extension = os.path.splitext(item)
#         Image.open(item).save(f'{file_name}.png')
# ------------------------------------------
# Sharpness
# Brightness
# Color
# Contrast
# Image blur # Gaussian blur
# ----------Sharpness
# from PIL import Image, ImageEnhance
# # 0 - blurry
# # 1 - original
# # 2 - sharpness increase
# img1 = Image.open('puppy1.jpg')
# enahncer = ImageEnhance.Sharpness(img1)
# enahncer.enhance(1).save('puppy2edited.jpg')
# ----------Brightness
# from PIL import Image, ImageEnhance
# # 0 - black
# # 1 - original
# # 2 - brightness increase
# img1 = Image.open('puppy1.jpg')
# enahncer = ImageEnhance.Brightness(img1)
# enahncer.enhance(1.5).save('puppy2edited.jpg')
# ----------Color
# from PIL import Image, ImageEnhance
# # 0 - black & white
# # 1 - original
# # 2 - color increase
# img1 = Image.open('puppy1.jpg')
# enahncer = ImageEnhance.Color(img1)
# enahncer.enhance(2).save('puppy2edited.jpg')
# ----------Contrast
# from PIL import Image, ImageEnhance
# # 0 - not visible
# # 1 - original
# # 2 - contrast increase
# img1 = Image.open('puppy1.jpg')
# enahncer = ImageEnhance.Contrast(img1)
# enahncer.enhance(1.5).save('puppy2edited.jpg')
# ----------Image blur # GaussianBlur
# from PIL import Image, ImageFilter
# img1 = Image.open('puppy3.jpg')
# img1.filter(ImageFilter.GaussianBlur(radius=4)).save('puppy3edited.jpg')
