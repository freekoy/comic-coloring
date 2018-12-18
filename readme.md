# comic coloring 漫画自动上色

初衷：利用gan对抗网络给漫画上色

运行环境 python3 keras2.2.4

修改自
https://github.com/eriklindernoren/Keras-GAN/pix2pix

数据来源
参考https://zhuanlan.zhihu.com/p/25709644

1: 把图片放到imgs中

2: 运行create_data.py制作训练模型所需的数据

3: 运行pix2pix.py即可

效果如下：
![avatar](https://github.com/freekoy/comic-coloring/blob/master/infer.png)