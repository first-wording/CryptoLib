import classical

def multiply_encode(plain):
    # 第一次加密，代换密码加密
    key1 = {'a': 'X', 'b':'N', 'c':'Y', 'd':'A', 'e':'H', 'f':'P', 'g':'O', 'h':'G', 'i':'Z', 'j':'Q', 'k':'W', 'l':'B', 'm':'T', 'n':'S', 'o':'F', 'p':'L', 'q':'R', 'r':'C', 's':'V', 't':'M', 'u':'U', 'v':'E', 'w':'K', 'x':'J', 'y':'D', 'z':'I'}
    cryp1 = classical.Substitution(plain=plain, key=key1)

    # 第二次加密，仿射密码加密
    key2 = (7, 3)
    cryp2 = classical.Affine(plain=cryp1.getCipher(), key=key2)

    # 第三次加密，维吉尼亚密码加密
    key3 = (2, 8, 15, 7, 4, 17, 8, 7)
    cryp3 = classical.Vigenere(plain=cryp2.getCipher(), key=key3)

    # 第四次加密，希尔密码加密
    key4 = [[11, 8], [3, 7]]
    cryp4 = classical.Hill(plain=cryp3.getCipher(), key=key4)

    return cryp4.getCipher()

def multiply_decode(cipher):
    # 倒序解密
    key4 = [[11, 8], [3, 7]]
    key3 = (2, 8, 15, 7, 4, 17, 8, 7)
    key2 = (7, 3)
    key1 = {'a': 'X', 'b':'N', 'c':'Y', 'd':'A', 'e':'H', 'f':'P', 'g':'O', 'h':'G', 'i':'Z', 'j':'Q', 'k':'W', 'l':'B', 'm':'T', 'n':'S', 'o':'F', 'p':'L', 'q':'R', 'r':'C', 's':'V', 't':'M', 'u':'U', 'v':'E', 'w':'K', 'x':'J', 'y':'D', 'z':'I'}
    cryp4 = classical.Hill(cipher=cipher, key=key4)
    cryp3 = classical.Vigenere(cipher=cryp4.getPlain(), key=key3)
    cryp2 = classical.Affine(cipher=cryp3.getPlain(), key=key2)
    cryp1 = classical.Substitution(cipher=cryp2.getPlain(), key=key1)
    return cryp1.getPlain()


if __name__ == '__main__':
	print('测试所用到的文本：thisisatestforml')
	a = multiply_encode('thisisatestforml')
	print('对原文加密后的结果：', a)

	b = multiply_decode(a)
	print('对密文解密后的结果：', b)
