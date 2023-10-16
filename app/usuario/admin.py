from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Usuario
from .forms import Usuario, UsuarioCreationForm, UsuarioChangeForm


class UsuarioAdmin(UserAdmin):

    fieldsets = (
    
        (None, {"fields": ("username","email", "password")}),

        #(_("Personal info"), {"fields": ('nombres','apellidos','genero')}),

        (_("Permissions"), {"fields": ('is_active', 'is_staff', 'is_superuser')}),

        #(_("Important dates"), {"fields": ('last_login','date_joined')}),

    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": ("username","email", "password1", "password2"),
            },
        ),
    )

    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    list_display = ('username','email','is_staff')
    search_fields = ('username','email')
    ordering = ('-id',)





# Register your models here.
admin.site.register(Usuario,UsuarioAdmin)