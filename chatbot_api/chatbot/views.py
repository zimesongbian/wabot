from django.shortcuts import render

# Create your views here.
# chatbot/views.py

import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse

RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

@api_view(['POST'])
def chatbot_response(request):
    user_message = request.data.get('message')
    if not user_message:
        return JsonResponse({'error': 'No message provided'}, status=400)

    # Send message to Rasa
    response = requests.post(
        RASA_SERVER_URL,
        json={'sender': 'user', 'message': user_message}
    )

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Failed to connect to Rasa server'}, status=500)
