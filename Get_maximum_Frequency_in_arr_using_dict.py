
#code 1 in single scan find the value
def pairSum0(arr):
    c = 0
    dic = {}
    for val in arr:
        if -val in dic :
            c += dic[-val]
        dic[val] = dic.get(val, 0) + 1
    return c

#code 2 in double scan get your answer
def pairSum0(arr):
    dic = {}
    c = 0 # will be our ans we will add count into it
    for i in arr:
        dic[i] = dic.get(i, 0) + 1  #getting how much frequency of value

    part = dic.get(0, 1)  # counting of zero
    extra = (part*(part-1))//2   # need : _if_we_get_zero use combination formula nCr vala

    for key in dic:
        if key > 0 and -key in dic:
            c = c + (dic[key]*dic[-key]) # example  [2: 6times and -2: 3times] so pair will be 6*3 = 18
    return c + extra


arr = [2,-2,0,4,1,2,0,2,-2]
print(pairSum0(arr))