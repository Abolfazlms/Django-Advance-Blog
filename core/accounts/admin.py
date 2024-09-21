from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Register your models here.
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ("email",)


# class CustomUserCreationForm(forms.ModelForm):
#     password1=forms.CharField(label='Password', widget=forms.PasswordInput)
class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = CustomUserCreationForm
    list_display = ("email", "is_superuser", "is_active", "is_verified")
    list_filter = ("email", "is_superuser", "is_active", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        ("AUTHENTICATION", {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
        ("Group Permissions", {"fields": ("groups", "user_permissions")}),
        ("Important Date", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
