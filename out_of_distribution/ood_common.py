import cv2
import numpy as np
from tensorflow.keras import datasets, utils, Input, Sequential
from tensorflow.keras.layers import (Flatten,
                                     Dense,
                                     Dropout,
                                     Conv2D,
                                     MaxPooling2D)

BASE_SHAPE = (28, 28, 1)


def get_mnist_data(fashion=False):

    source = datasets.fashion_mnist if fashion else datasets.mnist

    (x_train, y_train), (x_test, y_test) = source.load_data()

    x_train = x_train.astype('float32') / 255
    x_test = x_test.astype('float32') / 255

    y_train = utils.to_categorical(y_train)
    y_test = utils.to_categorical(y_test)

    return (
        np.expand_dims(x_train, -1),
        np.expand_dims(x_test, -1),
        y_train,
        y_test
    )


def get_ood_data_random_uniform(shape=BASE_SHAPE, n=10000):
    return np.random.rand(*((n,) + shape)).astype('float32')


def get_ood_data_cifar10(shape=BASE_SHAPE):
    (_, _), (x_test, _) = datasets.cifar10.load_data()

    def convert(img):
        return cv2.cvtColor(cv2.resize(img, shape[:2]), cv2.COLOR_BGR2GRAY)

    imgs = np.array([convert(img) for img in x_test]).astype('float32') / 255
    return np.expand_dims(imgs, -1)


def conv_classifier(n_classes=10, input_shape=BASE_SHAPE):

    layers = [
        Input(shape=input_shape),
        Conv2D(32, kernel_size=(3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, kernel_size=(3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dropout(0.5),
        Dense(n_classes, activation='softmax'),
    ]

    model = Sequential(layers)

    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])

    return model


def logistic_regression(n_classes, input_shape):

    layers = [
        Input(shape=input_shape),
        Dense(n_classes, activation='softmax'),
    ]

    model = Sequential(layers)

    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])

    return model
