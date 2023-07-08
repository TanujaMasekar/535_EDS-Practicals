from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
tips_data=pd.read_csv("C:\\Users\\Admin\\Downloads\\tips.csv")
tips = sns.load_dataset("tips")
sns.catplot(data=tips, x="tip", y="sex", kind="bar")
tips = sns.load_dataset("tips")
sns.catplot(data=tips, x="day", y="total_bill")
sns.catplot(data=tips.query("size != 3"), x="size", y="total_bill")
plt
sns.catplot(data=tips, x="smoker", y="tip", order=["No","Yes"],kind='bar')
import pandas as pd
sns.catplot(data=tips, x="day", y="total_bill", kind="bar")
plt.title('Tips')
sns.catplot(
 data=tips, x="day", y="total_bill", hue="sex",kind="violin", split=True,)
sns.catplot(data=tips, x="smoker", kind="count", palette="ch:.25")
sns.catplot(
 data=tips, x="day", y="total_bill", hue="smoker",kind="swarm", col="time", aspect=.7,)
sns.catplot(data=tips, x="day", y="total_bill", kind="box")
sns.catplot(
 data=tips, x="total_bill", y="day", hue="sex",palette={"Male": "g", "Female": "m"},markers=["^", "o"], linestyles=["-", "--"],kind="point")