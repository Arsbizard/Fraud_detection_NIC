def pso(num_particles, dimensions, bounds, max_iter, c1, c2, w):
    particles = [Particle(dimensions, bounds) for _ in range(num_particles)]
    global_best_position = None
    global_best_score = float('inf')

    for _ in range(max_iter):
        for particle in particles:
            score = fitness_function(particle.position)
            if score < particle.best_score:
                particle.best_position = particle.position
                particle.best_score = score

            if score < global_best_score:
                global_best_position = particle.position
                global_best_score = score

        for particle in particles:
            r1, r2 = np.random.rand(), np.random.rand()
            particle.velocity = w * particle.velocity + c1 * r1 * (particle.best_position - particle.position) + \
                                c2 * r2 * (global_best_position - particle.position)
            particle.position += particle.velocity
            particle.position = np.clip(particle.position, bounds[0], bounds[1])

    return global_best_score, global_best_position
