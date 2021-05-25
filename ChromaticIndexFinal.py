import nltk
import pandas as pd
import os
import sys
from IPython.core.display import display, HTML
import numpy
import matplotlib

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

def searchFolios(option):

    folioList = []

    #Make NLTK text object of entire manuscript in order to generate disperson plot
    alltlRaw = open("all_tl.txt.txt", encoding="utf8").read()
    alltlTokenized = nltk.word_tokenize(alltlRaw)
    alltl = nltk.Text(alltlTokenized)

    print('Searching for: ' + option + '\n')
    alltl.dispersion_plot([option])
    #alltl.dispersion_plot(["red", "blue", "yellow", "green"])

    # Search through folios for inputted term, print out results and links
    for filename in os.listdir('BnfTL'):
        tlRaw = open(('./BnfTL/' + filename), encoding="utf8").read()
        tlTokenized = nltk.word_tokenize(tlRaw)
        tl = nltk.Text(tlTokenized)

        kwic = nltk.ConcordanceIndex(tl)

        if kwic.offsets(option):
            print(filename)
            print('==========')
            print('\n')
            kwic.print_concordance(option)
            print('==========')
            print('\n')
            folioList.append(filename)

    print("Links to folios" + "\n")

    for folio in folioList:
        folioURL = 'https://github.com/cu-mkp/m-k-manuscript-data/blob/master/ms-txt/tl/' + folio
        print(folioURL)
        folioLink = display(HTML("<a href=" + folioURL + ">" + folio + "</a>"))
        display(HTML(folioLink))

    # Print link to Frantext
    print('Link to Frantext search for ' + option + '\n')
    frantextURL = 'https://artflsrv03.uchicago.edu/philologic4/frantext0917/query?report=kwic&method=proxy&q=' + option + '&start=0&end=0&direction=&metadata_sorting_field='
    frantextLink =  display(HTML("<a href=" + frantextURL + ">" + 'Frantext search for ' + option + "</a>"))
    display(HTML(frantextLink))

cindex_menu()
