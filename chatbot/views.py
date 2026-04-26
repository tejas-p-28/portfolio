from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .chatbot import ask

@csrf_exempt
def chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)
    try:
        data = json.loads(request.body)
        question = data.get('question', '')
        if not question:
            return JsonResponse({'error': 'No question provided'}, status=400)
        answer = ask(question)
        return JsonResponse({'answer': answer})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
