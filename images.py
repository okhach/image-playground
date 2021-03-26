from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
converted_img = img.convert('L')

converted_img.save("grey.png", "png")
