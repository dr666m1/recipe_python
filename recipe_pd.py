import numpy as np
import pandas as pd
import seaborn as sns
#==========
# pandas
#==========

#===== Series =====

#=== コンストラクタ
x=pd.Series([0,0.5,1,1.5,2])
y=pd.Series([0,0.5,1,1.5,2],index=[0,2,4,6,8])
z=pd.Series({"e":0,"d":0.5,"c":1,"b":1.5,"a":2})#辞書
mi=pd.Series({
    ("nigata",2000):100
    ,("nigata",2010):200
    ,("tokyo",2000):100
    ,("tokyo",2005):300
})#多階層インデクス

mi=pd.DataFrame(
    {
        2000:pd.Series({"nigata":100,"tokyo":200})
        ,2005:pd.Series({"tokyo":100})
        ,2010:pd.Series({"nigata":100,"tokyo":300})
    }
)
mi
mi=mi.stack()

#=== 属性
#dir(x)
x.values#ndarray
z.index#indexは勝手にソートされる
#z.keys()#上に同じ
#list(z.items())#参考まで
print(x.size,x.shape,x.ndim,x.dtype)#ndarrayとかなり重複する

#=== アクセス
#スライシング
#x[:2]#基本はndarrayと一緒
#y[1:4]
#y[6:8]#この範囲の要素はない
#z["a":"c"]

#ピンポイント
#y[4]#何番目、ではなくindexが一致する要素
#z["a"]

#label_location,integer_location
y.loc[0:8]#両端含む
y.iloc[0:3]#3は含まず
mi.loc[:,:2005]#単純に次元が追加されたと解釈するとよい

#データ追加
z["aa"]=9#追加しただけではソートされない

#=== 演算
x=pd.Series([0,0.5,1,1.5,2])

print(x.sum(),x.mean())


#=== 文字列操作
x=pd.Series(["dairyou","taika","ohmi","taisei"])

x.str.len()
x.str.contains("ai")#re.search()を適用しているらしい
#上記以外にもメソッドいっぱいあるから要確認

#=== 時系列データ型
pd.to_datetime(["2015-01-01","2016-01-01"])#dtypeはdatetime64らしい
pd.to_datetime(["2015年01月01日","2016年01月01日"],format="%Y年%m月%d日")#書式の指定


#=== ソート　※スライシングを行うためには重要
z.sort_index()#上書きはされない

#===== コンストラクタ =====
#=== Seriesから
pd.DataFrame(pd.Series([0,1,2]))
pd.DataFrame({"salary":pd.Series([100,200,300]),"age":pd.Series([20,21,22])})
pd.DataFrame({
    "salary":pd.Series({"a":100,"b":200,"b":300,"c":300})
    ,"age":pd.Series({"b":21,"b":23,"b":21,"d":24,"e":25,"e":20})
})
#上は悪い例
#indexの欠損はNaNで埋まるが、Series内のindexの重複は挙動が不明だから避けたい

#=== ndarrayから
pd.DataFrame(np.random.random((3,2)),columns=["a","b"],index=[1,2,3])
#pd.DataFrame(np.zeros(3,dtype=[("name","U10"),("age","i4")]))#構造化配列から

#=== 辞書のリストから
pd.DataFrame([{"a":i,"b":i*2,"c":i*3} for i in range(5)])

#=== 多階層インデクス
mi=pd.DataFrame(np.hstack([np.random.random((4,2)),np.array(["a","a","b","b"])[:,np.newaxis],np.array([1,2,1,2])[:,np.newaxis]]),columns=["c1","c2","class","number"])
mi=mi.set_index(["class","number"])

#===== 属性 =====
data=pd.DataFrame(np.random.random((3,2)),columns=["a","b"],index=[1,2,3])
mi=pd.DataFrame(np.hstack([np.random.random((4,2)),np.array(["a","a","b","b"])[:,np.newaxis],np.array([1,2,1,2])[:,np.newaxis]]),columns=["c1","c2","class","number"])
mi=mi.set_index(["class","number"])

data.values#ndarray
data.columns
data.index
mi.index.names#levelとして指定するときに便利かも

