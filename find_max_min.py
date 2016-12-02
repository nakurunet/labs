def find_max_min(x):
    minimum = maximum = x[0] 
    for i in x[1:]:
        if i < minimum: #check if element is lowest
            minimum = i
        else: 
            if i > maximum: maximum = i#check if element is largest
    a=int(minimum) #convert minimum element to int
    b=int(maximum) #convert max element to int
    c=[a,b] #the list to return
    d=[len(x)] #return array of lenth of x if the maximum and minimum are equal
    if a == b:
      return d
    return c 