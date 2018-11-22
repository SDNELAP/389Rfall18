#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct
import binascii

# TODO: Potential improvements
# - Prompt user for message/malicious
# - Improved parsing now that we know the format
# - Break on correct answer

#####################################
### STEP 1: Calculate forged hash ###
#####################################
message = 'Hello there'
malicious = 'Hacking is life' # put your malicious message here

# Connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('142.93.118.186', 1234))

# Get first Notary Prompt
res = s.recv(1024)

# Respond to Notary Option Menu
s.send('1\n')
s.recv(1024)

# Sign the message and recieve hash data

s.send(message + '\n')
response = s.recv(1024)

# Parse and print hash
legit = response.split(' ')[-1]
print 'Actual hash:',legit,'\n'

fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.strip().decode('hex'))

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print 'Fake hash:',fake_hash,'\n'

#############################
### STEP 2: Craft payload ###
#############################

# Read next set of data
s.recv(1024)

for i in range(6, 16):
    # Padding has a total of 64 bytes
    # 8 bytes are dedicated to size encoding in little endian
    # \x80 is one original byte
    # the remainder of the size of the padding is determined by length of the original message and the size of secret
    # Overall padding size = 64 - 8 - 1 - len(message) - i
    padding = '\x80' 
    padding_size = 64 - 8 - 1 - len(message) - i
    
    padding += ('\x00') * padding_size # Duplicate 0 padding_size times and append to padding

    # Format length of secret + message in little endian
    length = struct.pack('<Q', (i + len(message)) * 8)

    # Construct payload
    payload = message + padding + length + malicious

    # Respond to Notary Option Menu
    s.send('2\n')
    print s.recv(1024)

    # Pass the fake hash to the Notary 
    s.send(fake_hash + '\n')
    print s.recv(1024)

    # Send the payload to the Notary
    s.send(payload + '\n')
    response = s.recv(1024)

    # Check for flag
    response = s.recv(1024)
    if 'CMSC389R' in response:
        print 'Flag is found\n'
        print response
        print binascii.hexlify(payload)
        break
    else:
       print 'Failed'

       
    