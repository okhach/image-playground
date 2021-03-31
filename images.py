from PIL import Image, ImageFilter

img  = Image.open('./spacex.jpg')

img.thumbnail((400, 400))

img.save("newSpacex01.jpg")
