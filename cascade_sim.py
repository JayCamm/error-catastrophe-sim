def simulate_cascade_with_stats(N, chi_range, alpha=0.35, correction_ratio=0.1, n_sims=500):
    capacity = int(N * correction_ratio)
    means = []
    stds = []
    
    for chi in chi_range:
        results = []
        
        for _ in range(n_sims):
            p_base = 0.5 * erfc(chi / np.sqrt(2))
            states = np.random.rand(N) < p_base
            
            for _ in range(3):
                influence = np.roll(states, 1) + np.roll(states, -1)
                p_eff = 0.5 * erfc((chi - alpha * influence) / np.sqrt(2))
                states = np.logical_or(states, np.random.rand(N) < p_eff)
                
            results.append(np.sum(states) > capacity)
        
        results = np.array(results)
        means.append(results.mean())
        stds.append(results.std() / np.sqrt(n_sims))  # standard error
        
    return np.array(means), np.array(stds)