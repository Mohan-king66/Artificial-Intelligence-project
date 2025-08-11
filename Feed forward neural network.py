import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([
    [0],
    [1],
    [1],
    [0]
])
np.random.seed(1)
input_layer_neurons = X.shape[1]
hidden_layer_neurons = 2
output_neurons = 1
weights_input_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bias_output = np.random.uniform(size=(1, output_neurons))
hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
hidden_output = sigmoid(hidden_input)
final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
final_output = sigmoid(final_input)
print("Input:\n", X)
print("\nOutput of Neural Network after Feedforward:\n", final_output)
