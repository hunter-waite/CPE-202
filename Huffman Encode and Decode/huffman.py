class HuffmanNode:
    # added a code to the init to help with creating a list of codes
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        self.code = ''

    #tests whether or not the node is a leaf
    def is_leaf(self):
        if self.right == None and self.left == None:
            return True
        return False

#a global variable for the list of codes (useful in recursive functions don't @ me)
list_of_codes = ['']*256

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file"""
    freqList = [0]*256
    try:
        file = open(filename,'r')
    except:
        raise FileNotFoundError
    #adds one to the frequency of every character based on ascii table
    for char in file.read():
        freqList[ord(char)] = freqList[ord(char)]+1
    file.close()
    return freqList

def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    node_list = []
    #takes the character frequencies and makes nodes out of all the ones that
    #aren't a frequency of 0 then adds them to the list
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            tHuffNode = HuffmanNode(i,char_freq[i])
            node_list.append(tHuffNode)
    #sorts the node list first based on frequency and if the frequencties are the
    #same based on the the ord of the character in the ascii table
    node_list.sort(key=lambda huffnode:(int(huffnode.freq),int(huffnode.char)))
    #loops through the created list of nodes in order to buid a huffman tree
    while len(node_list) > 1:
        #removes the first two nodes in the list
        x = node_list.pop(0)
        y = node_list.pop(0)
        parent_char = min(x.char,y.char)
        #creates a node with the lesser character as the new character and
        # the frequency as the two odl freqs added together
        new_node = HuffmanNode(parent_char,(x.freq+y.freq))
        #sets the node's left and right to the proper node from before hand
        new_node.left = x
        new_node.right = y
        #count = 0
        #appends the new node to the list then sorts that bih
        node_list.append(new_node)
        node_list.sort(key=lambda huffnode:(int(huffnode.freq),int(huffnode.char)))
    return node_list[0]

def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    #calls the recursive create code function in order to create a list of codes
    #then returns the global variable
    global list_of_codes
    _create_code(node,'')
    return list_of_codes

def _create_code(node,code):
    #recrsively goes through the entire tree creating a code for the leaves
    #then adds it to the list of codes at the right location to be accessed later
    global list_of_codes
    if not node.is_leaf():
        _create_code(node.left,code+'0')
        _create_code(node.right,code+'1')
    else:
        list_of_codes[node.char] = code

def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    retStr = ''
    for i in range(len(freqs)):
        if not freqs[i] == 0:
            #creates the header by adding the ascii table value and the frequency
            #to the end of the header
            retStr = '{} {} {}'.format(retStr,str(i),str(freqs[i]))
    retStr = retStr[1:len(retStr)]
    return retStr

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    #uses all the functions that I have created to generate a huffman code
    # and write it out to a file
    try:
        infile = open(in_file,'r')
    except:
        raise FileNotFoundError
    s = infile.read()
    if len(s) == 0:
        outfile = open(out_file,'w')
        outfile.close()
    else:
        freq_list = cnt_freq(in_file)
        header = create_header(freq_list)
        outfile = open(out_file,'w')
        outfile.write(header)
        huff_tree = create_huff_tree(freq_list)
        code_list = create_code(huff_tree)
        #loops through all the letters in the text file and writes the correct code
        #to the file
        first = True
        for c in s:
            for i in range(len(list_of_codes)):
                if i == ord(c):
                    if not list_of_codes[i] == '' and first:
                        first = False
                        outfile.write('\n')
                    outfile.write(list_of_codes[i])
                    break
    outfile.close()
    infile.close()

def huffman_decode(encoded_file,decode_file):
    '''Takes in two files [0] is the encoded huffman file with the header that is
    going to be converted and [1] is the file that the decode will be written too'''
    try:
        infile = open(encoded_file,'r')
    except:
        raise FileNotFoundError
    o = open(decode_file,'w')
    s = ''
    for line in infile:
        s = line
        break
    freq_list = parse_header(s)
    huff_tree = create_huff_tree(freq_list)
    for line in infile:
        f = line
    curr_node = huff_tree
    i = 0
    while(i<len(f)):
        if curr_node.right == None and curr_node.left == None:
            o.write(chr(curr_node.char))
            curr_node = huff_tree
        elif f[i] == '0':
            curr_node = curr_node.left
            i+=1
        else:
            i+=1
            curr_node = curr_node.right
    o.write(chr(curr_node.char))
    o.close()
    infile.close()
def parse_header(header_string):
    freq_list = [0]*256
    l = []
    l = header_string.split(' ')
    for i in range(len(l)):
        if i % 2 == 0:
            freq_list[int(l[i])] = int(l[i+1])
    return freq_list
