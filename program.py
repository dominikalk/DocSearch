from os.path import exists
import sys

def read_file_path():
    file_path = input("What is the path of the file?: ")
    return file_path

def read_files(file_path):
    file = []
    query = []
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
        file.append([s.strip() for s in line.split(" ")])

    query = [s.strip() for s in q.readline().split(" ")]

    f.close()
    q.close()

    return file, query

def make_dict(file):
    dict = {}
    for line in file:
        for word in line:
            if word in dict:
                pass
            else: 
                dict[word] = []
    return dict

def print_no_words(dict):
    print(f"Words in dictionary: {len(dict)}")

def print_query_details():
    print("Query: {'QUERY'}")
    print("Relevant documents: {'RELEVANT_DOCUMENTS'}")
    pass

def main():
    file, query = read_files(read_file_path())
    dict = make_dict(file)
    print_no_words(dict)
    print(dict)

if __name__ == "__main__":
    main()