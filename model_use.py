def use_model():
    final_model = DecisionTreeClassifier(max_depth=best_max_depth, min_samples_split=best_min_samples_split,
                                                                         min_samples_leaf=best_min_samples_leaf)
    final_model.fit(X_train, y_train)
    final_predictions = final_model.predict(X_test)
    final_accuracy = accuracy_score(y_test, final_predictions)
    print("Final Accuracy:", final_accuracy)
