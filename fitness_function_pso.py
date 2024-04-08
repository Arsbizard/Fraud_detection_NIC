def fitness_function(parameters):
    parameters = np.round(parameters).astype(int)
    max_depth = int(np.mean(parameters[0]))
    min_samples_split = int(np.mean(parameters[1]))
    min_samples_leaf = int(np.mean(parameters[2]))
    model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return -accuracy
