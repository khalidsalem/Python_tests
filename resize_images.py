
import os
from PIL import image

fit_size = int(input("enter size : "))
output_folder = input("enteroutput folder name: ")

if not os.path.exists(output_folder):
    os.mkdir("output_folder")

for file_name in os.listdir('.'):
    if not filename.endswith((".PNG " ,".png" , ".jpeg" , ".jpg")):
        continue
    ## open image -----> get image size -----------> resize

    image = image.open (filename)
    width , height = image.size

    if width > fit_size and height > fit_size :   ## image shd be greater than fit size or value

        if width > fit_size :
            height = int((fit_size / width) * height)
            width = fit_size

        else: 
            width  = int((fit_size / height) * width)
            height = fit_size

    image = image.resize((width , height))
    print ('resizing : %s'  %(filename))
image = image.save(os.path.join(output_folder , filename)  ## when u save the image, u need to sae it with the full path and the filename.
 

## print('-------------')


## print ("DOOONNNEEE") 