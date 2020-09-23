# 分治限界法(一般队列)实现装载问题
import pdb
# 创建队列元素
class QueueItem:
    # 根据节点信息赋值
    # i表示第几层，cw表示当前载重，x解空间树
    def __init__(self, i, cw, x):
        self.i = i
        self.cw = cw
        self.x = [i for i in x]
# 打印当前队列中元素
def printItem(queue):
    for item in queue:
        print(item.i, item.cw, item.x)


# 判断是进队列还是更新当前最优值,记录当前解x
def EnQueue(queue, x, wt, i, n):  # 使用QueueItem数据结构
    global bestw
    if (i == n - 1):
        # 叶子结点
        if (wt >= bestw):  # 这里的'>='号很重要
            bestw = wt
            print("当前最优解:", str(x))
            print("当前最优载重:", str(bestw))
    else:
        item = QueueItem(i, wt, x)
        queue.insert(0, item)

# 从尾部出队列
def DeQueue(queue):  # 使用QueueItem数据结构
    return queue.pop()
def BranchBound():  # 求装载重量，限界右子树，同时求装载物品是哪些

    global n  # 物品个数
    global x  # 解空间树表征数组
    global w  # 物品重量数组
    global c  # 容量
    global restw  # 剩余重量
    global cw  # 当前载重量
    global bestw  # 当前最优装入重量

    queuelist = []  # 队列,从头部插入，从尾部取出
    item = QueueItem(-1,-1,x)
    queuelist.insert(0, item)
    i = 0  # 第一层
    restw = restw - w[0]  # 当前剩余重量（即物品全部重量）减去第一个物品重量
    while (True):
        if item.i != -1:
            x = item.x
            cw = item.cw
        sum_w = cw + w[i]
        if sum_w <= c:
            if bestw < sum_w:
                bestw = sum_w
            x[i] = 1
            EnQueue(queuelist, x, sum_w, i, n)
        if cw + restw >= bestw:
            x[i] = 0
            EnQueue(queuelist, x, cw, i, n)
        item = DeQueue(queuelist)
        if item.i == -1:
            if len(queuelist) == 0:
                print("最优装载重量为：", str(bestw))
                return
            else:
                queuelist.insert(0,QueueItem(-1,-1,x))
                item = DeQueue(queuelist)
                i = i + 1
                restw = restw - w[i]

if __name__ == '__main__':
    # 3-3,2,2-4
    # 3-2,2,3-4
    # 5-3,2,2,1,1-6
    glist = input().split('-')
    # 物品个数
    n = int(glist[0])
    # 容量
    c = int(glist[len(glist) - 1])
    items = glist[1].split(',')
    # 物品重量数组
    w = [int(item) for item in items]
    # 当前载重量
    cw = 0
    # 当前剩余重量，初始等于全部物品重量
    restw = 0
    for i in w:
        restw = restw + i
    # 当前最优装入重量
    bestw = 0
    # 解空间树表征数组
    x = [0 for i in range(n)]
    print('物品个数:', str(n))
    print('物品重量数组:', str(w))
    print('容量:', str(c))
    BranchBound()
