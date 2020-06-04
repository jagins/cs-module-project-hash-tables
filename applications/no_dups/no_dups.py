def no_dups(s):
    dictionary = {}

    string = s.split()
    new_array = []
    sepeartor = " "
    for i in string:
        if i not in dictionary:
            dictionary[i] = i
    
    for word in string:
        if word in dictionary:
            if word not in new_array:
                new_array.append(word)
    return sepeartor.join(new_array)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))