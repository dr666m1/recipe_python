#==========
# import
#==========

#公式docのInstallationの、jupyter notebookのパターンを参照
#condaではなくpipを使ってみた（そっちの方が新しいversionになる？）
import altair as alt
from vega_datasets import data
import pandas as pd

#==========
# 導入
#==========

dat=pd.DataFrame({
  "a":list("cccdddeee"),
  "b":[2,7,4,1,2,6,8,4,7]
})
chart=alt.Chart(dat).configure(background="white") #configure()...設定を書き加えて、Chartクラスを返すようだ
chart.mark_point().encode(
  x="a"
  , y="b"
)
chart.mark_bar().encode(
  x="a"
  , y="average(b)"
) #集約関数的なものを使える

chart.mark_bar(color="firebrick").encode(
  alt.X("average(b)",title="this is title")
  , y="a"
) #データ型でどちらを棒にするか判断してくれているようだ

#==========
# 基本
#==========


#===== 散布図 =====

iris=data.iris()
alt.Chart(iris).configure(background="white").mark_point().encode(
  x="petalLength"
  , y="petalWidth"
  , color="species"
)
#===== 積上縦棒 =====
source=data.barley()
source.head()
alt.Chart(source).configure(background="white").mark_bar().encode(
  x="variety"
  , y="sum(yield)"
  , color="site"
)
