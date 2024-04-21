def load_data(train_identity, train_transaction):
  df_identities = pd.read_csv(train_identity)
  df_transaction = pd.read_csv(train_transaction.csv)
  data = pd.merge(df_transaction, df_identities, on='TransactionID', how='left')
  return data
