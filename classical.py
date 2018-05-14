import cryptomath
import numpy

class Classical(object):
    """ 古典密码基类，定义公共接口和成员变量，约束明文为小写，密文为大写 """

    __plain = ''
    __cipher = ''
    __key = None

    """ encode 函数必须重载 """
    def encode(self):
        # self.__cipher = self.__plain.upper()
        return self.__plain.upper()

    """ decode 函数必须重载 """
    def decode(self):
        # self.__plain = self.__cipher.lower()
        return self.__cipher.lower()

    def getPlain(self):
        return self.__plain

    def getCipher(self):
        return self.__cipher

    def getKey(self):
        return self.__key

    def setPlain(self, plain):
        self.__plain = plain
        self.encode()

    def setCipher(self, cipher):
        self.__cipher = cipher
        self.decode()

    def setKey(self, key):
        __key = key
        self.encode()

    def __init__(self, plain = '', cipher = '', key = None):
        """
        plain 和 cipher 需要调用保证其中一个为空，若都不为空则默认
        cipher 为空需要输入保证原文或密文为只含字母的字符串，其他字
        符不会被加密/解密
        """
        self.__plain = plain.lower()
        self.__cipher = cipher.upper()
        self.__key = key

        if self.__plain:
            self.__cipher = self.encode()
        elif self.__cipher:
            self.__plain = self.decode()

class Caesar(Classical):
    """
    移位密码体制，移动位数 key 在初始化时指定，并可以被改变移位密码的
    key 应当为一个 [0, 25] 之间的整数，由输入保证，函数本身不做检查
    """
    def encode(self):
        cipher = self.getPlain().upper()
        for i in range(0, len(cipher)):
            cipher = cipher[:i] + chr((ord(cipher[i]) - ord('A') + self.getKey()) % 26 + ord('A')) + cipher[i+1:]
        return cipher

    def decode(self):
        plain = self.getCipher().lower()
        for i in range(0, len(plain)):
            plain = plain[:i] + chr((ord(plain[i]) - ord('a') - self.getKey() + 26) % 26 + ord('a')) + plain[i+1:]
        return plain

class Substitution(Classical):
    """
    代换密码体制，key 应当为一个字典，键为 26 个小写字母，值为替换后的
    26 个大写字母，输入保证代换表为单射且为满射，同时列表中所有值都应当
    为字母，函数本身不做检查。
    """
    def encode(self):
        cipher = self.getPlain()
        for i, text in enumerate(cipher):
            cipher = cipher[:i] + self.getKey()[text].upper() + cipher[i+1:]
        return cipher

    def decode(self):
        key_negtive = {v: k for k, v in self.getKey().items()} # 通过字典推异构造 key 的逆映射
        plain = self.getCipher()
        for i, text in enumerate(plain):
            plain = plain[:i] + key_negtive[text].lower() + plain[i+1:]
        return plain

class Affine(Classical):
    """
    仿射密码体制，key 应该为一个列表，列表中第一个元素表示线性变换的系数
    a，第二个元素表示线性变换的常数 b，输入保证正确性，不检查。
    """
    def encode(self):
        cipher = self.getPlain().upper()
        for i in range(0, len(cipher)):
            cipher = cipher[:i] + chr(((ord(cipher[i]) - ord('A')) * self.getKey()[0] + self.getKey()[1]) % 26 + ord('A')) + cipher[i+1:]
        return cipher

    def decode(self):
        plain = self.getCipher().lower()
        key_nagtive = cryptomath.ext_euclid(self.getKey()[0], 26)[1] % 26 # 扩展欧几里得算法求乘法逆元
        for i in range(0, len(plain)):
            plain = plain[:i] + chr(((ord(plain[i]) - ord('a') - self.getKey()[1]) * key_nagtive) % 26 + ord('a')) + plain[i+1:]
        return plain

class Vigenere(Classical):
    """
    维吉尼亚密码体制，key 应为一个列表，列表长度为分组长度，列表每一项
    表示加密的移位长度
    """
    def encode(self):
        cipher = self.getPlain().upper()
        len_key = len(self.getKey())
        for i in range(0, len(cipher)):
            cipher = cipher[:i] + chr((ord(cipher[i]) - ord('A') + self.getKey()[i % len_key]) % 26 + ord('A')) + cipher[i+1:]
        return cipher

    def decode(self):
        plain = self.getCipher().lower()
        len_key = len(self.getKey())
        for i in range(0, len(plain)):
            plain = plain[:i] + chr((ord(plain[i]) - ord('a') - self.getKey()[i % len_key] + 26) % 26 + ord('a')) + plain[i+1:]
        return plain

class Hill(Classical):
    """
    希尔密码体制，key 为一个矩阵或二维列表
    """
    def encode(self):
        cipher = self.getPlain().upper()

        # 原文的向量化
        cipher = list(cipher)
        cipher = [ord(i) - ord('A') for i in cipher]

        foo = [] # 词穷，用来储存分组的向量
        temp = []

        for i in cipher:
            temp.append(i)
            if len(temp) == len(self.getKey()[0]):
                foo.append(temp)
                temp = []
        cipher = ''

        for i in foo:
            sss = numpy.dot(i, self.getKey()) % 26 + ord('A')
            sss = [chr(i) for i in sss]
            cipher += ''.join(sss)
        return cipher

    def decode(self):
        key_negtive = cryptomath.inverse_mat(self.getKey()) % 26
        plain = self.getCipher().lower()

        # 原文的向量化
        plain = list(plain)
        plain = [ord(i) - ord('a') for i in plain]

        foo = []
        temp = []

        for i in plain:
            temp.append(i)
            if len(temp) == len(self.getKey()[0]):
                foo.append(temp)
                temp = []
        plain = ''

        for i in foo:
            sss = numpy.dot(i, key_negtive) % 26 + ord('a')
            sss = sss.astype(int)
            sss = [chr(i) for i in sss]
            plain += ''.join(sss)
        return plain

class Permutation(Classical):
    """
    置换密码体制，密钥是置换表，字典类型
    """
