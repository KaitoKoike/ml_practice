import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import ensemble
from sklearn import metrics

def makefeature(x):
    #数値変数のスケーリング
    cn_num = ["age","balance","day","duration","campaign","pdays","previous"]
    x_num = x[cn_num]
    x[cn_num] = (x_num - x_num.mean())/x_num.std()
    #ダミー変数への変換
    x_dum = pd.get_dummies(x)
    return x_dum


bank = pd.read_csv("data/bank-full.csv",sep=";")
features,label = makefeature(bank.drop('y',1)),bank.y
random_state = np.random.RandomState(123)
X_train,X_test,y_train,y_test = train_test_split(features,label,test_size=.3,random_state=random_state)

#ランダムフォレストによる予測モデルの構築
random_state = np.random.RandomState(123)
clf = ensemble.RandomForestClassifier(n_estimators=500,random_state=random_state)
clf.fit(X_train,y_train)
#クラスラベルの予測
pred=clf.predict(X_test)

#クラスごとの適合率、再現率、F−値の算出
print(metrics.classification_report(y_test,pred,target_names=["no","yes"]))
