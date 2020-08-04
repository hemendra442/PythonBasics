def featureExtractor(x,D):
    print("Sentence: ", x)
    print("Words Set: ", D)
    f1 = {}
    f1 = x.split()
    print("words in sentence, Feature1: ",f1)
    count =0
    for w in f1:
        if w not in D:
            count+=1
    print("Num of Words in x not in D, Feature2: ",count)
x= input("Enter your sentence: ")
D = set()
n = int(input("Enter num of words in dictinory: "))
for i in range(n):
    word = str(input("Enter the word: "))
    D.add(word)

featureExtractor(x,D)