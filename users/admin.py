from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

# Register your models here.


class UserAdminConfig(UserAdmin):
    model = User
    list_per_page = 10

    search_fields = ('email', 'username',)
    list_filter = (('date_joined', DateRangeFilter),
                   'is_superuser', 'is_staff', 'account_activated')
    ordering = ('email',)
    list_display = ('email', 'username', 'is_superuser',
                    'is_staff', 'account_activated', 'date_joined',)
    list_display_links = ('username',)

    fieldsets = (
        ('Personal', {
         'fields': ('email', 'username')}),
        ('Permissions', {
         'fields': ('is_superuser', 'is_staff', 'account_activated')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'account_activated')}
         ),
    )


admin.site.register(User, UserAdminConfig)
