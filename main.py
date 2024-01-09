""" **********************************************************
    Universidad de Cádiz
    Recuperación de la Información
    Proyecto RI
    Jorge Guerrero Díaz
    Cristian Leilael Rico Espinosa
********************************************************** """
# Import Libraries
import os
from tika import parser
import math
import json


def Result(IDF):
    for i in weights.keys():
        peso = IDF * weights[i]
        result[i] = peso
    weights.clear()


def TF_Process(indexJSON, kw, files):
    repeats = indexJSON[kw]
    for lst in repeats:
        if (files in lst):
            return math.log(lst[1], 2) + 1
    return 0


def IDF_Process(indexJSON, kw, size_files):
    number_files = len(indexJSON[kw])
    if (number_files != 0):
        return math.log((size_files/number_files), 2)
    return 0


def filter(i):
    special_char = ['.', ',', '¿', '?', '!', '¡', '=']
    stop_words = ['a', 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came', 'can', 'cannot', 'can\'t', 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', 'didn\'t', 'different', 'do', 'does', 'doesn\'t', 'doing', 'done', 'don\'t', 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', 'hasn\'t', 'have', 'haven\'t', 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', 'i', 'id', 'ie', 'if', 'i\'ll', 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is', 'isn\'t', 'it', 'itd', 'it\'ll', 'its', 'itself', 'i\'ve', 'j', 'just', 'k', 'keep	keeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', '\'ll', 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now',
                  'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', 'she\'ll', 'shes', 'should', 'shouldn\'t', 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure	t', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'that\'ll', 'thats', 'that\'ve', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'there\'ll', 'thereof', 'therere', 'theres', 'thereto', 'thereupon', 'there\'ve', 'these', 'they', 'theyd', 'they\'ll', 'theyre', 'they\'ve', 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', '\'ve', 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', 'we\'ll', 'went', 'were', 'werent', 'we\'ve', 'what', 'whatever', 'what\'ll', 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', 'who\'ll', 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', 'wont', 'words', 'world', 'would', 'wouldnt', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', 'you\'ll', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'you\'ve', 'z', 'zero']
    # Remove any special characters
    if (len(i) > 3):
        if (i in stop_words):
            return 'falso'
        else:
            # If a word has a special character from the array it would be removed.
            for j in special_char:
                i = i.replace(j, "")
            return i


def insert_index(parsed_document, files):
    if (parsed_document != None):
        res = parsed_document.split()
        for i in res:
            repetitions = parsed_document.count(i)
            kw = filter(i)
            if (kw != 'falso'):
                # if key word already exists in the index just add the file
                if (kw in index):
                    repeats = index[kw]
                    for lst in repeats:
                        if (files not in lst and files not in visited[kw]):
                            visited[kw] += (' ' + files)
                            index[kw].extend([[files, repetitions]])
                # if key word hasn't being inserted in the index
                elif (kw not in index):
                    index[kw] = [[files,  repetitions]]
                    visited[kw] = files


def readfiles(folderPath):
    corpusFiles = [file for file in os.listdir(folderPath)]
    # Read all the content for each file in the directory
    for files in corpusFiles:
        path = '.\\corpus\\' + files
        parsed_document = parser.from_file(path)
        insert_index(parsed_document['content'], files)


def readIndex(indexJSON, kw, size_files):
    if kw in indexJSON:
        repeats = indexJSON[kw]
        for lst in repeats:
            for files in lst:
                weights[files] = TF_Process(indexJSON, kw, files)
                break

            IDF = IDF_Process(indexJSON, kw, size_files)
            Result(IDF)
    else:
        print("There's not document with that word.")


def OneWord(folderPath):
    corpusFiles = [file for file in os.listdir(folderPath)]
    size_files = len(corpusFiles)
    consulta = input("\n Write the word: ")

    with open('indexFile.json') as f:
        indexJSON = json.load(f)
    readIndex(indexJSON, consulta, size_files)

    # Results
    if consulta in indexJSON:
        sorted_results = sorted(
            result.items(), key=lambda x: x[1], reverse=True)
        converted_dict = dict(sorted_results)
        counter = 0

        for i in converted_dict.keys():
            print("File Name: " + i)
            print("Weight: ")
            print(result[i])
            counter += 1
            if (counter > 20):
                break


