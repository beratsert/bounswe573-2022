from django.contrib import admin

from .models import Workspace, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class WorkspaceAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Workspace, WorkspaceAdmin)