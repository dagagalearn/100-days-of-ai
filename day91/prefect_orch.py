from prefect import task, flow
import numpy as np
import os
os.environ["PREFECT_API_URL"] = ""

@task(retries=3, retry_delay_seconds=15)
def generate_data():
  return np.random.rand(500,5)

@task()
def preprocess_data(data):
  return (data)*(10)

@task()
def present_data(data):
  print(f"The data has {data.shape} shape")


@task(retries=3, retry_delay_seconds=10)
def errorish_task():
  rand = np.random.rand()
  if rand<=0.5:
    raise ValueError("Hi. I have 50% chance of occuring")
  else:
    print("Ok")

@flow()
def all_in_one():
  raw_data = generate_data()
  processed_data = preprocess_data(raw_data)
  present_data(processed_data)
  errorish_task()

if __name__=="__main__":
  all_in_one()



