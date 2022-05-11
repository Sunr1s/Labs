import simplemma
from simplemma import text_lemmatizer
langdata = simplemma.load_data('uk')
Token_text = ''
# Python program to convert a list to string
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ' '+ele  
    
    # return string  
    return str1 

print(text_lemmatizer(listToString(Token_text), langdata))