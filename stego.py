#! /usr/bin/python
 
"""
By: Nicole Shadowen
October 28, 2015
 
Program to read in img file (img1.png) & secret message (msg.txt) to create new altered img file (img2.png) with stenography applied to RGB codes in image, conveying a secret message.  Begin at start of img RGB codes and convert until end of binary phrase length.  Odd RG or B code = 1 in binary, even = 0. 
"""
 
 
#program to return ith bit of message:
 
def getbit(message,i): 
    byte = i/8
    bit = i%8
    ithbyte = '0'+bin(ord(message[byte]))[2:]
    while len(ithbyte) != 8:
        ithbyte = '0'+ithbyte
    #print bit, len(ithbyte),ithbyte
    return ithbyte[bit]
 
 
#read in msg.txt file:
 
infile = open("msg.txt")
hiddenphrase = infile.read()
def msg2bin(string):
    return "".join(getbit(string,i) for i in range(8*len(string)))
 
binaryhiddenphrase = msg2bin(hiddenphrase + "*")
#indexphrase = len(hiddenphrase)
#indexbinaryphrase = len(binaryhiddenphrase)
 
 
#read in img1.png file RGB codes to the end length of given phrase (found in msg.txt): 
 
import png
initialfile = png.Reader("img1.png")
firstimage = initialfile.read_flat()
 
actual_pixels = firstimage[2]
 
 
#compare actual_pixels RGB values of img1.png with binaryhiddenphrase values, change when 0 != even
 
new_pixels = actual_pixels[:]
for i in range(len(binaryhiddenphrase)):
    if actual_pixels[i]%2==0 and binaryhiddenphrase[i] == "0":
        new_pixels[i] = (actual_pixels[i])
    elif actual_pixels[i]%2==0 and binaryhiddenphrase[i]=="1":
        new_pixels[i] = (actual_pixels[i]+1)
    elif actual_pixels[i]%2==1 and binaryhiddenphrase[i]=="1":
        new_pixels[i] = (actual_pixels[i])
    elif actual_pixels[i]%2==1 and binaryhiddenphrase[i]=="0":
        new_pixels[i] = (actual_pixels[i]-1)
 
print actual_pixels[:15]
print binaryhiddenphrase[:15]
print new_pixels[:15]
 
 
#deposit new_pixels into new file img2.png
 
w = png.Writer(firstimage[0],firstimage[1], colormap=new_pixels)
f = open("img2.png","wb")
w.write_array(f,new_pixels)