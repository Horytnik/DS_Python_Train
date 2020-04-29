
def test(fun, *args):
    print ("".join(['-' for i in range(40)]))
    print (fun.__name__[:-1].upper()+" "+fun.__name__[-1])
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print ("Yes, "+decoded.replace("my","your"))
        else:
            print ("No, "+decoded.replace("my","your").replace("has","has not")+" yet")
    else:
        print ("Is correct? "+ str(res == args[-1]))
    print ("".join(['-' for i in range(40)]))


def zadanie1(listObject):
    uniqueList = [listObject[0]]

    for obj in listObject:
        if obj != uniqueList[-1]:
            uniqueList.append(obj)
    return uniqueList
print(zadanie1([1, 2, 3, 3, 5, 68, 68, 24]))
test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1,2,3,5,68,24])


def zadanie2(list1, list2):
    sumList = []

    if len(list1) < len(list2):
        shorterList = list1
        longerList = list2
    else:
        shorterList = list2
        longerList = list1

    for i in range(0,len(shorterList)):
        sumList.append(list1[i])
        sumList.append(list2[i])
    sumList = sumList + longerList[i+1:len(longerList)]
    # type your code
    return sumList

print(zadanie2([1, 2, 19, 'dd', ':P', ":("], [12,'c','5']))

test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])


def zadanie3(listTuples):
    listTuples.sort(key = lambda tup: tup[-1])
    return listTuples

test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])


def zadanie4(text):
    sentence = ""
    text = text.replace("$", " ")
    text = text.replace("ok", "")
    words = text.split(" ")
    for ctr in range(0, len(words), 2):
        sentence = sentence + " " + words[ctr]
    return sentence


print(zadanie4("okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af"))


test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])
