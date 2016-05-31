from django.contrib import admin

from .models import Deck, Question, Alternative, Class, Reply

class QuestionInline(admin.TabularInline):
    model = Question

class AlternativeInline(admin.TabularInline):
    model = Alternative

class DeckAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AlternativeInline
    ]

admin.site.register(Deck, DeckAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Alternative)
admin.site.register(Class)
admin.site.register(Reply)
