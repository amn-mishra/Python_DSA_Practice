# check  the frequency of the word in our string :
def frequency(str, k):
    word = [i for i in str.split()]
    d = {}
    for w in word:
        d[w] = d.get(w, 0) + 1
    for i in d:
        if d[i] == k:
            print(i, d[i])


string = "this is the only this this solution of this perticular problem and keep in mind you are on right track this is enough in my case"
k = 5
frequency(string, k)
