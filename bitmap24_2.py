# create BMP file 912x1140  1:2:1
import os
os.chdir("c:\\user")            # change working directory
fout=open("vline2inv.bmp","wb")      # open output file as binary file

# File header 14byte
h1 = bytearray([0x42, 0x4d])                # BM    
h2 = bytearray([0xf6, 0x97, 0x2f, 0x00])    # File size
h3 = bytearray([0x00, 0x00, 0x00, 0x00])    # reserved
h4 = bytearray([0x36, 0x00, 0x00, 0x00])    # offset to Image
fout.write(h1)
fout.write(h2)
fout.write(h3)
fout.write(h4)

# BMP Info header  40byte
b1 = bytearray([0x28, 0x00, 0x00, 0x00])    # Info header size
b2 = bytearray([0x90, 0x03, 0x00, 0x00])    # H width 912
b3 = bytearray([0x74, 0x04, 0x00, 0x00])    # V width 1140
b4 = bytearray([0x01, 0x00])    # plane
b5 = bytearray([0x18, 0x00])    # bit size/pixel
b6 = bytearray([0x00, 0x00, 0x00, 0x00])    # no RLE
b7 = bytearray([0xc0, 0x97, 0x2f, 0x00])    # Data size(byte)
b8 = bytearray([0x13, 0x0b, 0x00, 0x00])    # H dot/m
b9 = bytearray([0x13, 0x0b, 0x00, 0x00])    # V dot/m
ba = bytearray([0x00, 0x00, 0x00, 0x00])    # 0x00
bb = bytearray([0x00, 0x00, 0x00, 0x00])    # 0x00
fout.write(b1)
fout.write(b2)
fout.write(b3)
fout.write(b4)
fout.write(b5)
fout.write(b6)
fout.write(b7)
fout.write(b8)
fout.write(b9)
fout.write(ba)
fout.write(bb)

# Image generation
Hsize = 912
Vlize = 1140
Bpixel = bytearray([0x00, 0x00, 0x00])
Wpixel = bytearray([0xff, 0xff, 0xff])

for L in range(0, 1140):    # 1140 lines
    for i in range(0, 228):	# white
        fout.write(Wpixel)
    for i in range(0, 456): # black
        fout.write(Bpixel)
    for i in range(0, 228):	# white
        fout.write(Wpixel)

fout.close()

