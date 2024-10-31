import openai
import pandas as pd

openai.api_key = "api"

def data_mobil(nama):
    car = cardata[cardata['nama_mobil'].str.lower() == nama.lower()]
    if not car.empty:
        return car.iloc[0]['jumlah']

def generate_answer(prompt):
    datam = data_mobil(prompt)
    response = openai.ChatCompletion.create(
        messages = [
            #{"role": "system", "content": "seorang sales mobil yang akan menjelaskan katalog mobil berdasarkan data"},
            #{"role": "assistant", "content" : datam},
            {"role": "user", "content": "prompt"}   
        ],
        model = 'gpt-3.5-turbo'
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    while True:
        user_input = input("masukkan jenis mobil: ")
        response = data_mobil(user_input) #generate_answer(user_input) #

        print("jumlah mobil adalah ", response)