def perm_gen_lex(a):
    """Returns the various permutations of a given word in Lexographic order
     as a list"""
    permutations = []
    if len(a) == 1:
        return [a]
    elif len(a) == 0:
        return []
    else:
        for letter in a:
            for b in perm_gen_lex(a.replace(letter,'')):
                permutations.append(letter+b)
    return(permutations)
