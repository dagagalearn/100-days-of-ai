import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
 
sentences = ["Hello my name is Dagaga",
             "I am on day seventy five",
             "Goodbye"]

tokenizer = Tokenizer(num_words=100,oov_token="<OOV>")

tokenizer.fit_on_texts(sentences)

sequence = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequence,padding="post",maxlen=9,truncating="pre")

word_index = tokenizer.word_index 

print("Word Indices: ")
print(word_index)

print("Padded list: ")
print(padded)

print("Sequences")
print(sequence)
