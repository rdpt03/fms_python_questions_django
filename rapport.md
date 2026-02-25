
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
  - Objectif : Ajouter la date de publication à côté du titre de chaque sondage dans la page principale.
  - Fichiers modifiés :
    - `question_app/templates/question_app/index.html`
    - `question_app/views.py` (déjà existant)
    - `questionProject/urls.py` (pour que la racine / pointe sur index)
  - Modifications apportées :
  #### index.html :
  ```
  <ul>
  {% for question in latest_question_list %}
      <li>{{ question.question_text }} — Publié le {{ question.pub_date|date:"d/m/Y H:i" }}</li>
  {% endfor %}
  </ul>
  ```

  #### urls.py :
  ```
  from django.contrib import admin
  from django.urls import path
  from question_app import views
    
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', views.index, name='index'),  # la racine pointe sur index.html
  ]
  ```
  #### views.py :
  ```
  from django.shortcuts import render
  from .models import Question

  def index(request):
      latest_question_list = Question.objects.order_by('-pub_date')[:5]
      context = {'latest_question_list': latest_question_list}
      return render(request, 'question_app/index.html', context)
  ```
  - Résultat obtenu dans le browser (http://127.0.0.1:8000/) :
  ```
  Comment ça va? — Publié le 19/01/2026 18:38
  Quel type de musique aimez vous? — Publié le 21/01/2026 18:50
  Qui est le moins cher — Publié le 20/02/2026 18:51
  Quel est ta couleur préféré — Publié le 22/02/2026 18:52
  Quel est le meilleur reseau de bus? — Publié le 16/02/2026 09:53
  Quel est ton plat préféré? — Publié le 24/02/2026 10:51
  ```
  - Observations :
    - Même sans créer explicitement /polls, la racine / montre les sondages avec leur date.
      - La méthode {{ question.pub_date|date:"d/m/Y H:i" }} permet de formater la date pour plus de lisibilité. 
      - Cette étape correspond uniquement à l’item 1 de l’exercice 3.2. Les items 2 et 3 seront réalisés plus tard avec de nouvelles URLs et templates.