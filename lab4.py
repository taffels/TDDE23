def split_it(message):
    string1 = []
    string2 = []
    
    for elem in range(len(message)):
        char = message[elem]
        if char.islower() or char == "_" or char == ".":
            string1.append(char)
        elif char.isupper() or char == " " or char == "|":
            string2.append(char)
    return "".join(string1), "".join(string2)


def split_rec(message, lower = '', upper = ''):
    res = lower, upper

    if len(message) == 0:
        return res

    char = message[0]

    if isinstance(message, str):
        if char.islower() or char == "_" or char == ".":
            return split_rec(message[1:], lower + char, upper)
        elif char.isupper() or char == " " or char == "|":
            return split_rec(message[1:], lower, upper + char)
        else:
            return split_rec(message[1:], lower, upper)
    else:
        print("must be a string")



def interpret(arg, dic):
        
    if isinstance(arg, str):
        if arg in dic.keys():
            if dic[arg] == 'true':
                return 'true'
            else:
                return 'false'
        else:
            return arg
        
        
    elif isinstance(arg, list) and len(arg) == 2:
        if arg[0] == "NOT":
            if interpret(arg[1], dic) == 'true':
                return 'false'
            else:
                return 'true'
           


    elif isinstance(arg, list) and len(arg) == 3:
        if arg[1] == "AND":
            if interpret(arg[0], dic) == 'true' and interpret(arg[2], dic) == 'true':
                return 'true'
            else:
                return 'false'
        elif arg[1] == "OR":
            if interpret(arg[0], dic) == 'true' or interpret(arg[2], dic) == 'true':
                return 'true'
            else:
                return 'false'
        else: 
            return 'false'