#===== 変形 =====
data=pd.DataFrame(np.random.random((3,2)),columns=["a","b"],index=[1,2,3])
mi=pd.DataFrame(np.hstack([np.random.random((4,2)),np.array(["a","a","b","b"])[:,np.newaxis],np.array([1,2,1,2])[:,np.newaxis]]),columns=["c1","c2","class","number"])
mi=mi.set_index(["class","number"])
#=== 基本
data.T
data.stack()
data.stack().unstack()
#levelで階層を指定できるらしい

#=== インデクス関係
mi.reset_index("number")#index->列
mi.reset_index("number").set_index(["number"])#列->index
mi.reset_index("number").set_index(["number"],append=True)

#===== 結合 =====
x=pd.DataFrame(np.random.randint(0,10,(3,3)),columns=["A","B","C"],index=[1,2,3])
y=pd.DataFrame(np.random.randint(0,10,(3,3)),columns=["B","C","D"],index=[3,4,5])
a=pd.DataFrame({
    "name":["a","b","c","d"]
    ,"year":[2010,2012,2018,2010]
    ,"salary":[2010,2012,2018,2010]
})
b=pd.DataFrame({
    "name":["e","b","b","d"]
    ,"year":[2010,2012,2012,2012]
    ,"class":[1,2,3,4]
})

#=== concat
#基本
pd.concat([x,y])#x.append(y)#3つ以上の場合に対応ができない
pd.concat([x,y],axis=1)

#インデクスまわり
try:
    pd.concat([x,y],verify_integrity=True)#indexの重複を許さない
except ValueError as e:
    print("ValueError":,e)
pd.concat([x,y],ignore_index=True)#新しいindexが付与される
#pd.concat([x,y],keys=["from_x","from_y"])#多階層インデクスにして対応

#columnsまわり
pd.concat([x,y],join="inner")#両方に存在するcolumnのみ残る
#pd.concat([x,y],join_axes=[x.columns])#文字列で指定できないらしく使い勝手が悪い

#=== merge　※SQL的な操作
pd.merge(a,b)#両方に存在するcoloumnsをすべて条件にするinner_join
pd.merge(a,b,on="name")
pd.merge(a,b,on="name",how="left")
pd.merge(a,b,on="name",how="outer")#full_outer

#pd.merge(a,b,on="name",suffixes=["_a","_b"])#列名の末尾を操作できる
pd.merge(a,b,left_on="name",right_on="name")
pd.merge(a,b,left_index=True,right_index=True)#indexを条件に結合。多階層の場合はすべてマッチする必要あり

a.join(b,lsuffix="_a",rsuffix="_b")#上に同じ。suffixを指定しないとエラー

#===== アクセス =====
area=pd.Series({"nigata":12583,"tokyo":2187,"kyoto":4613})
pop=pd.Series({"nigata":2245057,"tokyo":13843403,"kyoto":2591779})
data=pd.DataFrame({"area":area,"pop":pop})
t=pd.DataFrame({"value":range(62)},index=pd.date_range("2018-12-01","2019-01-31",freq="1D"))

#=== Seriesの選択
data["area"]
#data.area#上に同じだが非推奨
data[["area","pop"]]

#=== label_location,integer_location　※ixは使わない方針
data.loc[:"nigata",["pop","area"]]
data.loc[data["area"]>=5000,:]
#論理値による指定はloc
#でもSeriesはloc,ilocなしで指定する必要があるかも
data.iloc[:2,:]
t.loc["2018",:]#2018年のレコードがすべて抽出できる

#=== 多階層
mi
mi.loc["a","c1"]
mi.loc[("a",1),:]
mi.loc[pd.IndexSlice[:,1],:]#上で"a"に加えて"b"も選択したい場合、タプル内で":"が使えないためこのように書く
mi.loc[(["a","b"],1),:]#別解。だがスライシングは使えていない

#=== 追加
data["density"]=data["pop"]/data["area"]

#===== 演算 =====
A=pd.DataFrame(np.random.randint(0,20,(2,2)),columns=list("AB"))
B=pd.DataFrame(np.random.randint(0,10,(3,3)),columns=list("ABC"))
p=sns.load_dataset("planets")
p.head()
mi=pd.DataFrame(np.hstack([np.random.randint(0,10,(6,2)),np.array([1,1,1,2,2,2])[:,np.newaxis],np.array([1,2,3,1,2,3])[:,np.newaxis]]),columns=["c1","c2","class","number"])
mi=mi.set_index(["class","number"])

