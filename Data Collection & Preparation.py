import numpy as np
import pandas as pd
import os

#loading dataset

#first excel file
prodata=pd.read_excel('/Users/sumitverma/H3RTZ/Python_nd_Stuff/College Project/Exc_data.xlsx')
df = pd.DataFrame(prodata)

#second excel file
prodata2=pd.read_excel('/Users/sumitverma/H3RTZ/Python_nd_Stuff/College Project/Exc_data2.xlsx')
df2 = pd.DataFrame(prodata2)

#merging excel files and converting into dataframe
muldf=[df,df2]
finaldf = pd.concat(muldf)
dfrm=pd.DataFrame(finaldf)


#overview of data
print("Overview of data \n", dfrm.head())
print("\n Information of the Dataframe \n" ,dfrm.info())
print("\n Description of the DataFrame \n" ,dfrm.describe())


#data cleaning

#calculating null values
print("\n Null Values in DataFrame\n" ,dfrm.isnull().sum())                                                     

#filling null values with average of the columns
dfrm['Design Phase Duration (weeks)'] = dfrm['Design Phase Duration (weeks)'].fillna(dfrm['Design Phase Duration (weeks)'].mean())
dfrm['Total Project Duration (weeks)'] = dfrm['Total Project Duration (weeks)'].fillna(dfrm['Total Project Duration (weeks)'].mean())
dfrm['Design Revision Count'] = dfrm['Design Revision Count'].fillna(dfrm['Design Revision Count'].mean())
dfrm['Cost Efficiency (%)'] = dfrm['Cost Efficiency (%)'].fillna(dfrm['Cost Efficiency (%)'].mean())
dfrm['Innovation Score'] = dfrm['Innovation Score'].fillna(dfrm['Innovation Score'].mean())
dfrm['Use of Sustainable Materials (%)'] = dfrm['Use of Sustainable Materials (%)'].fillna(dfrm['Use of Sustainable Materials (%)'].mean())
dfrm['Client Feedback Score'] = dfrm['Client Feedback Score'].fillna(dfrm['Client Feedback Score'].mean())
dfrm['Team Size'] = dfrm['Team Size'].fillna(dfrm['Team Size'].mean())
dfrm['Use of Local Materials (%)'] = dfrm['Use of Local Materials (%)'].fillna(dfrm['Use of Local Materials (%)'].mean())

#rounding off columns
dfrm['Design Phase Duration (weeks)'] = dfrm['Design Phase Duration (weeks)'].round(2)
dfrm['Total Project Duration (weeks)'] = dfrm['Total Project Duration (weeks)'].round(2)
dfrm['Design Revision Count'] = dfrm['Design Revision Count'].round(2)
dfrm['Cost Efficiency (%)'] = dfrm['Cost Efficiency (%)'].round(2)
dfrm['Innovation Score'] = dfrm['Innovation Score'].round(2)
dfrm['Use of Sustainable Materials (%)'] = dfrm['Use of Sustainable Materials (%)'].round(2)
dfrm['Client Feedback Score'] = dfrm['Client Feedback Score'].round(2)
dfrm['Team Size'] = dfrm['Team Size'].round(2)
dfrm['Use of Local Materials (%)'] = dfrm['Use of Local Materials (%)'].round(2)

#dropping duplicates
dfrm.drop_duplicates(inplace=True)                                                   


#feature Engineering

dfrm['Design-to-Total Duration Ratio'] = dfrm['Design Phase Duration (weeks)'] / dfrm['Total Project Duration (weeks)']
dfrm['Design-to-Total Duration Ratio'] = dfrm['Design-to-Total Duration Ratio'].round(2)

dfrm['Sustainability Index'] = (dfrm['Use of Sustainable Materials (%)'] + dfrm['Use of Local Materials (%)']) / 2

dfrm['Innovation per Revision'] = dfrm['Innovation Score'] / dfrm['Design Revision Count']
dfrm['Innovation per Revision'] = dfrm['Innovation per Revision'].round(2)


complexity_mapping = {'Very Low': 1,'Low': 2, 'Medium': 3, 'High': 4, 'Very High': 5,}
dfrm['Client Feedback Adjusted'] = dfrm['Client Feedback Score'] / dfrm['Design Complexity Level'].map(complexity_mapping)
dfrm['Client Feedback Adjusted'] = dfrm['Client Feedback Adjusted'].round(2)

