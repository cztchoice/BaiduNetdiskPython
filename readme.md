## 百度网盘Python客户端

自己手动写了BaiduOpenAPI/BaiduNetdisk.py和test.py，修改了BaiduOpenAPI/BaiduUtils.py（增加一个函数使得能够进行upload文件的操作），其他的文件是百度提供的OpenAPI样例。

本来自己是打算实现百度网盘的Linux客户端的，但是后来发现**百度网盘不提供对网盘上所有目录的访问权限**，只能访问"/apps/$app_id/"这个目录的访问权限，虽然安全性高了，但是对我没有什么意义了。所以就放弃了，然后放在这儿谁想当作样例可以用一下

我刚开始还纳闷他的access_token为什么可以那么久（最长10年，通过refresh_token刷新）


已实现功能：

<code>
BaiduNetdisk.quota()
</code>

<code>
BaiduNetdisk.upload\_single\_file()  大文件需要等待
</code>

test.py中

authorization code需要通过复制网址到浏览器打开，得到，然后手动输入的，只需一次，1个月内不用修改

但是，refresh token没有使用，需要手动删除token_data.txt重新获得authorization code，或者利用BaiduOpenAPI/BaiduOauth2里的函数调用一下即可