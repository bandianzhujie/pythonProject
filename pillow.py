from PIL import Image, ImageFilter


kitten = Image.open("C:/Users/Public/Pictures/Sample Pictures/kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("C:/Users/Public/Pictures/Sample Pictures/kitten_burred.jpg")
blurryKitten.show()