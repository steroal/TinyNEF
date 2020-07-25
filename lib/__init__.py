import numpy as np

class NefGym:

    def __init__(self, obs_size, neurons):

        # Encoder
        self.alpha = np.random.uniform(0, 100, neurons) # tuning parameter alpha
        self.b = np.random.uniform(-20,+20, neurons)    # tuning parameter b
        self.e = np.random.uniform(-1, +1, (obs_size,neurons)) # encoder weights

        self.neurons = neurons

    def new_params(self):

       return np.random.uniform(-1, +1, (self.neurons,1)) # decoder weights

    def eval_params(self, params, episodes=10):

        total_reward = 0
        total_steps = 0

        for _ in range(episodes):

            episode_reward, episode_steps = self.run_episode(params)

            total_reward += episode_reward
            total_steps += episode_steps

        return total_reward, total_steps

    def mutate_params(self, params, noise_std):

        d = params

        return d+noise_std*np.random.randn(*d.shape)

    def _curve(self, x):

        return NefGym._G(self.alpha * np.dot(x, self.e) + self.b)

    @staticmethod
    def _G(v):

        v[v<=0] = np.finfo(float).eps

        g = 10 * np.log(np.abs(v))

        g[g<0] = 0

        return  g

