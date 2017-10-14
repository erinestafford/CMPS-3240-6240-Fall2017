
# coding: utf-8

# In[48]:

from PIL import Image


# In[49]:

def convert_rgb_hsl(r,g,b):
    R = r / 255
    G = g / 255
    B = b / 255
    minimum = min([R,G,B])
    maximum = max([R,G,B])
    l = ((minimum+maximum)/2)*100
    if l>50:
        s = ((maximum-minimum)/(2.0-maximum-minimum))*100
    else:
        s = ((maximum-minimum)/(maximum+minimum))*100

    if maximum == R:
        h = ((G-B)/(maximum-minimum))*60
    elif maximum == G:
        h = (2.0 + ((B-R)/(maximum-minimum)))*60
    else:
        h = (4.0 + ((R-G)/(maximum-minimum)))*60
    return (h,s,l)


# In[70]:

def Read_Image(filename):
    pngfile = Image.open(filename)
    im = Image.open(filename)
    #im.show() 
    pixel_values = list(im.getdata())
    dict_colors = {}
    for pixel in pixel_values:
        if pixel not in dict_colors:
            dict_colors[pixel] = 1
        else:
            dict_colors[pixel] += 1
    blue_red = [0,0] #store number of blues (0) and reds (1)
    for key in dict_colors.keys():
        if dict_colors[key] > 10 and key != (255,255,255,255) and key != (0,0,0,255) and key[0]!=key[1]!=key[2]:
            (h,s,l) = convert_rgb_hsl(key[0], key[1], key[2])
            if h>(170) and h<(300):#color is blue
                blue_red[0] +=1
            else:#color is red
                blue_red[1] +=1
    return blue_red
        


# In[77]:

def getFeatures(file_list):
    feature_list =[[]]*len(file_list)
    counter = 0
    for file in file_list:
        example = Read_Image(file)
        feature_list[counter]=example
        counter+=1
    return feature_list


# In[78]:

file_list = ['testData.png','testData2.png']
getFeatures(file_list)


# In[ ]:



