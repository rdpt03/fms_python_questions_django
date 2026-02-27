
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
---
## 2.2.2.1
  - Ouvrir un terminal → OK
  - Aller dans le répertoire du projet → OK
  - Lancer `python manage.py shell` → OK
---
## 2.2.2.2
  - 1 : 
    - Lister toutes les Questions :
      - Commande utilisée : [i.question_text for i in Question.objects.all()]
      - Résultat :
        - `'Comment ça va?'`
        - `'Quel type de musique aimez vous?'`
        - `'Qui est le moins cher'`
        - `'Quel est ta couleur préféré'`
        - `'Quel est le meilleur reseau de bus?'`

  - 2 : 
    - Filtrage par date de publication :
      - Commande utilisée dans le shell Django :
          ```
          questions_2026 = Question.objects.filter(pub_date__year=2026)
          for q in questions_2026: print(q.question_text)
          ```
      - Résultat obtenu :
        - 'Comment ça va?'
        - 'Quel type de musique aimez vous?'
        - 'Qui est le moins cher'
        - 'Quel est ta couleur préféré'
        - 'Quel est le meilleur reseau de bus?'
      - Observations : le filtre permet de sélectionner un sous-ensemble de questions selon un composant de la date (année, mois ou jour)

  - 3 : 
    - Question avec id = 2 :
      - Commande utilisée :
        ```
        q2 = Question.objects.get(id=2)
        print(q2.question_text, q2.pub_date)
        for c in q2.choice_set.all(): print(c.choice_text, c.votes)
        ```
      - Résultat obtenu :
        - Question : 'Quel type de musique aimez vous?'
        - Date de publication : 2026-01-21 18:50:22+00:00
        - Choix associés :
          - 'Dance' | Votes: 0
          - 'Rock' | Votes: 0
          - 'Rap' | Votes: 0
    - Observations : la relation entre Question et Choice permet d’afficher facilement toutes les réponses liées à cette question via choice_set.all().

  - 4 : 
    - Boucle pour toutes les Questions et leurs Choices :
      - Commande utilisée dans le shell Django :
        ```
        for q in Question.objects.all():
        print("Question:", q.question_text)
        print("Date de publication:", q.pub_date)
        for c in q.choice_set.all():
            print("  Choice:", c.choice_text, "| Votes:", c.votes)
        ```
      - Résultat obtenu :
        - Question : 'Comment ça va?'
          - Choices : 'Super Bien' | Votes: 0, 'Bien' | Votes: 0, 'Bof' | Votes: 0
        - Question : 'Quel type de musique aimez vous?'
          - Choices : 'Dance' | Votes: 0, 'Rock' | Votes: 0, 'Rap' | Votes: 0
        - Question : 'Qui est le moins cher'
          - Choices : 'Leclerc' | Votes: 0, 'Carrefour' | Votes: 0, 'Intermarché' | Votes: 0
        - Question : 'Quel est ta couleur préféré'
          - Choices : 'Bleu' | Votes: 0, 'Rouge' | Votes: 0, 'Jaune' | Votes: 0
        - Question : 'Quel est le meilleur reseau de bus?'
          - Choices : 'Txik Txak' | Votes: 0, 'RATP' | Votes: 0, 'FLIXBUS' | Votes: 0
      - Observations : la boucle permet de lister toutes les questions avec leurs réponses, pratique pour vérifier la base de données et préparer l’interface admin.

  - 5 :
    - Nombre de choix par Question :
      - Commande utilisée :
        ```
        for q in Question.objects.all():
          nb_choix = q.choice_set.count()
          print("Question:", q.question_text, "| Nombre de choix:", nb_choix)
        ```
    - Résultat obtenu :
      - Question : `'Comment ça va?'` | Nombre de choix : `3`
      - Question : `'Quel type de musique aimez vous?'` | Nombre de choix : `3`
      - Question : `'Qui est le moins cher'` | Nombre de choix : `3`
      - Question : `'Quel est ta couleur préféré'` | Nombre de choix : `3`
      - Question : `'Quel est le meilleur reseau de bus?'` | Nombre de choix : `3`
    - Observations : chaque question a exactement 3 choix enregistrés, conforme à l'exercice précédent.

  - 7 : 
    - Tri des Questions par ordre antéchronologique :
      - Commande utilisée :
        ```
        questions_triees = Question.objects.all().order_by('-pub_date')
        for q in questions_triees:
            print(q.question_text, q.pub_date)
        ```
      - Résultat obtenu :
        - `'Quel est ta couleur préféré'` | `2026-02-22 18:52:41+00:00`
        - `'Qui est le moins cher'` | `2026-02-20 18:51:28+00:00`
        - `'Quel est le meilleur reseau de bus?'` | `2026-02-16 09:53:32+00:00`
        - `'Quel type de musique aimez vous?'` | `2026-01-21 18:50:22+00:00`
        - `'Comment ça va?'` | `2026-01-19 18:38:15+00:00`
      - Observations : la liste est triée du plus récent au plus ancien selon pub_date.

  - 9 : 
    - Créer une nouvelle Question et ses Choices via le shell Django :
      - Commandes utilisées :
        ```
        from question_app.models import Question, Choice
        from django.utils import timezone
    
        q = Question.objects.create(
            question_text="Quel est ton plat préféré?",
            pub_date=timezone.now()
        )
        Choice.objects.create(question=q, choice_text="Pizza", votes=0)
        Choice.objects.create(question=q, choice_text="Pâtes", votes=0)
        Choice.objects.create(question=q, choice_text="Sushi", votes=0)
    
        print(q.question_text)
        for c in q.choice_set.all():
            print(c.choice_text, c.votes)
        ```
      - Résultat obtenu :
        - Question : `'Quel est ton plat préféré?'`
        - Choices : `'Pizza' | Votes: 0`, `'Pâtes' | Votes: 0`, `'Sushi' | Votes: 0`
      - Observations : la création d’une Question et de ses Choices se fait entièrement dans le shell, sans passer par l’interface admin.
  - 10 : 
    - Ajouter 3 Choices supplémentaires à la Question "Quel est ton plat préféré?" :
      - Commandes utilisées :
        ```
        # Récupérer la question existante
        q = Question.objects.get(question_text="Quel est ton plat préféré?")
          
        # Ajouter 3 nouvelles choices
        Choice.objects.create(question=q, choice_text="Burger", votes=0)
        Choice.objects.create(question=q, choice_text="Salade", votes=0)
        Choice.objects.create(question=q, choice_text="Sushi végétarien", votes=0)
        
        # Vérifier le résultat
        for c in q.choice_set.all():
          print(c.choice_text, c.votes)
        ```
      - Résultat obtenu :
        ```
        Pizza 0
        Pâtes 0
        Sushi 0
        Burger 0
        Salade 0
        Sushi végétarien 0
        ```
      - Observations :
        - La Question contient maintenant 6 Choices.
        - L’ajout de nouvelles Choices se fait facilement dans le shell sans passer par l’interface admin.
        - Certaines combinaisons comme "Sushi végétarien" peuvent sembler étranges, mais c’est intéressant pour tester la flexibilité du modèle.
  - 11 : 
    - Lister les questions publiées récemment (derniers 7 jours) :
      - Commandes utilisées :
        ```
        from question_app.models import Question
        from django.utils import timezone
        from datetime import timedelta
    
        maintenant = timezone.now()
        une_semaine = maintenant - timedelta(days=7)
    
        questions_recentes = Question.objects.filter(pub_date__gte=une_semaine)
    
        for q in questions_recentes:
        print("Question:", q.question_text, "| Date de publication:", q.pub_date)
        ```
      - Résultat obtenu :
        ```
        Question: Qui est le moins cher | Date de publication: 2026-02-20 18:51:28+00:00
        Question: Quel est ta couleur préféré | Date de publication: 2026-02-22 18:52:41+00:00
        Question: Quel est ton plat préféré? | Date de publication: 2026-02-24 10:51:14.188482+00:00
        ```
      - Observations :
        - Le filtre `pub_date__gte=une_semaine` permet de récupérer toutes les questions publiées récemment, ici dans les `7` derniers jours.
        - On peut facilement ajuster la période en modifiant `timedelta(days=…)`.
