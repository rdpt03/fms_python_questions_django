from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 3 champs vides pour ajouter des réponses directement dans Question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # montre les Choices dans la page Question

admin.site.register(Question, QuestionAdmin)