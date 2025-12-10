# Prédiction du NO₂ à New Delhi

Ce projet a pour objectif de prédire la concentration de dioxyde d’azote (NO₂) à +6 heures à partir de données historiques de pollution et de données météorologiques. Il s’inscrit dans une démarche de Green AI visant à utiliser l’intelligence artificielle pour améliorer la qualité de vie et la santé publique.

---

## Objectif du projet

Anticiper les pics de pollution à New Delhi afin d’aider les citoyens, les écoles et les autorités locales à adapter leurs activités en cas de mauvaise qualité de l’air.  
Le projet combine une approche data science et une application interactive permettant d’exploiter facilement les prédictions.

---

## Données utilisées

- Fichier principal : `city_hour.csv`  
- Données horaires de polluants atmosphériques (dont le NO₂)  
- Données météorologiques récupérées via l’API Open-Meteo :  
  - Température  
  - Humidité  
  - Pression atmosphérique  
  - Vitesse du vent  
  - Précipitations  

---

## Méthodologie

1. Nettoyage et préparation des données  
2. Fusion des données pollution et météo  
3. Feature engineering (variables temporelles, valeurs passées du NO₂)  
4. Analyse exploratoire (EDA)  
5. Modélisation :  
   - Baseline  
   - Régression linéaire  
   - Random Forest  

---

## Résultats

Le modèle Random Forest obtient les meilleures performances avec un coefficient de détermination R² d’environ 0.72, montrant une bonne capacité à capturer les relations non linéaires entre les variables météorologiques et le NO₂.

---

## Application Streamlit

Une application web a été développée avec Streamlit afin de rendre les prédictions accessibles et simples à interpréter.

L’application permet de :  
- Entrer des conditions météorologiques récentes  
- Fournir les derniers niveaux de NO₂  
- Obtenir une prédiction du NO₂ à +6 heures  
- Visualiser une indication de la qualité de l’air (bonne, moyenne ou mauvaise)

---

## Librairies utilisées

- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- requests  
- streamlit  
- joblib  

---

## Auteurs

- Lila Benabdallah  
- Léa Hadj-Said  
- Faraa Awoyemi
