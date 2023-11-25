from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUserModel
	list_display = ("uuid", "first_name", "last_name", "email", "is_deleted") # , "is_staff", "is_superuser",
	fieldsets = (
		(None, {"fields": ("email", "password")}),
		("Informações Pessoais", {"fields": ("first_name", "last_name")}),
		("Permissões", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
		("Datas Importantes", {"fields": ("last_login", "date_joined")}),
	)
admin.site.register(CustomUserModel, CustomUserAdmin)
