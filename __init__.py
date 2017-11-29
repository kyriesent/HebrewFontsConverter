# -*- coding: utf-8 -*-

#Script to convert Text in BwHebb Fonts to normal unicode Hebrew.
#copyright 2013 Benjamin Schnabel Benjamin-777@gmx.de www.benjaminschnabel.de
#Benjamin-777@gmx.de

import os
import codecs

import hebrew_fonts_converter

#Load file
def LoadFile() :
    fread = input('Enter input file:')
    print('Select options:')
    print('[1] Bwhebb -> Hebrew')
    print('[2] Hebrew -> Bwhebb')
    print('[3] Bwgrk -> Greek')
    print('[4] Greek -> Bwgrk')
    selection = input()
    return (fread, selection)

#read line
def ReadLine(fread, selection) :
    return hebrew_fonts_converter.convert(fread, selection)

#write file
def  WriteFile(content) :
    content.encode(encoding='utf-8', errors='replace')
    filename = input('Enter output file:')
    fwrite = open(filename,'w', encoding='utf-8')
    fwrite.writelines(content)
    fwrite.close()

fread = None
result = None
fread, selection = LoadFile()
fread = os.path.abspath(fread)
result = ReadLine(fread, selection)
WriteFile(result)
