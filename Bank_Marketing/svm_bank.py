import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn import metrics


def makefeature(x):
    #数値変数のスケーリング
    cn_num = ["age","balance","day","duration","campaign","pdays","previous"]
    x_num = x[cn_num]
    x[cn_num] = (x_num - x_num.mean())/x_num.std()
    #ダミー変数への変換
    x_dum = pd.get_dummies(x)
    return x_dum

#データの読み込み
bank = pd.read_csv("data/bank-full.csv",sep=";")
features,label = makefeature(bank.drop('y',1)),bank.y

#訓練データとテストデータの作成
random_state = np.random.RandomState(123)
X_train,X_test,y_train,y_test = train_test_split(features,label,test_size=.3,random_state=random_state)

#RBFカーネルのSVMによる予測モデル構築
clf = svm.SVC()
clf.fit(X_train,y_train)

#クラスラベルの予測
pred = clf.predict(X_test)

#クラスごとの適合率、再現率、F値の算出
print(metrics.classification_report(y_test,pred,target_names=["no","yes"]))
