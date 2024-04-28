class AntColonyFeatureSelection:
    def __init__(self, X_train, X_test, y_train, y_test, n_ants, decay, alpha=1, beta=10):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.n_ants = n_ants
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.n_features = X_train.shape[1]
        self.pheromones = np.ones((self.n_features, self.n_features)) / self.n_features

    def run(self):
        best_features = []
        best_f1_score = 0
        for _ in range(self.n_ants):
            selected_features, f1_score = self._construct_solutions()
            if f1_score > best_f1_score:
                best_f1_score = f1_score
                best_features = selected_features

            self.pheromones *= self.decay
            
        return best_features, best_f1_score

    def _construct_solutions(self):
        features = []
        current_node = np.random.randint(self.n_features)  
        f1_early = 0
        while True:
            features.append(current_node)
            f1 = self._evaluate_features(features)
            print(f1)
            self._update_pheromone(f1, f1_early, current_node, features)
            if f1 >= 0.6358123994555129:
                print(features)
                break
            current_node = self._select_next(features)
            
            f1_early = f1

        return features, self._evaluate_features(features)
    
    def _update_pheromone(self, f1, f1_early, current_node, features):
        if f1_early >= f1:
            print(current_node)
            for t in features:
                self.pheromones[t][current_node] /= self.beta
        else:
            for t in features:
                self.pheromones[t][current_node] *= self.beta
            

    def _select_next(self, features):
        choices = list(set(range(self.n_features)) - set(features))
        pheromone_values = self.pheromones[features[-1], choices]
        probabilities = pheromone_values ** self.alpha
        probabilities /= np.sum(probabilities)
        return np.random.choice(choices, p=probabilities)

    def _evaluate_features(self, features):
        features = list(set(range(self.n_features)) - set(features))
        selected_features = self.X_train.iloc[:, features].values
        rf = RandomForestClassifier()
        rf.fit(selected_features, self.y_train)
        X_test_selected = self.X_test.iloc[:, features].values
        y_pred = rf.predict(X_test_selected)
        return f1_score(self.y_test, y_pred)

