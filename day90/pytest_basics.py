import pytest
import numpy as np

def normalize(data):
  if data is  None or len(data)==0:
    raise ValueError("Value can't be emptyy")
  else:
    data = (data-np.min(data)) / (np.max(data)-np.min(data))
    return data

def predict(weights, x):
  return np.dot(weights, x)


def test_normalize_data():
  data = np.array([0,3,6])
  result = normalize(data)
  assert result.min() == 0
  assert result.max() == 1

def test_checkshape():
  x = np.array([0,3,6])
  weights = np.array([0.3,-0.25,0.9])
  result = predict(weights,x)
  assert isinstance(result, (int,float,np.number))

def test_checknull():
  with pytest.raises(ValueError):
    normalize(np.array([]))


test_checkshape()
test_checknull()
test_normalize_data()
print("Passed")

