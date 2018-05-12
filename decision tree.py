from sklearn from tree

model=tree.DecisionTreeClassifier(creterion='gini')
model.fit(X,Y)
model.score(X,Y)
predicted=model.predict(x_test)