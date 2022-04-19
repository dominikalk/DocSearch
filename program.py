from fileinput import lineno
from os.path import exists
import sys, re

def read_file_path():
    file_path = input("What is the path of the file?: ")
    return file_path

def read_files(file_path):
    file = []
    queries = []
    print(f"{file_path}/docs.txt")
    if exists(f"{file_path}/docs.txt"):
        f = open(f"{file_path}/docs.txt", "r")
    else:
        sys.exit("That directory or the docs.txt file does not exist.")

    if exists(f"{file_path}/queries.txt"):
        q = open(f"{file_path}/queries.txt", "r")
    else:
        sys.exit("That directory or the queries.txt file does not exist.")

    for line in f:
        file.append([s.strip() for s in re.split(" |\t", line)])

    for line in q:
        queries.append([s.strip() for s in line.split(" ")])

    f.close()
    q.close()

    return file, queries

def make_dict(file):
    dict = {}
    for i, line in enumerate(file):
        for word in line:
            if word in dict:
                pass
            else: 
                dict[word] = [0] * len(file)

            dict[word][i] += 1
    return dict

def print_no_words(dict):
    print(f"Words in dictionary: {len(dict)}")

def print_query_details(dict, query, no_documents):
    print(f"Query: {' '.join(query)}")

    # Find query words that are actually in the file
    relevant_query = []
    for word in query:
        if word in dict:
            relevant_query.append(word)

    # Find relevant documents
    relevant_docs = list(range(1, no_documents + 1))
    for word in relevant_query:
        for i in range(0, no_documents):
            if dict[word][i] == 0:
                if (i + 1) in relevant_docs:
                    relevant_docs.remove(i + 1)
    print(f"Relevant documents: {' '.join([str(s) for s in relevant_docs])}")
    pass

def main():
    # file, queries = read_files(read_file_path())
    file, queries = read_files("testCases/set2")
    dict = make_dict(file)
    print_no_words(dict)
    for query in queries:
        print_query_details(dict, query, len(file))

if __name__ == "__main__":
    main()