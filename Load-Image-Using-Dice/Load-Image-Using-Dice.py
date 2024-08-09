from PIL import Image ,ImageStat 
import numpy as np
#Load image
#img = Image.open(".../Load-Image-Using-Dice/logo.png")

imageAddress = input("Enter address of the image that you want to processed with dice : ")

img = Image.open (imageAddress)
# Function to calculate darkness/lightness of an image
def calculateDarkness(image):
    # Convert image to grayscale for simplicity
    grayscale_image = image.convert("L")
    
    # Calculate the brightness statistics
    stat = ImageStat.Stat(grayscale_image)
    darkness = stat.mean[0]  # mean luminance value
    darknessLevel = (256-darkness)/ (256 / 5) + 1 
    return int(darknessLevel)

def load_tiles(folder):
    tiles = {}
    for i in range(1,7):  # فرض کنید شما 3 تصویر کوچک دارید
        tiles[i] = Image.open(f"{folder}/{i}.png")
    return tiles

def load_map(file_path):
    with open(file_path, "r") as f:
        map_data = [list(map(int, line.strip().split())) for line in f]
    return np.array(map_data)

def create_image(map_data, tiles, tile_size):
    rows, cols = map_data.shape
    new_image = Image.new('RGB', (cols * tile_size, rows * tile_size))

    for row in range(rows):
        for col in range(cols):
            tile_index = map_data[row, col]
            tile_image = tiles[tile_index]
            new_image.paste(tile_image, (col * tile_size, row * tile_size))

    return new_image




# Define the size of each considered square (e.g., 10x10 pixels)
squareSize = 10

# Get the image dimensions
width, height = img.size

file = open('.../Load-Image-Using-Dice/mapData.txt', 'w')

for top in range(0,width,squareSize):
    for left in range(0,height,squareSize):
        right = left + squareSize
        bottom = top + squareSize
        cosideredImage = (left, top, right, bottom)
        # Crop the considered image as cropedImage
        cropedImage = img.crop(cosideredImage)
        darknessLevel = calculateDarkness(cropedImage)
        
        with open('.../Load-Image-Using-Dice/mapData.txt', 'a') as file:
            file.write(str(darknessLevel))
            file.write(' ')
       # print(darknessLevel, end=',')
    with open('.../Load-Image-Using-Dice/mapData.txt', 'a') as file:
            file.write('\n')



tile_size = 60 

# بارگذاری تصاویر کوچک و نقشه اعداد
tiles = load_tiles(".../Load-Image-Using-Dice/Tiles") 

map_data = load_map(".../Load-Image-Using-Dice/mapData.txt")

# ایجاد و ذخیره تصویر جدید
new_image = create_image(map_data, tiles, tile_size)
new_image.save(".../Load-Image-Using-Dice/new_image.jpg")
new_image.show()