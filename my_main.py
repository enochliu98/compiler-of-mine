################################
################################
#####    NFA to DFA      #######
#####    by:lyz          #######
################################
################################

## 引入行坐标和纵坐标，用字母表示，
# 列用大写，行用小写（暂时不实现）
# 在程序中，行坐标和列坐标都用数字表示，为了便于实现矩阵
# 输入为一个矩阵


#############矩阵的索引从0开始



#################数据结构########################
# nfa 矩阵(二维）
nfamatrix=[[[],[]],[[],[]],[[3],[]],[[],[]],[[],[5]],[[],[]],[[],[]],[[8],[]],[[],[9]],[[],[10]],[[],[]]]
#nfa的尺度 输入后的得到一个二维的矩阵 假设为m行n列
m=11
n=2
# dfa 矩阵（二维）
dfamatrix=[]
# 存储e弧（一维）
e=[[1,7],[2,4],[-1],[6],[-1],[6],[1,7],[-1],[-1],[-1],[-1]]
#定义一个list，用于记录新的矩阵中所有的元素
mylist=[]
#用来存矩阵的间接结果
dfaline=[]
#action用来存矩阵的元素
action=[]


##############其余重要的变量####################
#用来指出初始状态
#nfa中初始状态可以是一个集合
#这里S为一个计集合
S=[0]
#终止状态也是一集合
V=[10]




from NFAtoDFA import NFA_DFA


NFA_DFA()