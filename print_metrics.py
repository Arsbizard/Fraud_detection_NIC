# Caclulate and print classification metrics: accuracy, precision, recall, and F1 score 
def print_clf_metrics(y_actual, y_pred ):
    # Calculate accuracy
    accuracy = sklearn.metrics.accuracy_score(y_actual, y_pred)

    # Calculate precision
    precision = sklearn.metrics.precision_score(y_actual, y_pred)

    # Calculate recall
    recall = sklearn.metrics.recall_score(y_actual, y_pred)

    # Calculate F1 score
    f1 = sklearn.metrics.f1_score(y_actual, y_pred)

    # Print metrics
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)
