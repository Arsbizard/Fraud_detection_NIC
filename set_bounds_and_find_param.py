def set_bounds_and_find_hyperparameters():
    max_depth_range = (3, 30)
    min_samples_split_range = (2, 20)
    min_samples_leaf_range = (1, 10)
    bounds = (np.array([max_depth_range[0], min_samples_split_range[0], min_samples_leaf_range[0]]),
              np.array([max_depth_range[1], min_samples_split_range[1], min_samples_leaf_range[1]]))
    
    best_cost, best_hyperparameters = pso(num_particles, dimensions, bounds, max_iter, c1, c2, w)
    print("Best Hyperparameters:", best_hyperparameters)
    
    if isinstance(best_hyperparameters, tuple) and len(best_hyperparameters) == 2:
        best_max_depth = max(1, int(np.mean(best_hyperparameters[0])))
        best_min_samples_split = int(np.mean(best_hyperparameters[1]))
        best_min_samples_leaf = 1
    elif isinstance(best_hyperparameters, np.ndarray):
        best_max_depth = max(1, int(np.mean(best_hyperparameters)))
        best_min_samples_split = 2
        best_min_samples_leaf = 1
    else:
        raise ValueError("Unexpected structure of best_hyperparameters")
    
