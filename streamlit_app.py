import streamlit as st
import pandas as pd
import requests

HORIZONTAL = "https://camo.githubusercontent.com/58f0d593d6ea48e93b0e1f325d489ac5a4ccfc82b0b8a6bfdaf781f21d9a6263/68747470733a2f2f692e696d6775722e636f6d2f415975745a4f462e706e67"
ICON = "https://user-images.githubusercontent.com/9741252/81717987-83b84000-947b-11ea-9ac9-5ad1d59adf7a.png"


st.logo(HORIZONTAL)
st.title("Pokedex | Generation 1-3")

poke_number = st.slider('Choose a Pokemon.', 1, 386)
url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}'
response = requests.get(url).json()

#element to isolate specific facts about that pokemon!
pokemon_name = response['name']
pokemon_height = response['height']
pokemon_weight = response['weight']
pokemon_image = response['sprites']['other']['dream_world']['front_default']

#code to display it! 
st.image(pokemon_image)
st.title(pokemon_name.title())


col1, col2 = st.columns(2)
col1.write('Height')
col2.write('Weight')

with col1:
    st.write(f'{pokemon_height} metres')
with col2:
    st.write(f'{pokemon_weight} kilograms')




















#st.title("📊 Data evaluation app")
#
#if 'counter' not in st.session_state.keys():
#    st.session_state['counter'] = 0 

#if st.button('Click me for a surprise!'):
#    st.snow()
#    st.session_state['counter'] += 1 
#
#st.write(f"You have clicked the button {st.session_state['counter']} times")

#my_title = st.empty()
#user_choice = st.radio('Which is the best?', options= ['cats', 'dogs'])
#my_title.title(f'Youve picked {user_choice}')

#sweets = st.slider('Please pick the best number of sweets in one day', 0, 100, 1)

#if sweets > 50:
#    st.write('fatty thats way too much')
#else:
#    st.write('quite alright')







