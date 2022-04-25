from os.path import exists
import sys
import numpy as np
import math

def read_files():
    """
    Function that reads docs.txt and queries.txt from the current directory and 
    returns a 2D array for both containing each word from each line.
    """
    file = []
    queries = []
    if exists("docs.txt"):
        f = open("docs.txt", "r")
    else:
        sys.exit("docs.txt file does not exist in this directore.")

    if exists("queries.txt"):
        q = open("queries.txt", "r")
    else:
        sys.exit("queries.txt file does not exist in this directore.")

    for line in f:
        file.append([s.strip() for s in line.strip().replace('\t', ' ').split(' ')])

    for line in q:
        queries.append([s.strip() for s in line.split(" ")])

    f.close()
    q.close()

    return file, queries

def make_dict(file):
    """
    Takes a 2D array and returns an inverted index dictionary with the occurencies
    of each word in each document.
    """
    dict = {}

    for i, line in enumerate(file):
        for word in line:
            if not word in dict:
                dict[word] = [0] * len(file)  
            dict[word][i] += 1
    return dict

def print_no_words(dict):
    """
    Takes a dictionary and prints a string detailing the number of unique 
    words in it.
    """
    print(f"Words in dictionary: {len(dict)}")

def calc_angle(x, y):
    """
    Takes two vectors in the form of a numpy array and works out the angle between them.
    """
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

def print_query_details(dict, tp, query, no_documents):
    """
    Takes a dictionary, query and the number of documents, and prints the query,
    relevant documents to it, in order from least to most relevant the angle between
    the document and query.
    """
    print(f"Query: {' '.join(query)}")

    # Find query words that are actually in the file
    relevant_query = []
    for word in query:
        if word in dict:
            relevant_query.append(word)

    # Find relevant documents
    list_of_document_IDs = []
    for i in range(no_documents):
        contains_all = True
        for word in relevant_query:
            if dict[word][i] == 0:
                contains_all = False
                break
        if contains_all == True and len(relevant_query) != 0:
            list_of_document_IDs.append(i + 1)
    print(f"Relevant documents: {' '.join([str(s) for s in list_of_document_IDs])}")

    # Find angles for each relevant document
    document_array = []
    for doc in list_of_document_IDs:
        x = np.array(tp[doc - 1])
        y = np.array([0] * len(dict))

        for word in relevant_query:
            if dict[word][doc - 1] != 0:
                y[list(dict.keys()).index(word)] = 1
        
        document_array.append([round(calc_angle(x, y), 5), doc])
    
    document_array = sorted(document_array, key=lambda x: x[0])
    
    # Print ordered documents with their angles
    for doc in document_array:
        print(f"{doc[1]} {doc[0]}")

def main():
    file, queries = read_files()
    dict = make_dict(file)
    print_no_words(dict)
    tp = np.transpose(list(dict.values()))
    for query in queries:
        print_query_details(dict, tp, query, len(file))

if __name__ == "__main__":
    main()