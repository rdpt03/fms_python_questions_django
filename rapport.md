
- creation -> OK
- config -> OK
- add app -> OK
# Exercices
## 2.2.1

  - **1** :
    - creation des modèles : OK
    - migrations appliquées : OK
    - enregistrement dans `admin.py` : OK

  - **2** :
    - accès à l’interface admin → nécessite un utilisateur
    - création du superuser avec `python manage.py createsuperuser`
    - ENTITÉS NON VISIBLES : app non ajoutée dans `INSTALLED_APPS` → corrigé
    - ajout des réponses directement lors de la création d’une question (inline admin)
    - erreur lors de l’ajout : tables non migrées → corrigé
    - création de 5 questions avec 3 réponses chacune

  - **3** :    
    - Voyez-vous tous les attributs de vos classes ?
      - oui → texte, date, réponses, votes
    - Pouvez-vous filtrer vos données selon les attributs ?
      - non, pas avec l’admin par défaut
    - Pouvez-vous trier vos données selon les attributs ?
      - non, pas avec l’admin par défaut
    - Pouvez-vous chercher un contenu parmi tous les champs ?
      - non, pas avec l’admin par défaut

  - **4.1** :    
    - création de 2 classes d’administration personnalisées :        
      - QuestionAdmin : OK
      - ChoiceAdmin : OK

  - **4.2** :
    - ajout des options ModelAdmin sur les deux classes :
      - `list_display` → afficher plusieurs attributs : OK
      - `list_filter` → filtrage dans l’interface : OK            
      - `ordering` → tri automatique des données : OK
      - `search_fields` → barre de recherche : OK
    - Résultat :
      - affichage complet des données
      - filtrage disponible
      - tri fonctionnel
      - recherche active dans l’admin