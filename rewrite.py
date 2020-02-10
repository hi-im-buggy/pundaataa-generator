from PIL import Image, ImageFont, ImageDraw
from textwrap import TextWrapper

#Initialising some variables
wrapper = TextWrapper(width = 30)
img = Image.open("src/template.jpg")
draw = ImageDraw.Draw(img)
selected_font = ImageFont.truetype("src/CaviarDreams.ttf", size = 10)

#Get the input text and wrap it 
print("Enter the text to be input - ")
input_text = input()
beautiful_text = wrapper.fill(input_text)

#Increase the font size till the text is just a little too wide
while selected_font.getsize_multiline(beautiful_text)[0] < (0.8 * img.size[0]):
    selected_font.size += 2

#If the text is too long, reduce the font size a little...
while selected_font.getsize_multiline(beautiful_text)[1] > (0.7 * img.size[1]):
    selected_font.size -= 2
    #..and then increase the number of characters per line till it's wide enough...
    while selected_font.getsize_multiline(beautiful_text)[0] < (0.8 * img.size[0]):
        wrapper.width += 2
        beautiful_text = wrapper.fill(input_text)
    #...rewrap the text, test again, and keep repeating till it sits well

#Position the x and y coordinates to draw the text so as to have it centered
x_begin, y_begin = img.size[0]/2 , img.size[1]/2
x_begin -= selected_font.getsize_multiline(beautiful_text)[0]/2
y_begin -= selected_font.getsize_multiline(beautiful_text)[1]/2

draw.text(
            (x_begin, y_begin),        
            beautiful_text,             
            (218, 243, 239),          
            font = selected_font     
        )
img.save("output.jpg")
