import sys
import os

def convert(fread, selection):
    """Convert Bibleworks fonts to Unicode"""

    if selection == '1':
        charfile = 'hebrew.txt'
        converter = 1
        lang = 1
    elif selection == '2':
        charfile = 'hebrew.txt'
        converter = 2
        lang = 1
    elif selection == '3':
        charfile = 'greek.txt'
        converter = 1
        lang = 2
    elif selection == '4':
        charfile = 'greek.txt'
        converter = 2
        lang = 2
    else:
        print('wrong selection, exiting...')
        sys.exit()

    bwhebb = []
    hebrew = []
    result = ''
    indicator = False
    vowels = ''

    try:
        c = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), charfile), 'r', encoding='utf-8')
    except (OSError, IOError):
        print('Character file not found, exiting...')
        sys.exit()

    #load characters and vowels in string
    for character in c:
        character.encode(encoding='utf-8', errors='replace')
        character = character.strip()
        split = character.split(' ')
        if indicator == True:
            vowels += character[0]
        if 'vowels:' in character:
            indicator = True
        elif converter == 1:
            bwhebb.append(split[0])
            hebrew.append(split[-1])
        elif converter == 2:
            bwhebb.append(split[-1])
            hebrew.append(split[0])
    c.close()

    try:
        f = open(fread, 'r', encoding='utf-8')
    except (OSError, IOError):
        print('Input file not found, exiting...')
        sys.exit()
    for content in f:
        content = content.replace(' / ', '*')
        content = content.replace('* ','*')
        content = content[:-1]
        #replace vowels
        content = ReplaceVowels(content, vowels)
        #change RTL before replacing characters
        if lang == 1:
            content = ChangeRTL(content)
        #change characters one by one
        for i in range(len(bwhebb)):
            content = content.replace(bwhebb[i], hebrew[i])
        content = content.replace('*', '/')
        result += content + '\n'
    f.close()
    if lang == 1:
        result = result +  u'\u200f'
    return result

def ReplaceVowels (content, vowels):
#change the place of the vowels with the consonant before it (RTL)
    content = ' ' + content + ' '
    for i in range(len(content)):
        for j in range(len(vowels)):
            if vowels[j] == content[i]:
                replace = list(content)
                replace[i] = content[i-1]
                replace[i-1] = content[i]
                content = ''.join(replace)
    content = content.strip()
    return content

#change RTL
def ChangeRTL(content) :
    result = ''
    for i in range(len(content)-1, -1, -1):
        result += content[i]
    return result

