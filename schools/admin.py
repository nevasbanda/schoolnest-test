from django.contrib import admin
from . models import School
from . models import Province

# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name', 'country', 'district', 'suburb', 'is_published', 'created_at')
    list_display_links = ('id', 'school_name')
    list_filter = ('country', 'district', 'suburb', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('school_name', 'country', 'district', 'suburb')


admin.site.register(School, SchoolAdmin)
admin.site.register(Province)
