##一个将日语文本转化为罗马音/平假名/片假名的API
---------
# xnkakasi 日语文本转化

一个将日语文本转化为罗马音/平假名/片假名的API
使用python库pykakasi来完成转化过程
其实就是用node.js调用python，用node.js启动一个服务器来转化日语文本
（实际上是我太菜，用不来python的flask，所以我才用这个似乎奇葩的方法来实现转化功能）

### 环境要求
需要部署node.js与python3.6+环境
python需要安装pykakasi库

### 安装/使用
忽略Node.js和Python的安装过程

1. 在pip中安装pykakasi

   ` pip install pykakasi `

2. 下载文件并解压

3. 在文件夹路径中打开终端

   ` npm install `

4. 现在部署已经完成 

5. 启动Node服务器 (默认端口是 3000, 可以在main.js中修改)

   ` node main.js `

6. 在浏览器中测试 (GET 方法)

> http://127.0.01:3000/user?content=大丈夫&mode=ToRoma 

"大丈夫" 可以替换为自己想转换的文本
"ToRoma" 意味着将文本转换为罗马音, 可以用"ToHira" 转换为平假名，用 “ToKana” 转换为片假名。


| 参数 | 值 | 介绍 |
| -- | -- | -- |
| content | 日语文本，如 "大丈夫" | 需要被转换的文本|
| mode | ToRoma/ToHira/ToKana | 转换模式，不输入的话默认为罗马音|

### 注意
- 返回值是json，如下:

  > {"url":"/user?content=%E5%A4%A7%E4%B8%88%E5%A4%AB","rText":"大丈夫","output":"daijoubu \r\n"}

- 这个API的默认方法是GET. 你也可以用POST，但是现在还不完善，过段时间我会完善下

- 如果不得不用POST, 可以在POST内容中传入需要转化的文本，然后得到文本转化的罗马音。 （现在POST方法只支持罗马音）返回值是纯文本，不是json。

- 运行目录下会有一个data.txt的文本文件，用来从javascript向python传递原文本。


-------------
-------------

# xnkakasi
An api converting Japanese text to Roma/Hiragana/Katakana.
Using pykakasi (a python lib) to finish the process of converting.
I just use node.js to Call the python file so that I can use the method of node.js to launch a server which can help me convert the Japanese text.
(Actually I didn't manage to learn the flask, so I continue my project in the way.)

------
### Environment
Need node.js and python3.6+
pykakasi (a python lib)

### Install/Use
Ignore the process of installing node.js and python

1. install pykakasi in pip

   ` pip install pykakasi `

2. download the file and upzip it

3. open the terminal in the dir

   ` npm install `

4. now the deployment is over 

5. launch the node server (default port is 3000, you can change it in file "main.js")

   ` node main.js `

6. test it on your browser (GET method)

> http://127.0.01:3000/user?content=大丈夫&mode=ToRoma 

"大丈夫" in the "content" can be replaced by your own text
"ToRoma" means converting text to roma, you can use "ToHira" to convert it to Hiragana and “ToKana” to convert it to Katakana.


| Arguments | Value | Introduction |
| -- | -- | -- |
| content | any japanese text like "大丈夫" | The text need to be converted|
| mode | ToRoma/ToHira/ToKana | The convert mode.If you don't input,  the default mode is ToRoma|

### Tips
- The return value is json like this:

  > {"url":"/user?content=%E5%A4%A7%E4%B8%88%E5%A4%AB","rText":"大丈夫","output":"daijoubu \r\n"}

- The default method of this API is GET. You can also use POST but it's not supported well at present. I'll update it in the near future.

- If you have to use POST in this imperfect version, you can put your text in the content of POST, and you will get its roma in return. (Now POST support ToRoma only). The return value is text.

- There will be a file called "data.txt" in the running path. It's used to convey text from javascript to python.

------------
