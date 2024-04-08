def preprocessing_data(data):
    is_fraud = data['isFraud']
    data = data.drop(columns=['isFraud'], axis = 1)

    # Preprocessing for numerical attributes
    numerical_data = data.select_dtypes(include=['float64', 'int64'])

    # Drop attributes with more than 20% missing values
    numerical_data = numerical_data.dropna(thresh=len(numerical_data)*0.8, axis=1)

    # Fill missing values with mean
    imputer = SimpleImputer(strategy='mean')
    numerical_data = pd.DataFrame(imputer.fit_transform(numerical_data), columns=numerical_data.columns)

    # Normalize numerical values
    scaler = StandardScaler()
    numerical_data = pd.DataFrame(scaler.fit_transform(numerical_data), columns=numerical_data.columns)

    # Preprocessing for categorical attributes
    categorical_data = data.select_dtypes(include=['object'])

    # Drop attributes with more than 50% missing values
    categorical_data = categorical_data.dropna(thresh=len(categorical_data)*0.5, axis=1)

    # Transformation of emails (if needed)

    # Fill missing values with most frequent value
    imputer = SimpleImputer(strategy='most_frequent')
    categorical_data = pd.DataFrame(imputer.fit_transform(categorical_data), columns=categorical_data.columns)

    # Merge small categories into 'Other' category (if needed)

    # One-hot encoding
    encoder = OneHotEncoder()
    categorical_data_encoded = encoder.fit_transform(categorical_data).toarray()

    # Combine processed numerical and categorical data
    processed_data = pd.concat([pd.DataFrame(numerical_data), pd.DataFrame(categorical_data_encoded)], axis=1)

    processed_data = pd.concat([pd.DataFrame(processed_data), pd.DataFrame(is_fraud)], axis=1)
    
    smote = SMOTE(random_state=42)
    processed_data.columns = processed_data.columns.astype(str)
    X_oversampled, y_oversampled = smote.fit_resample(processed_data.drop('isFraud', axis=1), processed_data['isFraud'])
    
    return X_oversampled, y_oversampled
