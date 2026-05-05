# Importing what we will need
import tensorflow as tf
import kagglehub
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense,Embedding,Flatten
from tensorflow.keras.models import Sequential
import numpy as np
import joblib 

#data preperation
path = kagglehub.dataset_download("praveengovi/emotions-dataset-for-nlp")
data = pd.read_csv(path+"/train.txt", sep=';', header=None, names=['text', 'emotion'])
X = data["text"]
y = data["emotion"]
y = pd.get_dummies(y).astype(int) # Convert boolean dummies to integers
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2)

# data preprocessing
tokenizer = Tokenizer(num_words=5000,oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)
seq = tokenizer.texts_to_sequences(X_train)
seq_2 = tokenizer.texts_to_sequences(X_test)
padded = pad_sequences(seq,maxlen=25,padding="pre",truncating="pre")
padded_2 = pad_sequences(seq_2,maxlen=25,padding="pre",truncating="pre")

# making our model and training
model = Sequential([
    Embedding(5001,128),
    tf.keras.layers.LSTM(128),
    Dense(128,activation="relu"),
    tf.keras.layers.Dropout(0.2),
    Dense(64,activation="relu"),
    tf.keras.layers.Dropout(0.2),
    Dense(6,activation="softmax")]
)
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(padded,y_train,validation_data=(padded_2,y_test),epochs=14)

# taking input and processing it
new_txt = input("Say something.....: ")
new_seq = tokenizer.texts_to_sequences([new_txt])
new_padded = pad_sequences(new_seq,maxlen=25,padding="pre",truncating="pre")

# prediction and output phase
prediction = model.predict(new_padded)
emotion_index = np.argmax(prediction)
emotion_labels = y_train.columns
print(f"Your predicted feeling: {emotion_labels[emotion_index]}, with confidence of: {np.max(prediction)*100:.2f}%")

# saving the model and tokeinizer for persistence
model.save('emotion_classifier_model.keras')
with open("tokenizer.joblib","wb") as f:
  joblib.dump(tokenizer,f)
