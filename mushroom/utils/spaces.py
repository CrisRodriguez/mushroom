import numpy as np


class Box:
    """
    This class implements functions to manage continuous states and action
    spaces. It is similar to the Box class in gym.spaces.box.

    """
    def __init__(self, low, high, shape=None):
        """
        Constructor.

        Args:
            low ([float, np.ndarray]): the minimum value of dimensions of the
                space. If a scalar value is provided, this value is considered
                as the minimum one for each dimension. If a np.ndarray is
                provided, each i-th element is considered the minimum value
                of the i-th dimension;
            high ([float, np.ndarray]): the maximum value of dimensions of the
                space. If a scalar value is provided, this value is considered
                as the maximum one for each dimension. If a np.ndarray is
                provided, each i-th element is considered the maximum value
                of the i-th dimension;
            shape (np.ndarray, None): the dimension of the space. Must match
                the shape of `low` and `high`, if they are np.ndarray.

        """
        if shape is None:
            self._low = low
            self._high = high
            self._shape = low.shape
        else:
            self._low = low
            self._high = high
            self._shape = shape
            if np.isscalar(low) and np.isscalar(high):
                self._low += np.zeros(shape)
                self._high += np.zeros(shape)

        assert self._low.shape == self._high.shape

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high

    @property
    def shape(self):
        return self._shape


class Discrete:
    """
    This class implements functions to manage discrete states and action
    spaces. It is similar to the Discrete class in gym.spaces.discrete.

    """
    def __init__(self, n):
        """
        Constructor.

        Args:
            n (int): the number of discrete values of the space.

        """
        self.values = np.arange(n)
        self.n = n

    @property
    def size(self):
        return self.n,

    @property
    def shape(self):
        return 1,
