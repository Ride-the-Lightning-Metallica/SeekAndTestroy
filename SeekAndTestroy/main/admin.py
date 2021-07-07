from django.contrib import admin

from main import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


class QuestionInline(admin.StackedInline):
    model = models.Question


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    inlines = [QuestionInline]


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('first_name', 'last_name', 'slug')


admin.site.register(models.Question)
