# Crypto lib.

这是一个用 Python3 实现的密码库。

写这个库主要是为了写密码学的作业。目前只完成了古典密码学的部分，其他部分以后再写。

`classical.py` 包含了所有古典密码体制类，它们的公共基类 `Classical` 定义了所有密码体制的公共接口。

`cryptomath.py` 包含古典密码体制中所用到的数学。

`multiply.py` 是我的作业……同时也是一个简短的库的使用说明。

`unit_testing.py` 是临时写的用来测试古典密码体制类的。



## 乘积密码的加密顺序

```flow
op1=>operation: 代换密码体制
op2=>operation: 仿射密码体制
op3=>operation: 维吉尼亚密码体制
op4=>operation: 希尔密码体制

op1->op2->op3->op4
```

