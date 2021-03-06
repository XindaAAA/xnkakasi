import sys
import os,io
import pykakasi

kks = pykakasi.kakasi()

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
rText = "none"
if len(sys.argv)<=1:
    print ("未输入必选参数！")
    sys.exit() #如果未输入必选参数则退出
tMode = sys.argv[1] #读取参数中的转化模式
if tMode == "-ToRoma":
    ttMode="hepburn" #罗马音模式
elif tMode == "-ToHira":
    ttMode="hira" #平假名模式
elif tMode == "-ToKana":
    ttMode="kana" #片假名模式
else:
    ttMode="hepburn" #默认输出罗马音

with open("data.txt",encoding="utf-8") as f: #读取js放入文件的文本数据
    rText = f.read()
textList = rText.split("\n")

res=""
for x in textList:
    t=""
    a = kks.convert(x) #将文本进行kakasi转化
    for item in a:
        t+=item[ttMode]+" " #利用kakasi的分词功能，词词间添加空格
    res+=t+"\n"
print(res)