---
## 3.2
  - ##### 1 : Affichage de la date de publication dans `index.html`
    - Objectif : montrer la date de publication à côté du titre de chaque sondage.
    - Template : `index.html`
    - Vue : `index()`
    - Résultat :
    ```
    Comment ça va? — Publié le 19/01/2026 18:38
    Quel type de musique aimez vous? — Publié le 21/01/2026 18:50
    Qui est le moins cher — Publié le 20/02/2026 18:51
    Quel est ta couleur préféré — Publié le 22/02/2026 18:52
    Quel est le meilleur reseau de bus? — Publié le 16/02/2026 09:53
    Quel est ton plat préféré? — Publié le 24/02/2026 10:51
    ```
    - Notes : l’affichage utilise `{{ question.pub_date|date:"d/m/Y H:i" }}`. 
    - La racine `/` pointe vers cette page via urls.py.

  - ##### 2 : Liste de toutes les questions `/polls/all/` et page de détail
    - Objectif : lister toutes les questions avec id et titre, chaque titre cliquable vers sa page de détail. 
    - Templates : showall.html et showdetails.html 
    - Vues : showall() et showone()
    - Fonctionnalité :
      - `/polls/all/` : liste toutes les questions avec leur id et titre, titres cliquables 
      - `/polls/<id>/details/` (showdetails) : affiche question + date + toutes les réponses + nombre de votes 
    - Exemple de sortie pour une question :
    ```
    id : 2
    question : Quel type de musique aimez vous?
    Publié le : 21/01/2026 18:50
    Réponses :
    - Dance | Vote : 0
    - Rock | Vote : 0
    - Rap | Vote : 0
    ```
    - Notes : accès aux réponses via question.choice_set.all() ; chaque lien construit dynamiquement avec <int:question_id> dans urls.py.
  - ##### 3 : Page des résultats du sondage (`/polls/<id>/frequency/`)
    - Objectif : afficher les résultats d’un sondage avec le nombre de votes et le pourcentage pour chaque réponse. 
    - Modification réalisée :
      - lien des questions dans `/polls/all/` modifié pour pointer vers `/polls/<id>/frequency/`
      - création d’une vue qui calcule :
        - total des votes 
        - pourcentage pour chaque réponse 
      - affichage des résultats dans un template dédié 
      - Accès aux réponses :
        question.choice_set.all()
      - Protection appliquée :
        gestion du cas où le total de votes = 0 (pas de division par zéro). 
      - Résultat obtenu :
      ```
      Comment ça va?
      Super Bien — Votes: 25 — 50,0%
      Bien — Votes: 15 — 30,0%
      Bof — Votes: 10 — 20,0%
      ```
      - Conclusion :
        la page frequency permet d’afficher les résultats du sondage de manière lisible avec valeurs absolues et relatives.

  - ##### 4 : Page de statistiques (`/polls/statistics/`)
    - Objectif : afficher des statistiques globales sur les sondages. 
    - Informations affichées :
      - Nombre total de sondages : `6`
      - Nombre total de choix : `21`
      - Nombre total de votes : `50`
      - Moyenne de votes par sondage : `8,33`
      - Dernière question enregistrée : `24/02/2026 - 11:51`
    - Notes :
      - Les calculs utilisent les fonctions d’agrégation de Django : Count, Sum, Max. 
      - La vue protège contre la division par zéro pour la moyenne. 
    - Résultat obtenu :
      ```
      Total de sondages : 6
      Total de choix : 21
      Total de votes : 50
      Moyenne de votes par sondage : 8,33
      Dernière question enregistrée : 24/02/2026 11:51
      ```
  - ##### 5 : Ajout d’un formulaire de création de question
    - Un formulaire a été ajouté afin de permettre la création d’une nouvelle question depuis l’interface web. 
    - Un lien a été intégré dans la page principale (index.html) pour accéder au formulaire d’ajout. 
    - Deux routes ont été définies :
      - `/polls/add/` : affiche le formulaire de saisie 
      - `/polls/confirm_add/` : traite l’envoi du formulaire

    - La vue de confirmation récupère le texte saisi, supprime les espaces inutiles et vérifie que le champ n’est pas vide. 
    - Si le texte est valide, une nouvelle question est créée avec la date courante (timezone.now()) puis enregistrée en base de données. 
    - Si le champ est vide, le formulaire est réaffiché avec un message d’erreur. 
    - Deux templates ont été ajoutés :
      - `add.html` : formulaire de saisie d’une question 
      - `confirm_add.html` : message de confirmation après enregistrement
    - ##### Résultat obtenu :
      - L’utilisateur peut ajouter une question via le site. La question est enregistrée avec sa date de publication et un message de confirmation est affiché.
  

  - ##### 6 : Ajout de choix lors de la création d’une question
    - Le formulaire de création de question a été enrichi pour permettre la saisie de jusqu’à 5 choix directement lors de l’ajout d’une question. 
    - #### Fonctionnement :
      - Dans views.py, une constante NB_MAX_CHOIX = 5 définit le nombre maximum de champs de saisie pour les choix. 
      - La vue add transmet à la template une liste pour générer les 5 champs de saisie. 
      - La vue confirm_add récupère le texte de la question et, si valide, crée la question en base avec la date courante. 
      - Ensuite, elle parcourt les champs de choix saisis (choix_0 à choix_4) :
        - Les champs non vides sont ajoutés comme objets Choice liés à la question. 
        - Le traitement s’arrête dès qu’un champ vide est rencontré, pour ne pas créer de choix vides. 
    - Si le texte de la question est vide, le formulaire est réaffiché avec un message d’erreur. 
    - Template `add.html` :
      - Affiche la saisie de la question 
      - Affiche dynamiquement 5 champs de saisie pour les choix 
      - Bouton de soumission 
    - Résultat obtenu :
      - L’utilisateur peut créer une nouvelle question et ajouter jusqu’à 5 choix en même temps. 
      - Seuls les champs remplis sont pris en compte et enregistrés en base de données.