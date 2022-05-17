from django.contrib import admin

from .models import Learningspace, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class LearningspaceAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Learningspace, LearningspaceAdmin)