from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import*
from import_export import resources

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    pass