def ORWord(folderPath):
    corpusFiles = [file for file in os.listdir(folderPath)]
    size_files = len(corpusFiles)
    count = int(input("\n How many terms: "))
    consulta = [None] * count
    for i in range(count):
        consulta[i] = input("\n Write the word: ")

    with open('indexFile.json') as f:
        indexJSON = json.load(f)
    ORINDEX = {}
    for i in consulta:
        readIndex(indexJSON, i, size_files)
        print(i)
        for i in result.keys():
            prev = 0
            if (i in ORINDEX):
                prev = ORINDEX[i]
            ORINDEX[i] = result[i] + prev
        result.clear()

    # Results

    sorted_results = sorted(
        ORINDEX.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_results)
    counter = 0

    for i in converted_dict.keys():
        print("File Name: " + i)
        print("Weight: ")
        print(ORINDEX[i])
        counter += 1
        if (counter > 20):
            break


def ANDWord(folderPath):
    corpusFiles = [file for file in os.listdir(folderPath)]
    size_files = len(corpusFiles)
    count = int(input("\n How many terms: "))
    consulta = [None] * count
    for i in range(count):
        consulta[i] = input("\n Write the word: ")

    with open('indexFile.json') as f:
        indexJSON = json.load(f)
    ANDINDEX2 = {}
    ANDINDEX = {}
    count = 1
    if (count == 1):
        for i in consulta:
            readIndex(indexJSON, i, size_files)
            for i in result.keys():
                prev = 0
                if (i in ANDINDEX):
                    prev = ANDINDEX[i]
                    ANDINDEX[i] = result[i] + prev

                elif (i not in ANDINDEX):
                    ANDINDEX[i] = result[i] + prev
            result.clear()
        count += 1
    if (count > 1):
        for i in range(1, len(consulta)):
            print(consulta[i])
            readIndex(indexJSON, consulta[i], size_files)
            for i in result.keys():
                print('Archivos')
                print(i)
                prev = 0
                print(ANDINDEX)
                if (i in ANDINDEX):
                    prev = ANDINDEX[i]
                    ANDINDEX[i] = result[i] + prev
                    ANDINDEX2[i] = ANDINDEX[i]
            if (ANDINDEX.keys() != ANDINDEX2.keys()):
                if (ANDINDEX2):
                    ANDINDEX = ANDINDEX2
                    print('Despues de Galaxy')
                    print(ANDINDEX)
                    # ANDINDEX2.clear()
            result.clear()

    # Results

    sorted_results = sorted(
        ANDINDEX.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_results)
    counter = 0
    for i in converted_dict.keys():
        print("File Name: " + i)
        print("Weight: ")
        print(ANDINDEX[i])
        counter += 1
        if (counter > 20):
            break


def main():
    folderPath = '.\\corpus'
    print('*** Information Retrieval Project ***')

    ans = True
    while ans:
        print("""
        IMPORTANT: If its the first time, remember to create the index *BEFORE* making a search.
        1. Create Index.
        2. Look for a word.
        3. Search with AND condition(s).*
        4. Search with OR condition(s).
        5. Exit / Quit.
        ** 3. Doesn't work properly, it shows files without all of the words that are prompted.
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            print("Creating Index ...")

            readfiles(folderPath)
            with open('indexFile.json', 'w') as convert_file:
                convert_file.write(json.dumps(index))
            convert_file.close()
            print("--- Index Created ---")

        elif ans == "2":
            OneWord(folderPath)

        elif ans == "3":
            print("CAUTION: Doesn't work properly!")
            ANDWord(folderPath)

        elif ans == "4":
            ORWord(folderPath)

        elif ans == "5":
            print("\n Goodbye")
            ans = False

        elif ans != "":
            print("\n Invalid Choice, Try Again")
        indexJSON.clear()
        visited.clear()
        result.clear()
        weights.clear()
        index.clear()
        result.clear()


indexJSON = {}
visited = {}
result = []
weights = {}
index = {}
result = {}

i = 0
main()
