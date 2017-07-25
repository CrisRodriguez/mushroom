import gym
from PIL import Image

from PyPi.environments import Environment
from PyPi.utils.spaces import *


class Atari(Environment):
    def __init__(self, name, train=False):
        self.__name__ = name

        # MPD creation
        self.env = gym.make(self.__name__)

        # MDP spaces
        self.img_size = (84, 110)
        self.action_space = Discrete(self.env.action_space.n)
        self.observation_space = Box(low=0, high=255, shape=(self.img_size[1],
                                                             self.img_size[0],
                                                             3))

        # MDP parameters
        self.horizon = 100
        self.gamma = 0.99

        # MDP properties
        self._train = train
        self._lives = self.env.env.ale.lives()

        super(Atari, self).__init__()

    def reset(self, state=None):
        state = self._preprocess_observation(self.env.reset())
        self._state = np.array([state, state, state, state])

        if self._lives == 0:
            self._lives = self.env.env.ale.lives()

        return self._state

    def step(self, action):
        obs, reward, absorbing, info = self.env.step(action)

        if self._train:
            reward = np.clip(reward, -1, 1)

            if hasattr(info, 'ale.lives'):
                if info['ale.lives'] != self._lives:
                    absorbing = True
                self._lives = info['ale.lives']

        obs = self._preprocess_observation(self.get_state())
        self._state = self._get_next_state(self._state, obs)

        return self._state, reward, absorbing, info

    def render(self, mode='human', close=False):
        self.env.render(mode=mode, close=close)

    def _get_next_state(self, current, obs):
        return np.append(current[1:], [obs], axis=0)

    def _preprocess_observation(self, obs):
        image = Image.fromarray(obs, 'RGB').convert('L').resize(self.img_size)

        return np.asarray(image.getdata(), dtype=np.uint8).reshape(
            image.size[1], image.size[0])  # Convert to array and return