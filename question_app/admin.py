from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 3 champs vides pour ajouter des réponses directement dans Question

# Personalization admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # ajouter responses inline
    list_display = ['question_text', 'pub_date']  # colomnes qui apparaissent
    list_filter = ['pub_date']  # filtre par date a droite
    ordering = ['pub_date']  # ordre par default
    search_fields = ['question_text']  # barre de recherche

admin.site.register(Question, QuestionAdmin)