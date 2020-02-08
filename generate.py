from PIL import Image, ImageFont, ImageDraw
from textwrap import TextWrapper
from operator import itemgetter

img = Image.open("src/template.jpg")
#open the image as the object img
draw = ImageDraw.Draw(img)
#create object draw, whose member function will be used to draw the actual text
width, height = img.size
x_begin, y_begin = width/2 , (height/2 + 30)     #need a bit more space vertically to account for header.

char_width = 22                             #the number of characters allowed per line
fontsize = 100
text_box_height = 0
text_box_width = 0

wrapper = TextWrapper(width = char_width)
selected_font = ImageFont.truetype("src/CaviarDreams.ttf", fontsize)

print("Enter the text which you want to be input - ")
input_text = input()

wrapped_lines = wrapper.wrap(input_text)            #lines wrapped and separated, and put into a list
formatted_text = wrapper.fill(input_text)           #lines wrapped and concatenated into a single string with newline characters
line_size_list = []

for line in wrapped_lines:
    line_size_list.append( selected_font.getsize(line) )   #initialize a list of sizes for the rendered lines in our selected font

text_box_width = max(line_size_list, key = itemgetter(0))[0]       #return the max width of rendered line i.e. the text box width

for line in line_size_list:                 #text box height will simply be the sum of the heights of the rendered lines
    text_box_height += line[1]

x_begin -= (text_box_width/2)
y_begin -= (text_box_height/2)

draw.text(
            (x_begin, y_begin),         #beginning coordinates
            formatted_text,             #input text
            (218, 243, 239),            #rgb values for text colour
            font = selected_font        #font selection
        )
img.save("output.jpg")
