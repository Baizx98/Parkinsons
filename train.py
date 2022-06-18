import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


# 读取数据
# 查看数据信息
df = pd.read_csv('parkinsons.data')
print(df.tail())
df.describe()
df.info()
print(df.shape)

# 提取特征和健康状态
features = df.loc[:, df.columns != 'status'].values[:, 1:]
labels = df.loc[:, 'status'].values
# 统计健康和帕金森人数
print(df['status'].value_counts())

# 特征归一化
scaler = MinMaxScaler((-1, 1))
x = scaler.fit_transform(features)
y = labels

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)

# 训练模型
model = XGBClassifier()
model.fit(x_train, y_train)
# 获取预测值
y_prediction = model.predict(x_test)
# 输出准确率
print("Accuracy Score is", accuracy_score(y_test, y_prediction)*100, "%")
