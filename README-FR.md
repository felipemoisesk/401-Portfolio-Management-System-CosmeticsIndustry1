<h1 align="center">
     <a> 401-Gestion-Portefeuille-IndustrieCosmétique</a>
</h1>

<h4 align="center">
	🚧 OCT/21 jusqu'à MAR/22 🚀 🚧
</h4>

## 💻 À propos du projet

Le système de gestion de portefeuille, ou SGP, est un système développé pour le cœur du portefeuille et des catégories, la direction de l'intelligence du marché, qui offre une vue détaillée du portefeuille de vente au détail, au niveau du SKU, en tenant compte de la collecte, du traitement, de la démocratisation et de l'analyse des données pour le parties prenantes de l'entreprise.

L'outil suivant couvre la phase ETL du projet, collectant et traitant les données des différents systèmes de l'entreprise, mises à disposition après extraction dans des fichiers .xlsx ou .csv, principalement.

La construction de cet outil a réduit le temps de traitement de 87% par rapport à la solution originale qui était développée sous Excel par l'équipe précédemment responsable, de +8h à moins de 1h, considérant le début du traitement jusqu'à la livraison finale avec pré-analyse et outil imprimerie.

Afin de répondre aux besoins d'une équipe majoritairement composée de personnes ayant des compétences métiers, Microsoft SharePoint a été choisi comme référentiel de fichiers bruts, traités et raffinés, émulant un environnement en couches (Bronze, Silver et Gold) déjà connu dans les pipelines ETL en ingénierie des données.

Dans le cadre de l'analyse des données, des tableaux de bord dans Tableau et PowerBI ont été mis à la disposition de l'équipe, y compris la modélisation dimensionnelle des données dans les deux.

Le projet apporte de la valeur et de l'autonomie à l'équipe métier, de l'ETL à l'autoconsommation de données et aux analyses d'équipe.

---

## ⚙️ Fonctionnalités

- [x] **Automatisation ETL** :
  - [x] création de datamart, localhost et Microsoft SharePoint, en couches Bronze, Silver et Gold :
    - bronze : données extraites des systèmes aux formats TXT, XLSX et CSV
    - silver : données traitées, nettoyées et organisées dans des fichiers tabulaires
    - d'or : données affinées, avec modélisation dimensionnelle appliquée pour l'entrée dans les outils de dataviz de l'entreprise
  - [x] interaction entre le script et l'utilisateur :
    - navigation entre les modules et sous-modules que vous souhaitez mettre à jour de manière interactive et didactique, au travers de questions et sélection de réponses

- [x] **Outil construit sur des modules interconnectés** :
  - [x] module de performance financière
    - régions géographiques
    - régions commerciales
    - canaux de vente
  - [x] Module de planification commerciale
    - régions géographiques
    - canaux de vente

---

## 🚀 Comment exécuter l'outil


Lors de l'exécution des scripts, l'utilisateur recevra des questions sur l'écran d'exécution concernant les modules qu'il souhaite mettre à jour.

Cependant, cet outil est composé de trois étapes :

1. Collecte d'informations transactionnelles de l'entreprise, via xlsx/txt/csv, ou rapports générés dans les différents systèmes et départements de l'entreprise (insertion de la couche Bronze)
2. Exécution automatisée de scripts python pour le traitement, le nettoyage des données, la modélisation dimensionnelle des données et la pré-organisation des fichiers de données (insertion de la couche d'argent)
3. Disponibilité en référentiel, en sortie, des données traitées selon les besoins métiers (insertion Gold layer)

💡 La visualisation des données via Tableau ou PowerBi utilise la sortie de la couche Gold de l'outil.

### Conditions préalables

Comme il s'agit d'un outil qui fonctionne localement, avant de commencer, vous devrez télécharger ce projet sur votre machine, afin que les référentiels soient déjà liés au répertoire du projet. Je recommande également de télécharger [Git](https://git-scm.com) pour le contrôle de version. À propos de l'IDE, j'ai utilisé [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux).

---

## 🛠 Technologies

Les outils suivants ont été utilisés dans la construction du projet :

#### **ETL**  ([Python](https://www.python.org/))

-   **[Pandas](https://pandas.pydata.org/)**
-   **[NumPy](https://github.com/ReactTraining/react-router/tree/master/packages/react-router-dom)**
-   **[OS](https://docs.python.org/3/library/os.html)**
-   **[Matplotlib](https://matplotlib.org/)**

### **Visualisation de données**

-   **[Tableau](https://www.tableau.com/)**
-   **[PowerBI](https://powerbi.microsoft.com/pt-br/)**

### **Dépôt de données**

-   **[Microsoft SharePoint](https://www.microsoft.com/pt-br/microsoft-365/sharepoint/collaboration)**

#### **Utilitaires**

-   Éditeur:  **[PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux)**

---

## 📝 Licence

Ce projet est sous licence [MIT](./LICENSE).

Réalisé avec ❤️ par Felipe Möises 👋🏽 [Prendre contact!](https://www.linkedin.com/in/felipemoises/)

---

##  Versions README

[Portugais 🇧🇷](./README-PT.md)  |  [Anglais 🇺🇸](./README.md)
