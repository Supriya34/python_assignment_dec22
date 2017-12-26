list_of_words=input("enter the words separated by comma")

list_of_words=list_of_words.split(",")

list_of_words=sorted(list_of_words)

print(",".join(list_of_words))
