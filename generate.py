from PIL import Image, ImageFont, ImageDraw

img = Image.open("src/template.jpg")
#open the image as the object img
draw = ImageDraw.Draw(img)
#create object draw, whose member function will be used to draw the actual text

fontsize = 100
selected_font = ImageFont.truetype("src/CaviarDreams.ttf", fontsize)
width, height = img.size
x_begin, y_begin = width/10, height/5       #need a bit more space vertically to account for header.

print("Enter the text which you want to be input - ")
input_text = input()
draw.text(
            (x_begin, y_begin),         #beginning coordinates
            input_text,                 #input text
            (218, 243, 239),            #rgb values for text colour
            font = selected_font        #font selection
        )
img.save("output.jpg")
