
from PIL import Image, ImageFilter
kitten = Image.open("sohye.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("sohyeBlurry.jpg")
blurryKitten.show()