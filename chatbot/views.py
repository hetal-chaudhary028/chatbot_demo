from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Message
import json

@ensure_csrf_cookie
def index(request):
    return render(request, 'chatbot/index.html')

def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '').lower()
        
        # Simple knowledge base for Web Auth/Auth
        responses = {
            'authentication': 'Authentication is the process of verifying who a user is. Common methods include passwords, multi-factor authentication (MFA), and biometric data.',
            'authorization': 'Authorization is the process of verifying what a user has access to. For example, an admin can delete users, but a regular user cannot.',
            'jwt': 'JSON Web Token (JWT) is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. It is often used for authentication.',
            'oauth': 'OAuth is an open standard for access delegation, commonly used as a way for Internet users to grant websites or applications access to their information on other websites but without giving them the passwords.',
            'session': 'Session-based authentication is where the server creates a session for the user after they log in. The session ID is stored in a cookie on the client side.',
            'rbac': 'Role-Based Access Control (RBAC) is a method of restricting network access based on the roles of individual users within an enterprise.',
            '2fa': 'Two-Factor Authentication (2FA) is a security process in which users provide two different authentication factors to verify themselves.',
        }
        
        bot_response = "I am sorry, I cannot find the answer to that question. Please ask something else about Authentication and Authorization!"
        
        for key in responses:
            if key in user_message:
                bot_response = responses[key]
                break
        
        # Save to database
        Message.objects.create(user_message=user_message, bot_response=bot_response)
        
        return JsonResponse({'response': bot_response})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
