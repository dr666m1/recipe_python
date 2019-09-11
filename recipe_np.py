import numpy as np

#==========
# numpy
#==========

#===== コンストラクタ =====
#=== 基本
np.array([x for x in range(5)])
np.array([x for x in range(5)],dtype='float32')
#bool,int,float,complex覚えておけばひとまずOK
#あまり使わないかもしれないが、unicodeという文字列型もある

#=== 同じ要素で埋める
np.zeros((2,3))
np.ones((2,3))
np.full((3,5),3.14)

#=== 連番的な
np.arange(0,20,2)
#np.linspace(0,1,5)#

#=== ランダム
np.random.random((3,3))#[0,1]の一様分布
#np.random.rand(3,3)#上に同じ
np.random.normal(0,1,(3,3))
np.random.randint(0,10,(3,3))
np.random.choice(5,3)
np.random.choice(["a","b","c"],3)

rng=np.random.RandomState(0)#乱数生成のためのclass
rng.randint(0,10,(3,3))

#=== その他
#np.eye(3)#単位行列
#np.empty((3,3))#初期化しない配列

#===== 属性 =====
x=np.array([x for x in range(6)]).reshape((2,3))
dir(x)
#=== 形状
x.shape
#x.ndim
#x.size

#=== その他
x.dtype
#x.itemsize#要素のbytes
#x.nbytes#配列のbytes

#===== アクセス =====
x=np.array([x for x in range(18)]).reshape((3,6))
x
y=np.arange(5)
z=np.array([True,False,True,False,True])
#=== ピンポイント
x[0,2]
x[-1,-1]
x[[0,1],[0,1]]#x座標とy座標の配列を使って複数指定
x[np.array([0,1])[:,np.newaxis],[0,1]]
#インデクスをブロードキャストすることができる
#形状はインデクス配列に従う

#=== スライシング
x[:2,:]
#x[:2]#上の省略形（行の抽出の場合のみ可）
x[:2,1:3]
#x[0,1::2]#列はインデクス1から1つおきという指定
#x[0,::-1]#列は逆順という指定

y[z]#論理値を使った指定も可能

#===== 変形 =====
np.arange(6).reshape((2,3))
#order="C"...番号の大きな軸から埋める
#order="F"...番号の大きな軸から埋める
np.arange(6)[:,np.newaxis]

#===== 連結・分割 =====
#=== 連結
x=np.zeros((2,3))
y=np.ones((2,3))

#np.concatenate([x,y],axis=0)#axis=0は省略可能
#np.concatenate([x,y],axis=1)
np.vstack([x,y])
np.hstack([x,y])

#=== 分割

#===== 演算 =====
x=np.arange(6)
y=np.arange(12).reshape((3,4))
z=np.random.choice([True,False],3)

#=== 集約
#sum(),max(),min()と書くよりも速い
#+,*,/といった演算子はそのまま使ってもnp.addとかと変わらないから
np.sum(x)
np.max(x)
np.min(x)
np.mean(x)
np.var(x)
np.std(x)
np.sum(z)#Rと同様に、0,1で計算される
np.any(z)
np.all(z)
#ddof引数で不偏<-->標本の切り替えができるが、デフォルトは標本らしい
#np.mean((x-np.mean(x))**2)
#(np.mean((x-np.mean(x))**2))**(1/2)

#=== 集約（行・列ごと）
np.sum(y,axis=0)
np.sum(y,axis=1)

#=== 論理演算
np.array([True,True,False])&np.array([False,True,False])#論理積
np.array([True,True,False])|np.array([False,True,False])#論理和
np.array([True,True,False])^np.array([False,True,False])#排他的論理和
~np.array([True,True,False])#否定
#and,orというキーワードがあるらしいが、基本的には使わない

#===== ソート =====
x=np.array([4,5,3,1,2])
y=np.random.randint(0,100,(5,5))
#=== 一次元
np.argsort(x)#Rでいうorder()
x.argsort()#上に同じ

np.sort(x)#ソートされた配列を別に取得
x.sort()#ソートされた状態で上書き

#=== 多次元
#np.sort(y,axis=0)
#行・列内をソートする
#行・列の関係が崩れるからあまり使わないかと

#===== 構造化配列 =====
#=== コンストラクタ
x=np.zeros(4,dtype=[("name","U10"),("age","i4"),("weight","f8")])
#x=np.zeros(4,dtype={"names":("name","age","weight"),"formats":("U10","i4","f8")})#上に同じ
#y=np.zeros(4,dtype=("U10,i4,f8"))#名前の指定が不要な場合
x["name"]=["a","b","c","d"]
x["age"]=[1,2,3,4]
x["weight"]=[10,20,30,40]

#=== アクセス
x["name"]
x[:2]["age"]

#=== レコード配列型


#===== その他 =====
x=np.array([x for x in range(9)]).reshape((3,3))
y=x.copy()#値渡し









