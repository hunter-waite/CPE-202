from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance
        self.word_list = []

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            infile = open(filename,'r')
        except:
            raise FileNotFoundError
        self.stop_table = HashTable(191)
        s = []
        string = ''
        for char in infile.read():
            if not ord(char) == 10:
                string = string + char
            else:
                s.append(string)
                string = ''
        s.append(string)
        for word in s:
            self.stop_table.insert(word,0)
        infile.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        try:
            infile = open(filename,'r')
        except:
            raise FileNotFoundError
        filter = []
        s = []
        string = ''
        line_num = 1
        for char in infile.read():
            if not ord(char) == 10 and not ord(char) == 32 and not ord(char) == 45:
                if char.isalpha():
                    string = string + char
            else:
                string = string.lower()
                if not self.stop_table.in_table(string) and not string == '':
                    string = string.lower()
                    s.append([string,line_num])
                string = ''
            if ord(char) == 10:
                line_num += 1
        string = string.lower()
        if not string == '' and not self.stop_table.in_table(string):
            s.append([string,line_num])

        for i in range(len(s)):
            self.concordance_table.insert(s[i][0],s[i][1])

        for x in range(len(self.concordance_table.hash_table)):
            if not self.concordance_table.hash_table[x] == None:
                self.word_list.append(self.concordance_table.hash_table[x])
        infile.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        outfile = open(filename,'w')
        self.word_list = sorted(self.word_list, key = lambda word: word[0])
        for i in range(len(self.word_list)):
            write_string = ''
            for j in range(1,len((self.word_list[i]))):
                if not str(self.word_list[i][j]) in write_string:
                    write_string = write_string + ' ' + str(self.word_list[i][j])
            if not i == len(self.word_list)-1:
                outfile.write('{}:{}\n'.format(self.word_list[i][0],write_string))
            else:
                outfile.write('{}:{}'.format(self.word_list[i][0],write_string))
        outfile.close()
