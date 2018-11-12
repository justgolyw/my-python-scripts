这是一个将TestLink上的测试用例以xml的形式导出到本地后再转换为excel形式的脚本
包含两个文件：
Xml2Excel.py 是xml转成excel的逻辑代码
window.py 是UI代码（window2.py是不同的UI代码）
后续还可以进行优化
demo.xml 是测试用例
template.xlsx 是excel 模板

打包命令：在window.py所在的文件夹下执行如下命令即可打包成exe文件
	C:\python36\Scripts\pyinstaller.exe -F window.py

打包多个文件：1个python文件调用了其他多个python文件或者其他的资源文件（比如.jpg/.xlsx）
(1)pyi-makespec window.py
生成window.spec文件，修改spec文件
（1）第一个列表中写所有的py文件，与window.py一个在同一个目录下的可以直接写文件名，不同目录下的需要写完整的文件路径。

（2）datas是中的元素是tuple类型，tuple的第一个参数是python项目中资源文件（非py文件）的路径，第二个参数是资源的名字
注意：在python 文件中用到资源的地方也需要改写为完整的路径名：
shutil.copyfile(os.path.abspath(r"C:\Users\yangwei.li\PycharmProjects\ShowMeTheCode\xml2excel\template.xlsx"),path)

3.用之前配置的spec文件制作exe： 
C:\python36\Scripts\pyinstaller.exe -F window.spec(或pyinstaller -f window.spec)
或者pyinstaller -d window.spec