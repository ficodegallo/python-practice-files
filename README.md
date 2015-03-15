# python-practice-files
Practice python skill by creating a series of functions that take text, manipulate it and develop a vector based on matching 
a given sentence to a pre-defined list of words

- Create a function `unpunctuate` that takes a string and removes all punctuation, e.g.
- Write a function `get_bag_of_words_for_single_document` that, given any string (also called document), 
e.g. "John also likes to watch football games.", returns its bag of words:
- Write a function `get_bag_of_words` that uses the above function to achieve the following: given a list of strings, 
it returns the total bag of words for all of the documents.
- Given a bag of words for all of the documents in our data set, write a function `turn_words_into_indices` take the 
keys in the bag of words and alphabetize them
- Given a document, write a function `vectorize` that turns the document into a list (also will be called a vector) the same 
length as the number of keys of bag of words where for each index of the list will be 1 only if the word at that index in the 
word list is contained in the document and 0 otherwise.