dfrm['Complexity to Team Ratio'] = dfrm['Design Complexity Level'].map(complexity_mapping) / dfrm['Team Size']
dfrm['Complexity to Team Ratio'] = dfrm['Complexity to Team Ratio'].round(2)

dfrm['Complexity and Duration Interaction'] = dfrm['Design Complexity Level'].map(complexity_mapping) * dfrm['Total Project Duration (weeks)']
dfrm['Complexity and Duration Interaction'] = dfrm['Complexity and Duration Interaction'].round(2)

dfrm['Neighborhood Impact'] = dfrm.groupby('Neighborhood')['Client Feedback Score'].transform('mean')
dfrm['Neighborhood Impact'] = dfrm['Neighborhood Impact'].round(2)

#loading dataframe again
if os.path.exists('/Users/sumitverma/H3RTZ/Python_nd_Stuff/projects_data.csv'):
    dfrm = pd.read_csv('/Users/sumitverma/H3RTZ/Python_nd_Stuff/projects_data.csv')
    print("\nLoaded data from existing CSV file.\n")
else:
    dfrm = pd.DataFrame()
    print("\nNo existing data file found. Starting with an empty dataset.\n")



#CRUD operations
def addproj(data):
    global dfrm
    newdfrm = pd.DataFrame([data])
    dfrm = pd.concat([dfrm, newdfrm], ignore_index=True)
    print("\nNew project added successfully!\n")
    dfrm.to_csv('projects_data.csv', index=False)

def readproj(project_id):
    project = dfrm[dfrm['Project ID'] == project_id]
    if not project.empty:
        print("\nProject Details:\n", project)
    else:
        print("\nProject not found!")

def updateproj(project_id, updates):
    global dfrm
    for key, value in updates.items():
        dfrm.loc[dfrm['Project ID'] == project_id, key] = value
    print("\nProject updated successfully!\n")

def deleteproj(project_id):
    global dfrm
    dfrm = dfrm[dfrm['Project ID'] != project_id]
    print("\nProject deleted successfully!\n")

crudops = input("CRUD operations? (yes/no): ").strip().lower()

if crudops == 'yes':
    perfcreate = input("Do you want to perform 'Create' operation? (yes/no): ").strip().lower()
    perfread = input("Do you want to perform 'Read' operation? (yes/no): ").strip().lower()
    perfupdate = input("Do you want to perform 'Update' operation? (yes/no): ").strip().lower()
    perfdelete = input("Do you want to perform 'Delete' operation? (yes/no): ").strip().lower()

    if perfcreate == 'yes':
        print("Enter the following details for the new project:")
        new_project = {
            'Project ID': input("Project ID: "),
            'Project Name': input("Project Name: "),
            'Project Type': input("Project Type: "),
            'Design Phase Duration (weeks)': float(input("Design Phase Duration (weeks): ")),
            'Total Project Duration (weeks)': float(input("Total Project Duration (weeks): ")),
            'Design Revision Count': int(input("Design Revision Count: ")),
            'Cost Efficiency (%)': float(input("Cost Efficiency (%): ")),
            'Innovation Score': float(input("Innovation Score(1-5): ")),
            'Use of Sustainable Materials (%)': float(input("Use of Sustainable Materials (%): ")),
            'Client Feedback Score': float(input("Client Feedback Score(1-5): ")),
            'Design Complexity Level': input("Design Complexity Level(low,medium,high): "),
            'Team Size': int(input("Team Size: ")),
            'Design Software Used': input("Design Software Used: "),
            'Neighborhood': input("Neighborhood: "),
            'Use of Local Materials (%)': float(input("Use of Local Materials (%): "))
        }
        addproj(new_project)
        dfrm.to_csv('projects_data.csv', index=False)

    if perfread == 'yes':
        project_id = input("Project ID to read: ")
        readproj(project_id)

    if perfupdate == 'yes':
        project_id = input("Project ID to update: ")
        updates = {}
        updates['Total Project Duration (weeks)'] = float(input("New Total Project Duration (weeks): "))
        updates['Innovation Score'] = float(input("New Innovation Score: "))
        updateproj(project_id, updates)

    if perfdelete == 'yes':
        project_id = input("Project ID to delete: ")
        deleteproj(project_id)


#converting into a CSV file

dfrm.to_csv('projects_data.csv', index=False)
print("Data saved successfully!")
