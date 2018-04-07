import sklearn.datasets as datasets
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

#データの読み込み
iris = datasets.load_iris()

#種類が２であるものを捨てる
data = iris.data[iris.target != 2]
target = iris.target[iris.target != 2]

#ロジスティック回帰による学習と黄砂検定による評価
logi = LogisticRegression()
score = cross_validation.cross_val_score(logi,data,target,cv=5)

print(score)
