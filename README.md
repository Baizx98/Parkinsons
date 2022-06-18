# 环境
- python 3.10
- panda
- sklearn
- xgboost

# 运行
修改```df = pd.read_csv('parkinsons.data')```中路径为数据集实际路径，然后在命令行中运行即可输出模型准确率。


```bash
python train.py
```

# 数据集
该数据集由31个人的一系列生物医学语音测量组成，其中23人患有帕金森综合征。数据表中的每一列都是一个特定的语音测量值，每一行对应这些人195个语音记录中的一组数据。这些数据的主要目的是根据“状态”栏区分健康人和帕金森病患者，健康状态栏设置为0，帕金森病状态栏设置为1。  
各种语音信号处理算法，包括时频特征、Mel倒谱系数（MFCC）、基于小波变换的特征、声带特征和TWQT特征，已被应用于帕金森病（PD）患者的语音记录，以提取PD评估的临床有用信息。  
**属性信息:**
- name - ASCll对象名称和记录编号
- MDVP:Fo(Hz) - 平均人声基频
- MDVP:Fhi(Hz) - 最大人声基频
- MDVP:Flo(Hz) - 最小人声基频
- MDVP:Jitter(%) , MDVP:Jitter(Abs) , MDVP:RAP , MDVP:PPQ , Jitter:DDP - 基频变化的几种测量方法
- MDVP:Shimmer , MDVP:Shimmer(dB) , Shimmer:APQ3 , Shimmer:APQ5 , MDVP:APQ , Shimmer:DDA - 振幅变化的几种测量方法
- NHR , HNR - 声音中噪声与音调成分之比的两种测量方法
- status - 对象的健康状态 (1) - 帕金森患者, (0) - 健康
- RPDE , D2 - 两个非线性动态复杂性度量
- DFA - 信号分形标度指数
- spread1 , spread2 , PPE - 基频变化的三种非线性测度