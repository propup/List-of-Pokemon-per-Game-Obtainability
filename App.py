import streamlit as st
import pandas as pd
import ast

df = pd.read_csv("CSVs/Master_set_per_games.csv")
dfDex = pd.read_csv("CSVs/MasterDex.csv", engine='python')

df = df.merge(dfDex, on=['National_Dex', 'Pokemon'])


st.set_page_config(layout="wide")


uniqueGames= set()
df["Games"] = df["Games"].apply(ast.literal_eval)
df["National_Dex"] = df["National_Dex"].astype(int).astype(str)
df["Dex"] = df["Dex"].apply(ast.literal_eval)



for games in df["Games"]:
    for game in games:
        uniqueGames.add(game)

uniqueDex = set()

for dexs in df["Dex"]:
    for dex in dexs:
        uniqueDex.add(dex)


st.title("Pokémon Database")

search = st.text_input("Search for a Pokémon (Name or National Dex #)")

if search:
    if search.isdigit():
        filtered_df = df[df["National_Dex"].astype(int) == int(search)]
    else:
        filtered_df = df[df["Pokemon"].str.contains(search, case=False, na=False)]
else:
    filtered_df = df

show_based_on_games = st.multiselect(label="Sort by Games",
                                     options=sorted(uniqueGames))

if show_based_on_games:
    filtered_df = filtered_df[
        filtered_df["Games"].apply(
            lambda games: all(game in games for game in show_based_on_games)
        )]

show_based_on_Dex = st.multiselect(label="Sort by Dexs",
                                     options=sorted(uniqueDex))

if show_based_on_Dex:
    filtered_df = filtered_df[
        filtered_df["Dex"].apply(
            lambda dexs: all(dex in dexs for dex in show_based_on_Dex)
        )]

if(show_based_on_games):
    st.subheader(f"Showing Pokemon that are at least in : {' and '.join(show_based_on_games)}")

st.dataframe(filtered_df, hide_index=True,column_config={
        "National_Dex": st.column_config.TextColumn(width=55),
        "Pokemon": st.column_config.TextColumn(width=110),
        "Form": st.column_config.TextColumn(width=100),
        "Games":st.column_config.ListColumn(width=1300),
        "Dex": None
},width="stretch",height=600)

st.subheader(f"Showing {len(filtered_df)} Pokemon (Includes different Forms)")

st.caption("Event, Friend Safri, require glitchs, dns exploits, 3ds acting as fake wfi distributor; May or May not be included (They had to be manually added)")

st.caption('Also Forms are not fully implemented due to some data not including it')

