def error_checker(string):

    string=string.upper()

    error_d={}
    allowed=['A','C','G','T']

    for count,x in enumerate(string):

        if x not in allowed:
            
            error_d[x]='Position '+str(count+1)
    
    output=''
    
    if error_d=={}:
        output='Your string does not contain any errors'

    else:
        for key, value in error_d.items():
            output+=( '\n'+ '  '+ key + " : " + value)
    
 

    return output



