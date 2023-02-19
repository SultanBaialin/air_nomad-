from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

# from Hacaton final.tasks import send_confirm_email_task
from . import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from air_nomad.tasks import send_confirmation_tasks_email
from .send_mail import send_reset_email
import logging

User = get_user_model()

logger = logging.getLogger('main')


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                try:
                    send_confirmation_tasks_email.delay(user.email, user.activation_code)
                    # send_confirm_email_task.delay(user.email, user.activation_code)
                except:
                    logger.info('registration')
                    return Response({'msg': 'Registered but troubles with mail!',
                                     'data': serializer.data}, status=201)
            logger.info('registration')
            return Response(serializer.data, status=201)
        logger.debug('registration')
        return Response('Bad request', status=404)


class ActivationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            logger.info('active')
            return Response({
                'msg': 'Successfully activated!'
            }, status=200)
        except User.DoesNotExist:
            logger.debug('active')
            return Response ({'msg': 'Link expired!'}, status=400)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class LogoutView(GenericAPIView):
    serializer_class = serializers.LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info('logout')
        return Response('Successfully logged out!', status=200)


class ForgotPasswordView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = serializers.ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            email = serializer.data.get('email')
            user = User.objects.get(email=email)
            user.create_activation_code()
            user.save()
            send_reset_email(user)
            logger.info('code sent')
            return Response('Check your email. We send a code', 200)
        except User.DoesNotExist:
            logger.warning('does not exist')
            return Response('User with this email does not exist!', status=400)


class RestorePasswordView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = serializers.RestorePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info('password changed')
        return Response('Password changed successfully!')