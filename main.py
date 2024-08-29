import string
text = open("emotion.txt" ,encoding="utf-8").read()
lowercase = text.lower()
cleaned_text = lowercase.translate(str.maketrans('','',string.punctuation))
print (cleaned_text) 