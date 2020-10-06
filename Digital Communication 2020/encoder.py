import helpers
import numpy as np
from scipy.linalg import hadamard




#returns a list of characters from a given textfile
def read_text_file(filename):
    f = open(filename, 'r')
    chars = []
    while(True):
        c = f.read(1)
        if(not c):
            break
        chars.append(c)

    return chars

def chars_to_bits_partial(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result



# Transform 8 bit message into base 10 
def to_base10(message):
    c = ''
    for m in message:
        c = c +str(m)        
    return(int(c,2))



input = "input.txt"

# Returns a list of characters from a given textfile
text = read_text_file(input)

# Convert text to binary
text_binary = chars_to_bits_partial(text)

# Divide our 640 bits message into 64 chunks of size 10 
chunks = []
for i in range(0,len(text_binary),10):
    chunks.append(text_binary[i:i+10])
    
    
# Construct Hadamard Matrix
hadam = hadamard(512)


# Convert our chunks to a base 10 representation
base10_chunks = []
for chunk in chunks:
    base10_repr = to_base10(chunk)
    base10_chunks.append(base10_repr)

# Create message according to hadamard matrix
encoded_message = []
for c in base10_chunks:
    if c < 512:
        encoded_message.append(hadam[c])
    else :
        encoded_message.append(-hadam[c-512])
        
    
encoded_message_flat = [item for sublist in encoded_message for item in sublist]

np.savetxt("encoded.txt",encoded_message_flat,fmt='%i')