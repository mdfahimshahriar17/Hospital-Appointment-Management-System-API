from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework.views import APIView


from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated

from django.conf import settings

from .serializers import RegisterSerializer
from .serializers import ProfileSerializer

from .models import User

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer




class ForgotPasswordView(APIView):

    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'detail': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        token = default_token_generator.make_token(user)

        send_mail(
            subject='Password Reset',
            message=f'Your password reset token is: {token}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        return Response(
            {'detail': 'Password reset token sent.'},
            status=status.HTTP_200_OK
        )


class ResetPasswordView(APIView):

    def post(self, request):
        email = request.data.get('email')
        token = request.data.get('token')
        password = request.data.get('password')
        password2 = request.data.get('password2')

        if password != password2:
            return Response(
                {'password': 'Passwords do not match.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'detail': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if not default_token_generator.check_token(user, token):
            return Response(
                {'detail': 'Invalid or expired token.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(password)
        user.save()

        return Response(
            {'detail': 'Password reset successful.'},
            status=status.HTTP_200_OK
        )



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = ProfileSerializer(request.user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def patch(self, request):
        serializer = ProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
