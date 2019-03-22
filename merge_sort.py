def mergesort(list_a):
    if len(list_a) == 1:
        return list_a
    list_b = mergesort(list_a[:len(list_a)//2])
    list_c = mergesort(list_a[len(list_a)//2:])
    return merge(list_b,list_c)

def merge(list_b,list_c):
    list_a = []  
    while True:
        if list_b == None or list_b == []:
            list_a.extend(list_c)
            return list_a
        if list_c == None or list_c == []:
            list_a.extend(list_b)
            return list_a
        if list_b[0] <= list_c[0]:
            list_a.append(list_b[0])
            list_b = list_b[1:]
        else:
            list_a.append(list_c[0])
            list_c = list_c[1:]  
