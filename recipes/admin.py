from django.contrib import admin
from .models import Recipe, Category, Difficulty, Enrollment

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category__name', 'difficulty__name',
                     'total_servings', 'rating', 'preparation_time',)
    list_filter = ('category', 'difficulty',)
    ordering = ('-date_posted',)
    list_display = ('title', 'total_servings', 'preparation_time',
                    'category', 'difficulty', 'rating',)
    fieldsets = (
        ('About', {'fields': ('title', 'description',)}),
        ('Requirements', {'fields': ('total_servings', 'preparation_time',)}),
        ('Description', {'fields': ('rating', 'category', 'difficulty',)}),
        ('Chef', {'fields': ('chef',)}),
    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Enrollment)
