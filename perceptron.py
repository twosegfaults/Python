import numpy
class Perceptron:
    def start(self, size):
        self.weight = numpy.random(size + 1)
        self.bias = 0
    
    def predict(self, x):
        z = self.weight.T.dot(x) + self.bias
        return 1 if z >= 0 else 0
    
    def train(self, X, d, epochs=1, lr=0.01):
        for _ in epochs:
            for i in range(d.shape[0]):
                y = self.predict(X[i])
                error = d[i] - y
                self.weight = self.weight - lr * error * X[i]
                self.bias = self.bias-lr*error