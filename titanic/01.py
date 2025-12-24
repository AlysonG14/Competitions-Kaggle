import pandas as pd

df = pd.read_csv('data.csv', index_col='Name')
df.head(10)

Pokemon = []

def search_pokemons():
    for i in range(3):
        pokemons_input = str(input(f'Type the {i + 1}° pokemon: '))
        Pokemon.append(pokemons_input)
        print(Pokemon)

    print('Pokemons added: {}'.format(Pokemon))

    try:
        print(df.loc[Pokemon])
    except KeyError:
        print("Pokemon: {} not found!".format(Pokemon))

search_pokemons()