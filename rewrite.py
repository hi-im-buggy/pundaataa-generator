#!/usr/bin/env python3
from PIL import Image, ImageFont, ImageDraw
from textwrap import TextWrapper

#Initialising some variables
wrapper = TextWrapper(width = 20)
img = Image.open("src/template.jpg")
draw = ImageDraw.Draw(img)
fontsize = 10
max_fontsize = 512
selected_font = ImageFont.truetype("src/CaviarDreams.ttf", size = fontsize)
text_box_width, text_box_height = 0, 0

#Get the input text and wrap it 
print("Enter the text to be input - ")
input_text = input().strip()
beautiful_text = wrapper.fill(input_text)

####################################################################################################
#In the following code, note that wrapper.width is a mutable attribute of the object wrapper, whereas
#selected_font.size is NOT mutable, it can only return the current size. 
#Thus, the font has to be reconstructed with a new size each time.
####################################################################################################

#Increase the font size till the text is just a little too wide and fontsize <= max_fontsize
while selected_font.getsize_multiline(beautiful_text)[0] < (0.8 * img.size[0]) \
        and fontsize <= max_fontsize:
    fontsize += 2
    selected_font = ImageFont.truetype("src/CaviarDreams.ttf", size = fontsize)

#If the text is too long, reduce the font size a little...
while selected_font.getsize_multiline(beautiful_text)[1] > (0.7 * img.size[1]):
    fontsize -= 2
    selected_font = ImageFont.truetype("src/CaviarDreams.ttf", size = fontsize)
    #..and then increase the number of characters per line till it's wide enough...
    while selected_font.getsize_multiline(beautiful_text)[0] < (0.8 * img.size[0]):
        wrapper.width += 2
        beautiful_text = wrapper.fill(input_text)
    #...rewrap the text, test again, and keep repeating till it sits well

#Position the x and y coordinates to draw the text so as to have it centered
x_begin, y_begin = img.size[0]/2 , img.size[1]/1.85
x_begin -= selected_font.getsize_multiline(beautiful_text)[0]/2
y_begin -= selected_font.getsize_multiline(beautiful_text)[1]/2

#Finally, draw the text to the template
draw.text(
            (x_begin, y_begin),        
            beautiful_text,             
            (218, 243, 239),        #RGB values for the text color
            font = selected_font     
        )
img.save("output.jpg")
