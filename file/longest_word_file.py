def longest_word(fileName):

    with open(fileName, 'r') as fileData:
        wordList = fileData.read().split()

        longest_word_len = max(len(word) for word in wordList )   #len(max(wordList, key=len))

        print("Size of longest word", longest_word_len)

        result = [x for x in wordList if len(x) == longest_word_len]

        for item in result:
            print(item)

        print("The values are ", result)

    fileData.close()

longest_word("find_winner.py")