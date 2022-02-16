# python-plotting-commands

A collection of commonly used python plotting commands.

### 2022年2月更新：Win10安装Python3和绘图包 & 故障排除方法

#### 一、Win10安装Python3和绘图包

1. 官网 (https://www.python.org/downloads) 下载对应安装包，选择安装位置，勾选“将python加入环境变量”。命令行输入：python -V，显示版本号：Python 3.10.2 则说明安装成功。命令行运行脚本的方式：python xxx.py。
2. 运行 pip install matplotlib 安装绘图包，它所依赖的模块如numpy等会被自动安装。
3. Idea安装python插件，可方便编辑和运行脚本。

#### 二、中文字体显示为方块的问题

1. 输入 import matplotlib, print(matplotlib.matplotlib_fname())

   显示 py-install-dir\lib\site-packages\matplotlib\mpl-data\matplotlibrc，

   则 py-install-dir\Lib\site-packages\matplotlib\mpl-data\fonts\ttf 为字体路径，

   将 SimHei.ttf 文件放入其中。

2. 修改 matplotlibrc 文件：

   找到文件中 font.serif 和 font.sans-serif 所在位置，在第一位添加 SimHei。

#### 三、坐标轴上的负号显示为方块的问题

1. 修改 matplotlibrc 文件：

   找到文件中 axes.unicode_minus，将其值改为False。


