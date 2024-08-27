import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import panel as pn

pn.extension()

# Loading data
dfrm = pd.read_csv('projects_data.csv')

# Selecting columns only with numerical values
dfnm = dfrm.select_dtypes(include='number')

#visualization functions

def plot_frequency_distribution():
    print(dfrm['Project Type'].value_counts())
    print("\n", dfrm['Neighborhood'].value_counts())
    print("\n", dfrm['Design Complexity Level'].value_counts())
    print("\n", dfrm['Design Software Used'].value_counts())

    sns.set(font_scale=0.6)
    sns.histplot(dfnm, bins=10, element="step")
    plt.show()

    sns.histplot(dfrm['Neighborhood'])
    plt.xlabel("Neighbourhood", fontsize=15)
    plt.ylabel("Count", fontsize=15)
    plt.show()

    sns.displot(dfrm['Design Software Used'])
    plt.xlabel("Design Software Used", fontsize=15)
    plt.ylabel("Count", fontsize=15)
    plt.show()

    pd.crosstab(dfrm['Neighborhood'], dfrm['Project Type']).plot(kind='bar', stacked=True)
    plt.title("Project Type in Neighbourhoods")
    plt.show()

def plot_univariate():
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

def plot_bivariate():
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

def plot_trivariate():
    pivot_table = dfrm.pivot_table(values='Client Feedback Score', index='Neighborhood', columns='Project Type', aggfunc='mean')
    sns.heatmap(pivot_table, annot=True, cmap='coolwarm')
    plt.show()

    sns.barplot(x='Project Type', y='Cost Efficiency (%)', hue='Design Software Used', data=dfrm)
    plt.show()

#plotting
plot_options = {
    "Frequency Distribution": plot_frequency_distribution,
    "Univariate Analysis": plot_univariate,
    "Bivariate Analysis": plot_bivariate,
    "Trivariate Analysis": plot_trivariate
}

dropdown = pn.widgets.Select(name='Select Plot', options=list(plot_options.keys()))
figure_dropdown = pn.widgets.Select(name='Select Figure', options=[])

@pn.depends(dropdown.param.value)
def update_plot(selected_plot):
    plt.close('all')
    plot_function = plot_options[selected_plot]  
    plot_function() 
    return plt.gcf()

panel = pn.Column(dropdown, update_plot)
panel.show()  