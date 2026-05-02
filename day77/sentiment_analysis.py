from tensorflow.keras.datasets import imdb
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense,LSTM,Embedding, SpatialDropout1D

imdb = imdb.load_data(num_words=10000)
(X_train, y_train),(X_test,y_test) = imdb

X_train = pad_sequences(X_train,maxlen=100)
X_test = pad_sequences(X_test,maxlen=100)

model = tf.keras.models.Sequential([
    Embedding(10_000,128,input_length = 100),
    SpatialDropout1D(0.2),
    LSTM(128,dropout=0.2),
    Dense(1,activation="sigmoid")

])

model.compile(optimizer="adam",loss="binary_crossentropy",metrics = ["accuracy"])

model.summary()
history = model.fit(X_train, y_train, validation_data=(X_test,y_test),epochs=5)
print(history.history)

import string
def predict_review(review):
  word_index = tf.keras.datasets.imdb.get_word_index()
  sequence = []
  review = review.lower().split()
  for word in review:
    word = word.strip(string.punctuation)
    word_i = word_index.get(word,2)
    actual_ind = word_i+3
    if actual_ind<10_000:
      sequence.append(actual_ind)
    else:
      sequence.append(2)

  padded = pad_sequences([sequence],maxlen=100)
  score = model.predict(padded)[0][0]
  if score>0.5:
    return "Positive"
  elif score<0.5:
    return "Negative"
  else:
    return "Neutral"
  
my_review = """APEX is a solid, entertaining thriller that's worth checking out. At just over 90 minutes, 

it's a fast-paced movie that kept me glued to the screen with 

unexpected moments and nerve-racking scenes. 

The scenery is beautiful, and the cast is solid, delivering exactly what they set out to do—entertain"""

    

print(predict_review(my_review)) # Positive 
