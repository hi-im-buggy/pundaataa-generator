from PIL import Image, ImageFont, ImageDraw
from textwrap import TextWrapper
from operator import itemgetter

char_width = 30                 #the number of characters allowed per line
fontsize = 70
text_box_height = 0
text_box_width = 0

img = Image.open("src/template.jpg")
#open the image as the object img
draw = ImageDraw.Draw(img)
#create object draw, whose member function will be used to draw the actual text
width, height = img.size
x_begin, y_begin = width/2 , height/2     #need a bit more space vertically to account for header.

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

#increase the font size till width is maximised
while text_box_width < 0.8 * width:
    fontsize += 2
    selected_font = ImageFont.truetype("src/CaviarDreams.ttf", fontsize)
    for line in wrapped_lines:
        line_size_list.append( selected_font.getsize(line) )   
    text_box_width = max(line_size_list, key = itemgetter(0))[0]       

for line in line_size_list:                 #text box height will simply be the sum of the heights of the rendered lines
    text_box_height += line[1]

#Now the text box width has been maximised, but the text box height may still be too much
if len(wrapped_lines) > 1:
    while text_box_height > 0.6 * height:
        fontsize -= 2
        selected_font = ImageFont.truetype("src/CaviarDreams.ttf", fontsize)
        line_size_list.clear()
        for line in wrapped_lines:
            line_size_list.append( selected_font.getsize(line) )   
        text_box_width = max(line_size_list, key = itemgetter(0))[0]       
        #we reduce the font size, and then get the text box width with the new font size
        #then we maximise the text box width again, this time by increasing number of characters per line instead
        while text_box_width < 0.8 * width:
            char_width += 10
            wrapper.width = char_width
            wrapped_lines = wrapper.wrap(input_text)
            line_size_list.clear()
            for line in wrapped_lines:
                line_size_list.append( selected_font.getsize(line) )
            text_box_width = max(line_size_list, key = itemgetter(0))[0]       
        text_box_height = 0
        for line in line_size_list:                 #text box height will simply be the sum of the heights of the rendered lines
            text_box_height += line[1]
                
#Get the final updates text box dimensions so as to calculate coordinates for centering
#but it doesn't fucking work for long paragraphs and just prints off center so fuck me right?
wrapped_lines = wrapper.wrap(input_text)
line_size_list.clear()
for line in wrapped_lines:
    line_size_list.append( selected_font.getsize(line) )
text_box_width = max(line_size_list, key = itemgetter(0))[0]       
text_box_height = 0
for line in line_size_list:                 #text box height will simply be the sum of the heights of the rendered lines
    text_box_height += line[1]
     
#Offset the x and y beginning coordinates to center the text
x_begin -= (text_box_width/2)
y_begin -= (text_box_height/2)
#There's some sort of bullshit problem going on with text_box_height variable, really short input text, it gives me a huge offset,
#and makes the whole text disappear off of the face of the image.
draw.text(
            (x_begin, y_begin),         #beginning coordinates
            formatted_text,             #input text
            (218, 243, 239),            #RGB values for text colour
            font = selected_font        #font selection
        )
img.save("output.jpg")
