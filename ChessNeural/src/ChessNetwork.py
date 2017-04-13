import numpy as np
import matplotlib.pyplot as plt
import src.NeuralNetwork as NN


def load_fullAdder():
    x = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    y = np.array([[0, 0], [0, 1], [0, 1], [1, 0], [0, 1], [1, 0], [1, 0], [1, 1]])

    out = []

    # populate the tuple list with the data
    for i in range(x.shape[0]):
        result = list((x[i, :].tolist(), y[i].tolist()))
        out.append(result)

    return out


def load_xor():
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    out = []

    # populate the tuple list with the data
    for i in range(x.shape[0]):
        result = list((x[i].tolist(), y[i].tolist()))
        out.append(result)

    return out


def load_chess(filename):

    out = []
    with open(filename, 'r') as f:
        for line in f:
            chessTotal = []
            chessLineInput = []
            chessLineOutput = []
            chess = (line.rstrip().split(":"))
            chessInput = chess[0].split(",")
            chessOutput = chess[1].split(",")
            for i in chessInput:
                chessLineInput.append(int(i)/6)
            for o in chessOutput:
                chessLineOutput.append(int(o))
            chessTotal.append(chessLineInput)
            chessTotal.append(chessLineOutput)
            out.append(chessTotal)

    return out


def demo():

    chess = load_xor()

    # load the neural network, (input, [hidden], output)
    # the hidden layers has to be an array of at least 2 layers.
    Neuro = NN.MLP_NeuralNetwork(2, ([3, 3]), 1)
    Neuro.train(chess)
    # x = [4, 3, 2, 5, 6, 2, 3, 4,
    #      1, 1, 1, 1, 1, 1, 1, 1,
    #      0, 0, 0, 0, 0, 0, 0, 0,
    #      0, 0, 0, 0, 0, 0, 0, 0,
    #      0, 0, 0, 0, 1, 0, 0, 0,
    #      0, 0, 0, 0, 0, 0, 0, 0,
    #      1, 1, 1, 1, 0, 1, 1, 1,
    #      4, 3, 2, 5, 6, 2, 3, 4]
    # print(Neuro.giveInput(x))
    # predict = Neuro.predict(X)

    x = np.linspace(0, 1, 200)
    y = np.linspace(0, 1, 200)

    intensity = []
    for i in x:
        temp = []
        for j in y:
            temp.append(Neuro.giveInput([i, j]))
        intensity.append(temp)


    #setup the 2D grid with Numpy
    x, y = np.meshgrid(x, y)


    # now just plug the data into pcolormesh, it's that easy!
    plt.pcolormesh(x, y, intensity)
    plt.colorbar()  # need a colorbar to show the intensity scale
    plt.show()  # boom


if __name__ == '__main__':
    demo()