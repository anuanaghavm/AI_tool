import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings  # Add OPENROUTER_API_KEY to settings

class AskDoubtView(APIView):
    def post(self, request):
        question = request.data.get("question", "")
        if not question:
            return Response({"error": "Question is required"}, status=400)

        headers = {
            "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant in a doubt pad app."},
                {"role": "user", "content": question}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

        try:
            data = response.json()
            answer = data['choices'][0]['message']['content']
            return Response({"answer": answer})
        except (ValueError, KeyError, IndexError):
            return Response({
                "error": "Invalid or empty response from OpenRouter",
                "status_code": response.status_code,
                "content": response.text,
            }, status=500)
