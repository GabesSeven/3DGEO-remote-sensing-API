from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUserModel
from .serializers import CustomUserCreateSerializer, CustomUserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

import time



class UserView(APIView):
    """
    Realiza CRUD de usuário comum e master.
    Somente usuário admin possuirá acesso a esta classe.
    """    
    permission_classes = [IsAuthenticated]

    def send_first_login_email(self, email, user):
        """
        Envia e-mail com token de primeiro acesso para usuário.
        """
        pass

    def post(self, request):
        """
        Realiza Create.
        """
        pass
    
        """
        Verifica se nome do grupo existe e não é null. 
        """
        
        """
        Restaura usuário caso já exista.        
        """
        
            # """
            # Adiciona usuário ao grupo.
            # """
            
            # """
            # Cria grupo se não existir e insere usuário.
            # """
            
            # """
            # Verifica se grupo já possui administrador.
            # """ 
            
            # """
            # Salva dados do usuário.
            # """
            
            # """
            # Envia e-mail de primeiro acesso.        
            # """
                
        """
        Verifica dados de entrada.        
        """
            # """
            # Salva usuário.
            # """
        
            # """
            # Cria grupo se não existir e insere usuário.
            # """
                
            # """
            # Verifica se grupo já possui administrador.
            # """ 
            
        """
        Envia e-mail de primeiro acesso.        
        """
        
    def get(self, request, uuid=None):
        """
        Realiza Read.
        """
        if uuid:
            user = CustomUserModel.objects.filter(uuid=uuid).first()
            if user:
                serializer = CustomUserSerializer(user)
                user_groups = user.groups.all()
                group_names = [group.name for group in user_groups]
                return Response({"info": "Sucesso ao ler usuário.", "data": serializer.data, "user_groups": group_names}, status=status.HTTP_200_OK)
            return Response({"info": "Erro ao encontrar usuário.", "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"info": "Erro ao encontrar usuário.", "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, uuid=None):
        """
        Realiza Update.
        """
        pass

        """
        Verifica se nome do grupo existe e não é null. 
        """
        
        """
        Verifica se usuário a ser atualizado existe.
        """
        
        """
        Verifica dados de entrada.
        """
        
            # """
            # Se o usuário logado pelo token for admin, permite fazer alterações.
            # """

            # """
            # Verifica se variáveis foram setadas corretamente.
            # """
        
            # """
            # Atualiza permissões.
            # """
        
            # """
            # Verificar se usuário é o único admin para grupo não ficar sem administrador.
            # """

            # """
            # Verifica se usuário está contido em algum grupo, se sim altera o nome desse grupo pelo nome do novo grupo.
            # """

    def delete(self, request, uuid=None):
        """
        Realiza Delete. 
        """
        pass
            # """
            # Remove o usuário de todos os grupos.
            # """
            
        """
        Percorre todos os grupos que o usuário pertence, verifica se é o unico admin, senão for exlui somente ele mesmo, se for exclui todo o grupo.
        """  
        
            # """
            # Remove o usuário apenas do grupo atual.
            # """
        
        """
        Varrer e deletar todos os grupos que estiverem vazios (sem nenhum usuário).
        """
        

class GetGroupView(APIView):
    """
    Obtém todos usuários de um determinado grupo.
    """
    pass
    
        # """
        # Verifica se usuário é anônimo.
        # """
    
        # """
        # Remover o usuário atual da lista de usuários.
        # """
    
class GetAllGroupsView(APIView):
    """
    Obtém todos usuários.
    """
    pass

        # """
        # Verifica se usuário é anônimo.
        # """
            
        # """
        # Remover o usuário atual da lista de usuários.
        # """
        
class LoginView(APIView):
    """
    Autenticação de usuário, posteriormente o retorno de um token ou mensagem de erro.
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
        except:
            return Response({"info": "Alguma variável não foi setada corretamente.", "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
        """
        Verifica se o email e a senha foram fornecidos na requisição.
        """
        if not email or not password:
            return Response({"info": "Informe email e senha válidos.", "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

        """
        Autentica o usuário usando o email e a senha.
        """
        user = authenticate(username=email, password=password)

        """
        Verifica se a autenticação foi bem-sucedida.
        """
        if user is not None:
            """
            Gera os tokens JWT e retorna resposta.
            """
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            user_groups = user.groups.all()
            group_names = []
            for group in user_groups:
                if group.name != "<grupo_do_administrador>": # NÃO É ESTE O NOME 
                    group_names.append(group.name)

            serializer = CustomUserSerializer(user)
            return Response({"access_token": access_token, "refresh_token": refresh_token, "data": serializer.data, "groups": group_names,"status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response({"info": "Email ou senha incorretos.", "status": status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)

class UpdateAccessView(APIView):
    """
    Verifica token de primeiro acesso de usuário e grava a senha vinda no corpo da requisição.
    """
    pass 
    
        # """
        # Verifica o token de autenticação e grava a senha fornecida no corpo da requisição.
        # """
    
        # """
        # Define a nova senha para o usuário e salva as alterações do usuário.
        # """
    