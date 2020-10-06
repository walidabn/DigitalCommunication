import random



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


#Changes a list of 0,1 to a list of -1,1
def from_zero_to_neg(l):
    res = []
    res.extend(l)
    for i in range(len(l)):
        if res[i]==0:
            res[i]=-1
    return res
    

# changes list of characters to 1 and -1(instead of 0)
def chars_to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    for i in range(len(result)):
        if result[i] == 0 :
            result[i] = -1
    return result

#Changes list of bits +1,-1 to +1,0
def bits_to_chars(bits):
    chars = []
    chars.extend(bits)
    for i in range(len(chars)):
        if chars[i]== -1 :
            chars[i]=0
    return chars




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
    text_file = open("output_test.txt","w")
    n = text_file.write(string)
    text_file.close()
    


    
    
    

# creates a list of characters out of a given list and a k parameter on input, such that every character of input list is repeated k times.
def repetition_code(code, k):
    repeated = [[x] * k for x in code]
    flattened = [item for sublist in repeated for item in sublist]
    
    return flattened

#Cette méthode permet de faire un code de répétition sur les bits de message par k, et sur les bits de parité par parity_repeat
def repetition_hybrid(code, k,batch_size,parity_repeat):
    res = []
    for i in range(len(code)):
        if ((i% (batch_size+2)) != batch_size) and ((i% (batch_size+2)) != batch_size + 1)  : 
            repeated_char = [code[i]]*k
        else :
            repeated_char = [code[i]]*parity_repeat
        res.append(repeated_char)
    flattened = [item for sublist in res for item in sublist]
    return flattened

#Compute the hamming distance between two lists of same size, and returns the errors and indices of errors 
def compute_Hamming(l1,l2):
    assert(len(l1)==len(l2))
    count = 0
    errors = []
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            count +=1
            errors.append((i,l1[i]))
    return count,errors
        
#L'objectif, c'est qu'on donne une liste de taille batch_size à cette méthode
# Elle va compter le nombre de 1 dans la liste, si le nombre est pair, elle retourne -1, sinon elle retourne 1    
def parity_find(l):
    acc = 0
    for i in range(len(l)):
        if(i==4 or i==0 or i==2  or i==5 or i == 6 or i == 7 ):
            if l[i]==1:
                acc += 1
    mod = acc % 2
    if mod == 0 :
        return -1 
    else : 
        return 1
            
        
def parity_find_2(l):
    acc = 0
    for i in range(len(l)):
        if(i%2 ==0):
            if l[i]==1:
                acc += 1
    mod = acc % 2
    if mod == 0 :
        return -1 
    else : 
        return 1
    
def parity_find_3(l):
    acc = 0
    for i in range(len(l)):
        if(i==0 or i==1 or i==3  or i==5 or i == 6 or i == 7 ):
            if l[i]==1:
                acc += 1
    mod = acc % 2
    if mod == 0 :
        return -1 
    else : 
        return 1
    
    
#Given a list h, retrieves index i of h such that abs(h[i]) is minimal, and returns index i
def find_absolute_min_index(h):
    minimum = 10000000000
    min_index=0
    for i in range(len(h)):
        if abs(h[i]) < minimum :
            minimum = abs(h[i])
            min_index = i
    return min_index
    
def find_absolute_min_index_2(h):
    minimum = 10000000000
    min_index= 0
    min_index_2 = 0
    for i in range(len(h)):
        if abs(h[i]) < minimum :
            minimum = abs(h[i])
            min_index = i
    minimum = 10000000000        
    for i in range(len(h)):
        if (abs(h[i]) < minimum) and (i!=min_index) :
            minimum = abs(h[i])
            min_index_2 = i
            
    return min_index_2

    

# Generates a random list of size k, such that: 
#     composed of 1s if choice = 1 
#     composed of -1s if choice = -1 
#     composed of 1s and -1s if choice = 0
def generate_random_list(choice, k):
    if choice == -1: # Generating random list of -1 of size k
        input_list = [-1] * k
    elif choice == 1: # Generating random list of 1 of size k
        input_list = [1] * k
    elif choice == 0:  # Generating random list of -1 and 1 of size k
        input_list = []
        for i in range(0,k):
            n = random.choice([-1,1])
            input_list.append(n)
    else : return 'Sorry incorrect input, try again !'
    
    return input_list


# Transform 8 bit message into base 10 
def to_base10(message):
    c = ''
    for m in message:
        c = c +str(m)        
    return(int(c,2))

# Transform 8 bit message into base 10 
def to_binary(message):
    return int(bin(message)[2:])

#Given a list h, retrieves index i of h such that abs(h[i]) is minimal, and returns index i
def get_max_index(h):
    maximum = -10000000000
    max_index=0
    for i in range(len(h)):
        if abs(h[i]) > maximum :
            maximum = abs(h[i])
            max_index = i
    return max_index