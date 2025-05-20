# Importation de la bibliothèque Streamlit pour créer des applications web
import streamlit as st
# Importation de la bibliothèque pandas pour la manipulation de données
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv')
arrondissements = df['pickup_borough'].unique()
# st.write(arrondissement)


# Titre principal de l'application (affiché en haut de la page)
st.title("Bienvenue sur le site de Vincent")

# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
arrondissement_select = st.selectbox("Indiquez votre arrondissement de récupération",
                                     arrondissements
                                     )

# Affichage d'un message en fonction de l'option sélectionnée
st.write('Tu as choisi :', arrondissement_select)

# On créer le lien de l'image en fonction de l'arrondissement sélectionné
if pd.isna(arrondissement_select):
    link_image = "images/nan.jpg"
else:
    arrondissement_select = arrondissement_select.lower()
    link_image = f"images/{arrondissement_select}.jpg"

# affichage de l'image corespondant à l'arrondissement sélectionné
st.image(link_image, width=800)
