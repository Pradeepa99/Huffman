#!/usr/local/bin/python3
import sys
import argparse
import shutil
import heapq
import os

#Defining the attributes
class Declaration:

	def __init__(self, letter, count, L_node=None, R_node=None):
		self.char = letter
		self.key = count
		self.first_node = L_node
		self.second_node = R_node
		
	def __cmp__(self, other):
		if(other == None):
			return -1
		if(not isinstance(other, Declaration)):
			return -1
		return self.freq > other.freq	


class Huffman:

	def __init__(self):
		self.root = None
		self.word_list = []
		self.Nodes_list = []
		self.unique_dict = {}
		self.result_dict = {}

#Finding the unique character and its frequency

def find_letter_freq(self, words):
	frequency = {}
	for character in words:
		if not character in frequency:
			frequency[character] = 0
		frequency[character] += 1
	return frequency

#Creates a list containing nodes 

def create_heapnode(self,frequency):
	for key in frequency:
			node = Declaration(key, frequency[key])
			heapq.heappush(self.heap, node)

def add_new_node(self, addnode):
		for x, y in enumerate(self.Nodes_List):
			if addnode.key >= y.key:
				self.Nodes_list.insert(x, addnode)
			return

def create_huffman(self):
		
		self.create_node()
		if len(self.Nodes_List) == 1:
			self.root = self.Nodes_List[0]
			return

		while True:

			l = self.Nodes_List.pop(0)
			r = self.Nodes_List.pop(0)
			newNode = Declaration(None, l.key + r.key, l, r)
			self.add_new__node(newNode)

			if len(self.Nodes_List) == 2:
				break

		a = self.Nodes_List.pop(0)
		b = self.Nodes_List.pop(0)
		newNode = Declaration(None, a.key + b.key, a, b)
		self.root = newNode


def huff_char(self, character,present_char):
		
		if(character == None):
			return
		
		if(character.char != None):
			if len(self.nodeList) == 1:
				self.unique_dict[character.char] = '0'
				self.result_dict['0'] = character.char
			else:
				self.unique_dict[character.char] = present_char
				self.result_dict[present_char] = character.char
			return

		self.huff_char(character.left, present_char + '0')
		self.huff_char(character.right, present_char + '1')


def encode_function(self, text):
		q = self.find_letter_freq(text)
		self.create_huffman()
		encoded_text = ''
		for char in text:
			encoded_text += self.unique_list[char]
		return encoded_text

def decode_function(self, encoded_text):

		exist_node = ""
		decoded_text = ""
		with open('readfile', 'rb') as f: 
			self.result_dict = os.read.load(f)
		f.close()
		for bit in encoded_text:
			exist_node += bit
			if(exist_node in self.result_dict):
				char = self.result_dict[exist_node]
				decoded_text += char
				exist_node = ""
		return decoded_text



def encode(input_file, output_file):
	print("encoding ", input_file, output_file)
	# write code here

	# simply copying the file to bypass the actual test.
	# remove the below lines.
	if input_file != "" and output_file != "":
		shutil.copyfile(input_file, output_file)


def decode(input_file, output_file):
	print("decoding ", input_file, output_file)
	# write code here

	# simply copying the file to bypass the actual test.
	# remove the below lines.
	if input_file != "" and output_file != "":
		shutil.copyfile(input_file, output_file)


def get_options(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Huffman compression.")
	groups = parser.add_mutually_exclusive_group(required=True)
	groups.add_argument("-e", type=str, help="Encode files")
	groups.add_argument("-d", type=str, help="Decode files")
	parser.add_argument("-o", type=str, help="Write encoded/decoded file", required=True)
	options = parser.parse_args()
	return options


if __name__ == "__main__":
	options = get_options()
	if options.e is not None:
		encode(options.e, options.o)
	if options.d is not None:
		decode(options.d, options.o)
