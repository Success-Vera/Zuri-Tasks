# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open (filename) as f:
      lines=f.readlines()
    return lines
    #return "Hello World"
    


def count_words():
    word_counter={}
    text = read_file_content("./story.txt")
    for lines in text:
      word=lines.split()
      for words in word:
        if words not in word_counter.keys():
          word_counter[words]=0
        else:
          word_counter[words]+=1
    return word_counter

    # [assignment] Add your code here
    # return {"as": 10, "would": 20}
count_words()
