from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    """
    Gerenciador de usuário personalizado, onde o e-mail é o identificador exclusivo
    para autenticação em vez de nomes de usuários.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Criar e salvar um usuário com o email e a senha recebidas
        """
        if not email:
            raise ValueError("E-mail é obrigatório.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Criar e salvar um Super Usuário com o email e a senha recebidas.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário deve conter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário deve conter is_superuser=True.")
        return self.create_user(email, password, **extra_fields)
    
    def get_queryset(self):
        """
        Exclui todos usuários deletados lógicamente (soft delete) da vizualização.
        """
        return super().get_queryset().filter(is_deleted=False)

    def deleted(self):
        return super().get_queryset().filter(is_deleted=True)
    