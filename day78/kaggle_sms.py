import tensorflow as tf

path = "/content/drive/MyDrive/SPAM/spam.csv"

import pandas as pd

sms_data = pd.read_csv(path,encoding="latin1")

sms_data = sms_data.drop(["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1)
sms_data

from sklearn.model_selection import train_test_split
X = sms_data["v2"]
y = sms_data["v1"]
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2)


from tensorflow.keras.layers import Dense,Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences 
from sklearn.preprocessing import LabelEncoder

tokenizer = Tokenizer(num_words=1000,oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

seq = tokenizer.texts_to_sequences(X_train)
seq_2 = tokenizer.texts_to_sequences(X_test)

le = LabelEncoder()
y_train= le.fit_transform(y_train)
y_test =le.transform(y_test)


padded_x_train = pad_sequences(seq,maxlen=100,padding="post")
padded_x_test = pad_sequences(seq_2,maxlen=100,padding="post")


model = tf.keras.Sequential([
    Embedding(output_dim=16,input_dim=1000),
    GlobalAveragePooling1D(),
    Dense(24,activation="relu"),
    Dense(1,activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy",metrics=["accuracy"])

history = model.fit(padded_x_train,y_train,validation_data=(padded_x_test,y_test),epochs=10)

my_sms = "URGENT! Your mobile number has won a £2000 prize draw. Call 09061701461 to claim now!"

my_sms_seq = tokenizer.texts_to_sequences([my_sms])
padded_seq = pad_sequences(my_sms_seq,padding="post",maxlen=100)

score = model.predict(padded_seq)
if score>=0.5:
   print("spam")
else:
  print("ham")


#1-spam and 0-ham
