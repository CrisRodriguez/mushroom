from keras.models import Sequential
from keras.layers.core import Dense


class DenseNN(object):
    def __init__(self, **approximator_params):
        self.approximator_params = approximator_params

    def fit(self, x, y, **fit_params):
        if not hasattr(self, 'model'):
            self.model = self._init()

        self.model.fit(x, y, **fit_params)

    def predict(self, x):
        predictions = self.model.predict(x)

        return predictions.ravel()

    def _init(self):
        pars = self.approximator_params
        n_input = pars.pop('n_input')
        hidden_neurons = pars.pop('hidden_neurons')
        n_output = pars.pop('n_output')
        loss = pars.pop('loss')
        optimizer = pars.pop('optimizer')

        model = Sequential()
        model.add(Dense(hidden_neurons[0], input_shape=(n_input,), **pars))
        for i in range(1, len(hidden_neurons)):
            model.add(Dense(hidden_neurons[i], **pars))
        model.add(Dense(n_output, activation='linear', **pars))

        model.compile(loss=loss, optimizer=optimizer, **pars)

        return model