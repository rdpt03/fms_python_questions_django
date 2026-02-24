
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

  - **4.3**
    - Enregistrement des classes d'administration :
      - `admin.site.register(Question, QuestionAdmin)` → le modèle Question apparaît dans l’admin avec ses personnalisations 
      - `admin.site.register(Choice, ChoiceAdmin)` → (optionnel) le modèle Choice apparaît dans l’admin avec ses personnalisations*
    - Résultat : toutes les fonctionnalités ajoutées dans QuestionAdmin et ChoiceAdmin sont maintenant actives dans l’interface admin
    
  - **5**
    - Ajout d’un nouvel utilisateur via l’admin 
      - Ne pas donner “Statut équipe” ni “Statut super-utilisateur” → utilisateur créé
    - Tentative de connexion avec ce nouvel utilisateur → impossible
      - Message : “nom d’utilisateur ou mot de passe incorrect”
    - Explication : pour se connecter à l’admin, l’utilisateur doit avoir `is_staff=True` (Statut équipe)
      - Sans cela, Django refuse l’accès même si le compte existe et le mot de passe est correct
    - Conclusion : login impossible sans “Statut équipe”, c’est normal
  
  - **6**
    - Reconnexion avec l’administrateur (super-utilisateur)
    - Activation du compte de l’utilisateur et changement de mot de passe → OK
    - Résultat : l’utilisateur peut maintenant se connecter à l’interface admin
    
  - **7**
    - Désactivation du compte de l’utilisateur (au lieu de le supprimer) → OK
    - Tentative de connexion avec l’utilisateur désactivé → impossible
    - Conclusion : compte désactivé, l’utilisateur ne peut plus se connecter → OK