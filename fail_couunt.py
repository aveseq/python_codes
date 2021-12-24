math=set()
phy=set()
che=set()
cs=set()
mm=int(input())
for i in range(0,mm):
    val=input()
    math=math|{val}
mp=int(input())
for i in range(0,mp):
    val=input()
    phy=phy|{val}
mc=int(input())
for i in range(0,mc):
    val=input()
    che=che|{val}
mcs=int(input())
for i in range(0,mcs):
    val=input()
    cs=cs|{val}
fails=math|phy|che|cs
print(len(fails))