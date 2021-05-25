import nltk
import pandas as pd
import os
import sys
from IPython.core.display import display, HTML
import numpy
import matplotlib

#sys.stdout = open('concordanceResults.txt', 'w')

#os.system("all_tl.txt.txt")

#cwd = os.getcwd()
#print (cwd)
''' How should this be organized? Menu eventually reaches an 'option'; from 
there, I want to...
-make a 'results' file that everything will get written to (or maybe just a list??)
-iterate through all the txt files, pull out the entry name (which is just the file name)
-append entry to 'entry list' if concordance results are not null
-append concordance results to...something? a string?? hmm, write them to file
-link to github/frantext and such
-maybe open image?
-WOW!! 60+ materials...making a sub-menu for each of these is going to fucking suck. How to make this more efficient??
    Maybe...print out list of materials, tell user to type in which one they want in PARTICULAR and feed that into 'option'??'''

'''Make list of entries clicakble!!!! easy to do, string join with some library to make clickable'''


'''tlRaw = open("all_tl.txt.txt", encoding="utf8").read()
tlTokenized = nltk.word_tokenize(tlRaw)
tl = nltk.Text(tlTokenized)

tl.concordance("dragon")
tl.concordance("purple")
tl.concordance("orange")
tl.concordance("yellow", lines=100)
tl.concordance("green", lines = 1000)'''

def cindex_menu():
    choice = '0'
    while choice == '0':
        print("Chromatic Index for Bnf Ms Fr 640. Please press 1 for Red when prompted, or ''e'' to exit.")
        
        color_choice = input('Input 1 for Red or e to exit.')
        if color_choice=='e':
            sys.exit()
        
        if color_choice == '1':
            print('Red. Press 1 for the generic color "red"; press 2 for red materials; press 3 for red pigments/dyes; press 4 for colors derived from red; press 0 to return to main menu.')
    
            red_choice = input('Input 1, 2, 3, 4, or 0.')
            if red_choice=='0':
                cindex_menu()
            
            while red_choice == '1':
                print('Generic red.')
                searchFolios("red")
                red_choice = input('Input 2 for red materials, 3 for red pigments/dyes, 4 for colors derived from red, or 0 to return to the main menu. ')
                if red_choice=='0':
                    cindex_menu()
                
                searchFolios('red')
                      
            while red_choice == '2':
                print('Red materials. The list of materials will be printed, input the material you want.')
                
                materialsList = open("redMaterialsList.txt", encoding="utf8").readlines()
                for word in materialsList:
                    print(word)
                
                print("Please enter the material you want EXACTLY as it appeared - all lowercase, spaces where appropriate.")
                material_choice = input('Please input your desired material: ')
                
                searchFolios(material_choice)
                
                print('Input 2 to search for more materials, 3 for red pigments/dyes, 4 for red colors, or 0 to return to the main menu.')
                red_choice = input('Input your choice: ')
                
            while red_choice == '3':
                pigmentsDyesList = open("redPigmentsDyesList.txt", encoding="utf8").readlines()
                print('Red pigments/dyes. The list of dyes will be printed. Input the pigment/dye you want.')
                for word in pigmentsDyesList:
                    print(word)
                
                print("Please enter the pigment/dye you want EXACTLY as it appeared - all lowercase, spaces where appropriate.")
                pdChoice = input('Please input your desired pigment/dye.')
                searchFolios(pdChoice)
                
                print("Input 3 to search for more pigments/dyes, 2 to search for materials, 4 for red colors, or 0 to return to the main menu.")
                red_choice = input("Input your choice: ")
 
                
            while red_choice == '4':
                print('Red colors. The list of colors will be printed...')
                colorsList = open("redColors.txt", encoding="utf8").readlines()
                for word in colorsList:
                    print(word)
                
                print("Please enter the color you want EXACTLY as it appeared - all lowercase, spaces where appropriate.")
                searchColorChoice = input('Please input your desired color: ')
                searchFolios(searchColorChoice)
                
                print("Input 4 to search for more colors, 2 to search for materials, 3 for pigments/dyes, or 0 to return to the main menu.")
                red_choice = input("Input your choice: ")
 
            
            while red_choice == '5':
                color_choice == '1'

    while choice == '2':
        sys.exit()
        
    if choice != '1' and choice != '2':
        print('WHAT?!?! Try again, input 1, please.')
        cindex_menu()
        
#phrase cocordance??? https://stackoverflow.com/questions/33813405/concordance-for-a-phrase-using-nltk-in-python
'''def n_concordance_tokenised(text,phrase,left_margin=5,right_margin=5):
    #concordance replication via https://simplypython.wordpress.com/2014/03/14/saving-output-of-nltk-text-concordance/

    phraseList=phrase.split(' ')

    c = nltk.ConcordanceIndex(text.tokens, key = lambda s: s.lower())

    #Find the offset for each token in the phrase
    offsets=[c.offsets(x) for x in phraseList]
    offsets_norm=[]
    #For each token in the phraselist, find the offsets and rebase them to the start of the phrase
    for i in range(len(phraseList)):
        offsets_norm.append([x-i for x in offsets[i]])
    #We have found the offset of a phrase if the rebased values intersect
    #--
    # http://stackoverflow.com/a/3852792/454773
    #the intersection method takes an arbitrary amount of arguments
    #result = set(d[0]).intersection(*d[1:])
    #--
    intersects=set(offsets_norm[0]).intersection(*offsets_norm[1:])

    concordance_txt = ([text.tokens[map(lambda x: x-left_margin if (x-left_margin)&gt;0 else 0,[offset])[0]:offset+len(phraseList)+right_margin] for offset in intersects])

    outputs=[''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]
    return outputs

def n_concordance(txt,phrase,left_margin=5,right_margin=5):
    tokens = nltk.word_tokenize(txt)
    text = nltk.Text(tokens)

    return

#n_concordance_tokenised(text,phrase,left_margin=left_margin,right_margin=right_margin)'''
            
def searchFolios(option):
    
    folioList = []
    #optionBarList = []
    #opbarInd = 1
    
    alltlRaw = open("all_tl.txt.txt", encoding="utf8").read()
    alltlTokenized = nltk.word_tokenize(alltlRaw)
    alltl = nltk.Text(alltlTokenized)
    
    print('Searching for: ' + option + '\n')
    alltl.dispersion_plot([option])
    #alltl.dispersion_plot(["red", "blue", "yellow", "green"])
    
    for filename in os.listdir('BnfTL'):
        tlRaw = open(('./BnfTL/' + filename), encoding="utf8").read()
        tlTokenized = nltk.word_tokenize(tlRaw)
        tl = nltk.Text(tlTokenized)
        #tl = tl.lower()
        
        #kwicFile = filename+'kwicFile'
        #sys.stdout = open(kwicFile, 'w')
        
        #concordanceCheck
        '''if(tl.concordance(option, lines = 10000)) is not None:
            
            print(filename)
            print('\n')
            
            kwic = nltk.ConcordanceIndex(tl)
            for line in kwic:
                if kwic.offsets(option):
                    kwic.print_concordance(option)'''
            
        '''kwic = tl.concordance(option, lines = 1000)
            for line in kwic:
                if line.offsets(line):
                    line.print'''
        
        kwic = nltk.ConcordanceIndex(tl)
        
        if kwic.offsets(option):
            print(filename)
            print('==========')
            print('\n')
            kwic.print_concordance(option)
            print('==========')
            print('\n')
            folioList.append(filename)
            #optionBarList[opbarInd] = tl.count(option)
            #opbarInd +=1
            #optionBarList.append(tl.count(option))
     
    print("Links to folios" + "\n")
    
    for folio in folioList:
        folioURL = 'https://github.com/cu-mkp/m-k-manuscript-data/blob/master/ms-txt/tl/' + folio
        print(folioURL)
        folioLink = display(HTML("<a href=" + folioURL + ">" + folio + "</a>"))
        display(HTML(folioLink))
        
    print('Link to Frantext search for ' + option + '\n')
    frantextURL = 'https://artflsrv03.uchicago.edu/philologic4/frantext0917/query?report=kwic&method=proxy&q=' + option + '&start=0&end=0&direction=&metadata_sorting_field='
    frantextLink =  display(HTML("<a href=" + frantextURL + ">" + 'Frantext search for ' + option + "</a>"))   
    display(HTML(frantextLink))

cindex_menu()
    
        
    
