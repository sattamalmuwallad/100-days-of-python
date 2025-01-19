from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # fixed so the range is in the list of image
print(dice_images[dice_num])
