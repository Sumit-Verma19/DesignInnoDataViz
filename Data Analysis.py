import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading data
dfrm = pd.read_csv('projects_data.csv')

#selecting columns only with numerical values
dfnm = dfrm.select_dtypes(include='number')

#EDA

#frequency distribution
print(dfrm['Project Type'].value_counts())
print("\n",dfrm['Neighborhood'].value_counts())
print("\n",dfrm['Design Complexity Level'].value_counts())
print("\n",dfrm['Design Software Used'].value_counts())

sns.set(font_scale=0.6)

sns.histplot(dfnm, bins=10, element="step")
sns.boxplot(x=dfnm['Design Phase Duration (weeks)'])
plt.show()

nbrhd = sns.histplot(dfrm['Neighborhood'])
plt.xlabel("Neighbourhood", fontsize=15)
plt.ylabel("Count", fontsize=15)
plt.show()

dsu = sns.displot(dfrm['Design Software Used'])
plt.xlabel("Design Software Used", fontsize=15)
plt.ylabel("Count", fontsize=15)
plt.show()

pd.crosstab(dfrm['Neighborhood'], dfrm['Project Type']).plot(kind='bar', stacked=True)
plt.title("Project Type in Neighbourhoods")
plt.show()


#Data Visualization

#univariate
sns.lineplot(data=dfrm , y='Design Phase Duration (weeks)', x='Project Type')
plt.show()

sns.lineplot(data=dfrm , y='Total Project Duration (weeks)', x='Project Type')
plt.show()

sns.histplot(data=dfrm , x='Design Complexity Level', y='Project Type')
plt.show()

sns.lineplot(dfnm['Design-to-Total Duration Ratio'])
plt.show()

sns.catplot(dfnm['Sustainability Index'], kind="point")
plt.show()

sns.stripplot(dfnm['Innovation per Revision'])
plt.show()

sns.kdeplot(dfnm['Client Feedback Adjusted'])
plt.show()

sns.scatterplot(dfnm['Complexity and Duration Interaction'])
plt.show()

#bivariate
sns.scatterplot(x='Cost Efficiency (%)', y='Client Feedback Score', data=dfrm)
plt.show()

sns.pairplot(dfrm[['Cost Efficiency (%)', 'Innovation Score', 'Client Feedback Score']])
plt.show()

sns.boxplot(x='Project Type', y='Innovation Score', data=dfrm)
plt.show()

sns.violinplot(x='Project Type', y='Cost Efficiency (%)', data=dfrm)
plt.show()

sns.swarmplot(x='Design Complexity Level', y='Innovation Score', data=dfrm)
plt.show()

sns.jointplot(x='Design Phase Duration (weeks)', y='Total Project Duration (weeks)', data=dfrm, kind='reg')
plt.show()

sns.jointplot(x='Cost Efficiency (%)', y='Client Feedback Score', data=dfrm, kind='scatter', marginal_kws=dict(bins=15, fill=True))
plt.show()

plt.scatter(dfrm['Cost Efficiency (%)'], dfrm['Innovation Score'], s=dfrm['Team Size']*10, alpha=0.5)
plt.xlabel('Cost Efficiency (%)')
plt.ylabel('Innovation Score')
plt.title('Bubble Plot of Cost Efficiency vs Innovation Score (Bubble Size: Team Size)')
plt.show()


#trivariate
pivot_table = dfrm.pivot_table(values='Client Feedback Score', index='Neighborhood', columns='Project Type', aggfunc='mean')
sns.heatmap(pivot_table, annot=True, cmap='coolwarm')

sns.barplot(x='Project Type', y='Cost Efficiency (%)', hue='Design Software Used', data=dfrm)
plt.show()
