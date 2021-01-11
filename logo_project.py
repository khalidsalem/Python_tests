from PIL import Image
import os

LOGO_NAME = input('lplz enter logo name and ext : ')
NEW_FOLDER_NAME = input('PLZ ENTER THE FOLDER NAME : ')

## logo info
logo_image = Image.open(LOGO_NAME)

logo_width , logo_height = logo_image.size

 ## create folder 
os.mkdir(NEW_FOLDER_NAME)

 ## logo over image
for filename in os.listdir('.'):
    if not (filename endswith('.png') or filename endswith('.jpg') or filename == LOGO_NAME)
        Continue
    img = Image.open(filename)
    width , height = img.size

    ## adding logo to the image
    img.paste(logo_image , (width-logo , height-logo) )

    img.safe(os.path.join(NEW_FOLDER_NAME , filename))
print('DONE') 


