from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')


box = (100, 100, 200, 200)
region = img.crop(box)


region.save("region.png", 'png')

