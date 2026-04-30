import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,Flatten,Dense
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences



sentences = [
    "I cheated while playing the darts tournament by using a longbow.",
    "He drank life before spitting it out.",
    "Erin accidentally created a new universe.",
    "His get rich quick scheme was to grow a cactus farm.",
    "The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.",
    "It's not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.",
    "They called out her name time and again, but were met with nothing but silence.",
    "Love is not like pizza.",
    "Poison ivy grew through the fence they said was impenetrable.",
    "I really want to go to work, but I am too sick to drive.",
    "I've traveled all around Africa and still haven't found the gnu who stole my scarf.",
    "Andy loved to sleep on a bed of nails.",
    "He is no James Bond; his name is Roger Moore.",
    "Nothing is as cautiously cuddly as a pet porcupine.",
    "He was sitting in a trash can with high street class.",
    "Jason didn’t understand why his parents wouldn’t let him sell his little sister at the garage sale.",
    "He was sure the Devil created red sparkly glitter.",
    "The urgent care center was flooded with patients after the news of a new deadly virus was made public.",
    "Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.",
    "Today I bought a raincoat and wore it on a sunny day.",
    "There was coal in his stocking and he was thrilled.",
    "When he asked her favorite number, she answered without hesitation that it was diamonds.",
    "The lake is a long way from here.",
    "I've always wanted to go to Tajikistan, but my cat would miss me.",
    "Flash photography is best used in full sunlight.",
    "It was obvious she was hot, sweaty, and tired.",
    "I caught my squirrel rustling through my gym bag.",
    "He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.",
    "He dreamed of eating green apples with worms.",
    "She always had an interesting perspective on why the world must be flat.",
    "Garlic ice-cream was her favorite.",
    "Honestly, I didn't care much for the first season, so I didn't bother with the second.",
    "I thought red would have felt warmer in summer but I didn't think about the equator.",
    "The sight of his goatee made me want to run and hide under my sister-in-law's bed.",
    "Stop waiting for exceptional things to just happen.",
    "Patricia found the meaning of life in a bowl of Cheerios.",
    "Car safety systems have come a long way, but he was out to prove they could be outsmarted.",
    "When he had to picnic on the beach, he purposely put sand in other people’s food.",
    "You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.",
    "As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.",
    "I am never at home on Sundays.",
    "The Great Dane looked more like a horse than a dog.",
    "He realized there had been several deaths on this road, but his concern rose when he saw the exact number.",
    "I'm not a party animal, but I do like animal parties.",
    "There aren't enough towels in the world to stop the sewage flowing from his mouth.",
    "Jason lived his life by the motto, \"Anything worth doing is worth doing poorly.\"",
    "Most shark attacks occur about 10 feet from the beach since that's where the people are.",
    "For the 216th time, he said he would quit drinking soda after this last Coke.",
    "I would have gotten the promotion, but my attendance wasn’t good enough.",
    "David subscribes to the \"stuff your tent into the bag\" strategy over nicely folding it."
]


tokenizer = Tokenizer(num_words=500,oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences,maxlen=8,padding="post")
model = Sequential([
    Embedding(input_dim=500, output_dim=16,input_length=8),
    Flatten(),
    Dense(1,activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy")

import numpy as np
labels = np.array([0,1]*25)
model.fit(padded,labels,epochs=10)

weights = model.layers[0].get_weights()[0]
print(f"Shape of weights matrix: {weights.shape}")

word_to_lookup = "david"
word_id = tokenizer.word_index[word_to_lookup]
word_vector = weights[word_id]

print(f"Word: {word_to_lookup}")
print(f"Word ID: {word_id}")
print(f"Word Vector: {word_vector}")



