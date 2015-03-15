
# coding: utf-8

# In[1]:

#Write a function `unpunctuate` that takes a string and removes all punctuation, e.g.

import string

def unpunctuate(x):
    for i in string.punctuation:
        x = x.replace(i, "")
        
    return x

text = "Hey there! How's it going? I have a list: stuff, things and more stuff"
print unpunctuate(text)


# In[2]:

#Write a function `get_bag_of_words_for_single_document` that, given any string (also called document), e.g. "John also likes to watch football games.", returns its bag of words:
#Didn't strip out punctuation here, strip it out in next function

from collections import Counter

def get_bag_of_words_for_single_document(x):
    bag = {}
    words = x.split()
    count = Counter(words)
    for word in words:
        bag.update({word : count[word]})
    return bag

text = "John also likes to watch football games."
print get_bag_of_words_for_single_document(text)
    


# In[6]:

#Write a function `get_bag_of_words` that uses the above function to achieve the following: given a list of strings, it returns the total bag of words
#for all of the documents.

from collections import Counter

def get_bag_of_words(x):
    bag = {}
    words = [word for item in x for word in item.split()]
    unpunctuated =[]

    for word in words:
        x = str(word)
        for i in string.punctuation:
            x = x.replace(i, "")
        unpunctuated.append(x)
    
    count = Counter(unpunctuated)
    for word in unpunctuated:
        bag.update({word : count[word]})
    return bag


    
text = ["John likes to watch movies. Mary likes movies too.", "John also likes to watch football games."]
print get_bag_of_words(text)


# In[7]:

#Given a bag of words for all of the documents in our data set, write a function `turn_words_into_indices` take the keys in the bag of words and alphabetize them,

def turn_words_into_indices(x):
    keys_list = x.keys()
    keys_list.sort(key=lambda x: x.lower())
    return keys_list
    

    
bag_of_words_data = {
    "John": 1,
    "likes": 2,
    "to": 3,
    "watch": 4,
    "movies": 5,
    "also": 6,
    "football": 7,
    "games": 8,
    "Mary": 9,
    "too": 10
}

print turn_words_into_indices(bag_of_words_data)


# In[8]:

#Given a document, write a function `vectorize` that turns the document into a list (also will be called a vector) the same length as the number of keys of bag of words where
#for each index of the list will be 1 only if the word at that index in the word list is contained in the document and 0 otherwise.
from collections import Counter

def vectorize(word_list, document):
    vector = []
    document = document.split()
    count = Counter(document)
   
    for word in word_list:
        if word in document:
            vector.append(count[word])
        else:
            vector.append(0)
    return vector
    

x = ["also", "football", "games", "John", "likes", "Mary", "movies", "to", "too", "watch"]
y = "The sun also rises. Let's also go to the movies"
print vectorize(x, y)


# In[ ]:



