# python-exercises

 一些有趣的python题目合集

 要是有啥好题目or解题方法可以联系我

## 最大方格
（1）编程实现：

小明有一张N*M的方格纸，且部分小方格中涂了颜色，部分小方格还是空白。

给出N（2≤N≤30）和M（2≤M≤30）的值，及每个小方格的状态（被涂了颜色小方格用数字1表示，空白小方格用数字0表示），请帮助小明找出最大的矩形空白区域，并输出该矩形空白区域由多少个小方格组成。

例如：N=4，M=5，4*5的方格纸中每个小方格的状态如下图：

最大的空白区域由6个小方格组成（红色框区域）。

输入描述

第一行输入两个正整数N和M（2≤N≤30，2≤M≤30），分别表示方格纸的行数和列数，两个正整数之间以一个空格隔开

第二行开始输入N行，每行M个整数（整数为1或者0），1表示涂色方格，0表示空白方格，整数之间以一个空格隔开

输出描述

输出一个整数，表示最大矩形由多少个小方格组成（如果没有空白小方格，输出0）

样例输入

4 5

1 1 0 0 0<br>
1 0 1 0 0<br>
0 0 0 1 1<br>
0 0 0 1 0<br>

样例输出

6

## 挑选礼物

编程实现：

期末考试小明取得了优异的成绩，妈妈为鼓励小明再接再厉，在网购平台指定了N（2≤N≤50）件礼物供小明挑选。挑选前妈妈提出了以下要求：

1. 每种礼物只能挑选1件；

2. 所挑选的礼物总价格不能大于V（1≤V≤100）。

已知N件礼物中每件礼物的价格和小明对每件礼物的喜爱值（喜爱值越大喜爱程度越高），请你帮助小明挑选礼物，使得挑选的所有礼物在满足要求的前提下，总的喜爱值最大，并输出最大喜爱值。

例如：

N = 3，V=5，3件礼物的价格和喜爱值分别为（1，2），（2，4），（3，3）。

可挑选第二件礼物（2，4）和第三件礼物（3，3），总价格为5（5=2+3），总喜爱值为7（7=4+3），总价格不大于5且喜爱值最大，输出7。

输入描述

第一行输入两个正整数N（2≤N≤50）和V（1≤V≤100），分别表示指定的礼物数量和所挑选的礼物总价格不能大于的值，正整数之间以一个英文逗号隔开

第二行开始，输入N行，每行输入两个正整数J（1≤J≤V）和K（1≤K≤100），分别表示每件礼物的价格和喜爱值，正整数之间以一个英文逗号隔开

输出描述

输出一个整数，表示在满足题目要求下的最大喜爱值

样例输入

3,5

1,2

2,4

3,3

样例输出

7

## 走迷宫

设计一个走迷宫的代码