#=== DataFrame内の基本
#基本
A.sum()
A.sum(axis=1)
i=datasets.load_iris()
A.describe()#Rのsummary()に相当

#=== DataFrame内インデクスごと
mi
mi.sum(level="class")
mi.mean(level=["class","number"])#ちょっとcountだと動かなかったりと不安

#=== DataFrame内　groupby（特定の列の値ごと）
#集約
p.groupby(["method","number"]).mean()["distance"]
p.groupby(pd.cut(p["year"],[0,2000,9999])).mean()["distance"]#階級を作ってkeyに指定
p.groupby(pd.qcut(p["distance"],4)).mean()["year"]#階級を作ってkeyに指定
p.groupby("method").aggregate([np.max,np.min,np.sum])["distance"]#複数の集約関数を適用

#フィルタ
p.groupby("method").filter(lambda x:x["distance"].mean()>=1000)#having的な使い方だが、レコード単位で返ってくる
#lambda関数は論理値を返さないといけない

#変換
p.groupby("method").transform(lambda x:x-x.mean(0))#グループ化のkeyが消えてしまうが、どうしようもなさそう

#適用
p.groupby("method").apply(lambda x:x.iloc[0,:])#グループ化したDataFrameに対して好き放題できるイメージ
#lambda関数はスカラーかSeriesかDataFrameを返せばなんでもいけるらしい


#=== DataFrame内　時系列
# asfreq　※その気になればresampleですべて書ける

#df=pd.DataFrame({"value":range(1,32,2)},index=pd.date_range("2018-08-#01","2018-08-31",freq="2D"))
#df.asfreq("5D")["value"]#データの選択（存在しない場合はNaN）
#df.asfreq("5D",fill_value=0)
#df.asfreq("5D",method="ffill")#逆はbfill
#df.asfreq("1W-WED")

# resample　※使い方はgroupbyに近い
df=pd.DataFrame({"value":range(9)},index=pd.date_range("2018-08-01","2018-08-05",freq="12H"))
df.resample("D").mean()["value"]
df.reset_index().resample("D",on="index").mean()#特定の列を指定
#df.resample("D").aggregate([np.sum])["value"]#applyとかも使える
df.resample("D").first()#asfreqはこれに近い
df.resample("D",label="left",closed="left").sum()#label（インデクスをどちらにするか）とclosed（閉区間をどちらにするか）は同じ引数を与えるのがわかりやすい
#asfreqには存在しない引数
df.resample("3H").first().ffill()#NaNが生じるのがだめなら穴埋めしてしまう
#DateTimeIndexResamplerクラスのメソッドでもうちょっと柔軟な補完もできそうだが挙動が不明だからここまで

# shift, tshift
# rolling ※移動平均
help(pd.DataFrame.rolling)

#=== DataFrame内　pivot
p.pivot_table("distance",index="method",columns="number")#デフォルトは平均値
p.pivot_table("distance","method","number",aggfunc=np.sum)

#=== Series間またはDataFrame間
A+B#列もインデクスも整列させられることに注意
A.add(B,fill_value=0)#NaNが嫌な場合は指定ができる

#=== SeriesとDataFrame間
B-B.iloc[0,:]
B.subtract(B["A"],axis=0)#列単位の操作は注意が必要




#===== 欠損値 =====
x=np.array([1,2,np.nan,4])
y=pd.DataFrame(x)
df=pd.DataFrame([
    [1,np.nan,2]
    ,[2,3,5]
    ,[np.nan,4,6]
])
#=== 演算
np.sum(x)
np.nansum(x)#SQLの集約関数的なイメージ

#=== 検出
y.isnull()
y.notnull()#~を使うこともできるはず

#=== 除外
y.dropna()
df.dropna()
df.dropna(axis=1)

#=== 補完
df.fillna(0)
#df.fillna(method="ffill")#forward_fill
#df.fillna(method="bfill",axis=1)#back_fill。方向も指定可


#===== ソート　※スライシングを行うためには重要 =====
data=pd.DataFrame(np.random.random((3,2)),columns=["a","b"],index=[1,2,3])
data.loc[0,:]=np.random.random((1,2))

data
data.sort_index()


#=== 読み込み
pd.read_csv("sample.csv")