########################################################################
# Assignment No 40 - Question 8
# Decision Tree Visualization using plot_tree, find which feture
# appears at the root node and why it was selected first
########################################################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

Border = "-"*30

#########################################################
# Step 1 : Load The Dataset
#########################################################

print(Border)
print("Step 1 : Load The Dataset")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset Loded Succsesfully")
print(df.head())

#########################################################
# Step 2 : Deside Independant And Dependant Veriables
#########################################################

print(Border)
print("Step 2 : Deside Independant And Dependant Veriables")
print(Border)

feture_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feture_cols]
Y = df["FinalResult"]

#########################################################
# Step 3 : Split, Build And Train The Module
#########################################################

print(Border)
print("Step 3 : Split, Build And Train The Module")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

print("Module Trainned Succesfully")

#########################################################
# Step 4 : Visualize The Decision Tree
#########################################################

print(Border)
print("Step 4 : Visualize The Decision Tree")
print(Border)

plt.figure(figsize=(16,9))

plot_tree(model,
          feature_names=feture_cols,
          class_names=["Fail","Pass"],
          filled=True,
          rounded=True)

plt.title("Marvellous Student Performence - Decision Tree")
plt.show()

#########################################################
# Step 5 : Find Feture At Root Node
#########################################################

print(Border)
print("Step 5 : Find Feture At Root Node")
print(Border)

# tree_.feature[0] gives the index of the feture used to split the root node
root_feture_index = model.tree_.feature[0]
root_feture_name = feture_cols[root_feture_index]

print("Feture Which Appears At Root Node Is :",root_feture_name)

print()
print("This Feture Is Selected First Becouse The Decision Tree Algorithm")
print("Always Picks The Feture Which Gives The Highest Information Gain,")
print("Ie, The Feture Which Reduces The Gini Impurity / Entropy The Most")
print("So", root_feture_name, "Seperates The Pass And Fail Students Best")
print("Compared To All Other Feturers Present In The Dataset")
