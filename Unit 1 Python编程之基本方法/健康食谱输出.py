# 健康食谱输出
# 列出5种不同的食材，请输出它们可能组成的所有菜式名称。

diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))

'''
该代码有误，会出现重复菜品的情况。
该计算应为数学组合计算：
C(n,m)
组合的定义：
从n个不同元素中，任取m(m≤n）个元素并成一组，
叫做从n个不同元素中取出m个元素的一个组合；
从n个不同元素中取出m(m≤n）个元素的所有组合的个数，
叫做从n个不同元素中取出m个元素的组合数，用符号 C(n,m) 表示。
'''
