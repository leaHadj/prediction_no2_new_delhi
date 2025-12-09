# Prédiction du NO₂ à New Delhi

Ce projet a pour objectif de prédire la concentration de dioxyde d’azote (NO₂) à +6 heures à partir de données historiques de pollution et de données météorologiques.

## Objectif
Anticiper les pics de pollution à New Delhi grâce à des modèles de machine learning (régression linéaire et Random Forest).

## Données
- Fichier principal : city_hour.csv
- Mesures horaires de polluants atmosphériques
- Données météorologiques récupérées via l’API Open-Meteo

## Méthodologie
1. Nettoyage des données
2. Fusion pollution + météo
3. Feature engineering
4. Analyse exploratoire (EDA)
5. Modélisation :
   - Baseline
   - Régression linéaire
   - Random Forest

## Résultats
Le Random Forest est le modèle le plus performant avec un R² d’environ 0.72.

## Librairies utilisées
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- requests

## Auteur
Lila Benabdallah
Léa Hadj-said
Faraa Awoyemi
