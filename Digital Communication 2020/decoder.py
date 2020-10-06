import helpers
import numpy as np
from scipy.linalg import hadamard


#Converts a list of 0,1 bits into it's ascii chars representation
def from_bits_to_chars(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

#Writes a list of characters in the "output_text.txt" file
def write_chars_on_file(chars):
    string = str(chars)
    text_file = open("output.txt","w")
    n = text_file.write(string)
    text_file.close()
    
#Given a list h, retrieves index i of h such that abs(h[i]) is minimal, and returns index i
def get_max_index(h):
    maximum = -10000000000
    max_index=0
    for i in range(len(h)):
        if abs(h[i]) > maximum :
            maximum = abs(h[i])
            max_index = i
    return max_index
    



# Read output file
output = open('received.txt', 'r').read().splitlines()

# Convert output from char to float 
output = [float(i) for i in output]

output = np.asarray(output)

# Construct Hadamard Matrix
hadam = hadamard(512)

hadam = np.asarray(hadam)

# Divide our message into 64 chunks of size 512
output_chunks = []
for i in range(0,len(output),512):
    output_chunks.append(output[i:i+512])
    
output_chunks = np.asarray(output_chunks)

# Create U matrix for decoding
U = []
for c in output_chunks :
    U.append(np.matmul(hadam,c))
U = np.asarray(U)
    
    
# Get index of max of each line:
U_max_indices = []
for line in U:
    U_max_indices.append(get_max_index(line))
U_max_indices = np.asarray(U_max_indices)

# Decode 
U_max_indices_binary = []
for i in range(len(U_max_indices)):
    max_index = U_max_indices[i]
    if(U[i,max_index]<0):
        for c in "{0:010b}".format(max_index+512):
            U_max_indices_binary.append(int(c))
    else:
        for c in "{0:010b}".format(max_index):
                U_max_indices_binary.append(int(c))
             
res2 = from_bits_to_chars(U_max_indices_binary)
write_chars_on_file(res2)
        
        
