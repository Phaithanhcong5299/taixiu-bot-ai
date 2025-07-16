import numpy as np
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense
import os

label_map = {"Tài": 1, "Xỉu": 0}
reverse_map = {1: "Tài", 0: "Xỉu"}
MODEL_PATH = "lstm_model.h5"

def encode_sequence(seq):
    return np.array([[label_map[x]] for x in seq if x in label_map])

def predict_with_lstm(history):
    if not os.path.exists(MODEL_PATH) or len(history) < 30:
        return "Tài"
    model = load_model(MODEL_PATH)
    input_seq = encode_sequence(history[-30:]).reshape(1, 30, 1)
    pred = model.predict(input_seq)[0][0]
    return "Tài" if pred >= 0.5 else "Xỉu"

def update_lstm_model(history):
    if len(history) < 100:
        return
    X, y = [], []
    for i in range(len(history) - 31):
        seq = encode_sequence(history[i:i+30])
        label = label_map.get(history[i+30])
        if len(seq) == 30 and label is not None:
            X.append(seq)
            y.append(label)
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], 30, 1))
    model = Sequential()
    model.add(LSTM(32, input_shape=(30, 1)))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y, epochs=10, verbose=0)
    model.save(MODEL_PATH)
