from classical import *

if __name__ == '__main__':
    # unit testing for Caesar
    Caesar_p = 'abcdefghijklmnopqrstuVwxyz'
    caesar1 = Caesar(plain=Caesar_p, key=2)

    print(caesar1.getCipher())

    Caesar_c = caesar1.getCipher()
    caesar2 = Caesar(cipher=Caesar_c, key=2)
    print(caesar2.getPlain())

    # unit testing for Substitution
    Substitution_p = 'abcdefghijklmnopqrstuVwxyz'
    key={'a': 'X', 'b':'N', 'c':'Y', 'd':'A', 'e':'H', 'f':'P', 'g':'O', 'h':'G', 'i':'Z', 'j':'Q', 'k':'W', 'l':'B', 'm':'T', 'n':'S', 'o':'F', 'p':'L', 'q':'R', 'r':'C', 's':'V', 't':'M', 'u':'U', 'v':'E', 'w':'K', 'x':'J', 'y':'D', 'z':'I'}
    subs1 = Substitution(plain=Substitution_p, key=key)

    print(subs1.getCipher())

    Substitution_c = subs1.getCipher()
    subs2 = Substitution(cipher=Substitution_c, key=key)
    print(subs2.getPlain())

    # unit testing for Affine

    Affine_p = 'hot'
    key = (7, 3)
    aff1 = Affine(plain=Affine_p, key=key)

    print(aff1.getCipher())

    aff_c = aff1.getCipher()
    aff2 = Affine(cipher=aff_c, key=key)
    print(aff2.getPlain())

    # unit testing for Vigenere
    Vigenere_p = 'thiscryptosystemisnotsecure'
    key = (2, 8, 15, 7, 4, 17)
    Vigenere1 = Vigenere(plain=Vigenere_p, key=key)

    print(Vigenere1.getCipher())

    Vigenere_c = Vigenere1.getCipher()
    Vigenere2 = Vigenere(cipher=Vigenere_c, key=key)
    print(Vigenere2.getPlain())

    # unit testing for Hill
    Hill_p = 'july'
    Hill1 = Hill(plain=Hill_p, key=[[11, 8], [3, 7]])
    
    print(Hill1.getCipher())

    Hill_c = Hill1.getCipher()
    Hill2 = Hill(cipher=Hill_c, key=[[11, 8], [3, 7]])
    print(Hill2.getPlain())