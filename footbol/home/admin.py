from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from home.models import table, date, news, forum, month, matches
from reg.models import CustomUser

admin.site.register(table)
admin.site.register(date)
admin.site.register(news)
admin.site.register(forum)
admin.site.register(month)
admin.site.register(matches)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['username', 'student', 'year', 'is_staff']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Данные ученика', {
                'fields': (
                    'year',
                    'student',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Данные ученика',
            {
                'fields': (
                    'year',
                    'student',
                )
            }
        )
    )
