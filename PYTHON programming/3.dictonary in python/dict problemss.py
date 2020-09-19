## i have to get the sentance as input form the user and cout the user input..
#sentence -> input,key->word, value->length of the word


sent=input("Enter the sentence")
words=sent.split(" ")
count_words={words:len(words) for words in words}
print(count_words)
