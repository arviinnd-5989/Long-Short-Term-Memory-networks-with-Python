from keras.preprocessing.sequence import pad_sequences
sequences = [
    [1,2,3,4],
    [1,2,3],
    [1]
]

padded = pad_sequences(sequences, maxlen=2, truncating="post")
print(padded)