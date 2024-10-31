import openai
import pandas as pd
import numpy as np
import json

openai.api_key = "YOUR API"
car_data = "YOUR PATH FILE"

#Encode ur CSV file
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        return super().default(obj)
        
def data_mobil(nama):
    car = car_data[cardata['model'].str.lower() == nama.lower()]
    if not car.empty:
        return car.iloc[0] # Get all-row information

def generate_answer(prompt, datam):
    datam_dict = datam.to_dict() if datam is not None else {}
    response = openai.ChatCompletion.create(
        messages = [
            {"role": "system", "content": "A car salesperson who will explain the car catalog based on data"},
            {"role": "user", "content": "prompt"},
            {"role": "assistant", "content" : json.dumps(datam_dict, cls=NpEncoder)}   
        ],
        model = 'gpt-3.5-turbo'
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    while True:
        user_input = input("Car's model: ")
        car_info = data_mobil(user_input)

        if car_info is not None:
            response = generate_answer(user_input, car_info)
            print(response)
        else:
            print("Model not found")
