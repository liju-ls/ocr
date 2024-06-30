from paddleocr import PaddleOCR
from ocr import ocrText
from crop import crop
import os
from colorama import Fore
import easyocr
from mtp import getImage

det_model = "ch_PP-OCRv4_det_server_infer/"
rec_model = "ch_PP-OCRv4_rec_server_infer/"

paddleModel = PaddleOCR(use_angle_cls=True, lang="en", ocr_version='PP-OCRv4', use_space_char=True) # need to run only once to download and load model into memory
reader = easyocr.Reader(['en'])


characters = []
wordsFounded = {"word1": [],
                "word2": [],
                "word3": [],
                "word4": [],
                "word5": [],
				"word6": []}

wordCount = 0

# for j in words:
# 	print(j)

# for i in puzzle:
# 	print(i)

def find_word (wordsearch, word):
	"""Trys to find word in wordsearch and prints result"""
	# Store first character positions in array
	start_pos = []
	first_char = word[0]
	for i in range(0, len(wordsearch)):
		for j in range(0, len(wordsearch[i])):
			if (wordsearch[i][j] == first_char):
				start_pos.append([i,j])
	# Check all starting positions for word
	for p in start_pos:
		if check_start(wordsearch, word, p):
			# Word found			
			return
	# Word not found
	print(f'Word Not Found : {word}')

def check_start (wordsearch, word, start_pos):
	"""Checks if the word starts at the startPos. Returns True if word found"""
	directions = [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]
	# Iterate through all directions and check each for the word
	for d in directions:
		if (check_dir(wordsearch, word, start_pos, d)):
			return True

def check_dir (wordsearch, word, start_pos, dir):
	"""Checks if the word is in a direction dir from the start_pos position in the wordsearch. Returns True and prints result if word found""";
	global wordCount
	found_chars = [word[0]] # Characters found in direction. Already found the first character
	current_pos = start_pos # Position we are looking at
	pos = [start_pos] # Positions we have looked at
	while (chars_match(found_chars, word)):
		if (len(found_chars) == len(word)):
  			# If found all characters and all characters found are correct, then word has been found
			print('')
			print(f'Word Found : {word}')
			print('')
			# Draw wordsearch on command line. Display found characters and '-' everywhere else
			for x in range(0, len(wordsearch)):
				line = ""
				for y in range(0, len(wordsearch[x])):
					is_pos = False
					for z in pos:
						if (z[0] == x) and (z[1] == y):
							is_pos = True
					if (is_pos):
						line = line + " " + wordsearch[x][y]
						wordsFounded[f"word{wordCount+1}"].append((x, y))
					else:
						line = line + " -"
				# print(line)
			print('')
			wordCount = wordCount + 1

			return True
		# Have not found enough letters so look at the next one
		current_pos = [current_pos[0] + dir[0], current_pos[1] + dir[1]]
		pos.append(current_pos)
		if (is_valid_index(wordsearch, current_pos[0], current_pos[1])):
			found_chars.append(wordsearch[current_pos[0]][current_pos[1]])
		else:
			
			return

def chars_match (found, word):
	"""Checks if the leters found are the start of the word we are looking for"""
	index = 0
	for i in found:
		if (i != word[index]):
			return False
		index += 1
	return True

def is_valid_index (wordsearch, line_num, col_num):
	"""Checks if the provided line number and column number are valid"""
	if ((line_num >= 0) and (line_num < len(wordsearch))):
		if ((col_num >= 0) and (col_num < len(wordsearch[line_num]))):
			return True
	return False

quit = False


while quit == False:
    wordCount = 0
    characters.clear()
    
    for i in range(6):
        wordsFounded[f"word{i+1}"].clear()
    
    indent = " "
    print("1. Quit")
    print("2. Run")
    print(" ")
    option = input(f"Option : ")
    print(" ")
    
    if option == "1":
        quit = True
    if option == "2":
        getImage()
        crop()
        out = ocrText(paddleModel, reader)
        puzzle = out[0]
        
        # if len(puzzle) > 9:
        #     puzzle.pop()
        
        # for i in puzzle:
            
        #     if len(i) == 8:
        #         if i[0] == "I":
        #             i.insert(0, "I")
        #         elif i[-1] == "I":
        #             i.insert(-1, "I")
            
        #     if len(i) > 9:
        #         i.pop()
        #     print(i)
        
        words = out[1]
        for i in range(6):
            find_word(puzzle, words[i])
        for i in range(len(puzzle)):
            line = ""
            for j in range(len(puzzle[i])):
                if (i, j) in wordsFounded["word1"]:
                    line += indent + f"{Fore.BLUE}{puzzle[i][j]}"
                elif (i, j) in wordsFounded["word2"]:
                    line += indent + f"{Fore.LIGHTBLACK_EX}{puzzle[i][j]}"
                elif (i, j) in wordsFounded["word3"]:
                    line += indent + f"{Fore.GREEN}{puzzle[i][j]}"
                elif (i, j) in wordsFounded["word4"]:
                    line += indent + f"{Fore.RED}{puzzle[i][j]}"
                elif (i, j) in wordsFounded["word5"]:
                    line += indent + f"{Fore.MAGENTA}{puzzle[i][j]}"
                elif (i, j) in wordsFounded["word6"]:
                    line += indent + f"{Fore.YELLOW}{puzzle[i][j]}"
                else:
                    line += indent + f"{Fore.WHITE}{puzzle[i][j]}"
            print(line)
        print(" ")
                    
                 
        input_image_path = os.path.join("image/", os.listdir('image/')[0])
        os.remove(input_image_path)