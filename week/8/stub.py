#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

index = 0 
offset = 8
# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[index:offset])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

index = offset
offset = offset + 16
tstamp, author, sec_count = struct.unpack("<L8sL", data[index:offset])

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.datetime.fromtimestamp(tstamp).strftime('%Y-%m-%d %H:%M:%S'))
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % int(sec_count))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

index = offset
offset = index + 8



def process_png(start,end,name):
    with open(name,"wb") as f:
        f.write(b'\211PNG\r\n\032\n')
        f.write(data[start:end])

def process_word_sections(start,end,word_size):
    words =[]
    for index in range(0, len(data[start:end])//word_size):
        words.append(data[index*word_size: (index+1)*word_size])
    print(words)


count = 1
while(index < len(data)):

    sec_type, sec_len = struct.unpack("<LL",data[index:offset])
    
    start = offset
    end = offset + sec_len

    print("Section %d"%(count))
    if sec_type == 1:
        print("PNG")
        process_png(start,end,("output"+str(count)))
    elif sec_type == 2:
        print("DWORDS")
        process_word_sections(start,end,8)
    elif sec_type == 3:
        print("UTF8")
        print(struct.unpack(str(sec_len) + "s", data[start:end]))
    elif sec_type == 4:
        print("DOUBLES")
        print(struct.unpack(str(sec_len)+"s", data[start:end]))
    elif sec_type == 5:
        print("WORDS")
        process_word_sections(start,end,4)
    elif sec_type == 6:
        print("COORD")
        lat,lon = struct.unpack("<dd", data[start:end])
        print("lat: %s long: %s" %(str(lat), str(lon)))
    elif sec_type == 7:
        print("REFERENCE")
        print("%d" %(struct.unpack("<L", data[start:end])))
    elif sec_type == 9:
        print("ASCII")
        print(data[start:end])
    else:
        print("Error")

    index = end
    offset = index + 8
    count = count + 1