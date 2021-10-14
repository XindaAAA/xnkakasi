import sys
import os,io
import pykakasi

kks = pykakasi.kakasi()

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
rText = "none"
if len(sys.argv)<=1:
    print ("未输入必选参数（文本）！")
    sys.exit() #如果未输入必选参数（文本）则退出
tMode = sys.argv[1] #读取第二个参数中的转化模式
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
    a = kks.convert(x) #再将分词后的文本进行kakasi转化
    for item in a:
        t+=item[ttMode]+" "
    res+=t+"\n"
print(res[0:len(res)-1])#去除末尾的\n