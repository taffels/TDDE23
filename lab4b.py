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
