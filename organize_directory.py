import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))
## organize images into images folder
for filename in os.listdir(current_dir):
    ##print(filename)
    if filename.endswith((".PNG" , ".png", ".jpeg", ".GIF", ".jpg")):
        ##if not os.path.exists("images"):
          ##os.mkdir('images')
          shutil.copy(filename , "images")
          os.remove(filename)
          print("images are done")

## organize docs into docs folder
    if filename.endswith((".pdf" , ".xlsx", ".txt")):
        ##if not os.path.exists("docs"):
          ##os.mkdir('docs')
          shutil.copy(filename , "docs")
          os.remove(filename)
          print("docs are done")

##organize code into code folder
    if filename.endswith((".css" , ".js", ".html" ,  ".py")):
        ##if not os.path.exists("code"):
          ##os.mkdir('code')
          shutil.copy(filename , "code")
          os.remove(filename)
          print("codes are done")          
