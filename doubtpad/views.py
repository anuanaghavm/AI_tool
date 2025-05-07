import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import re

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
        "model": "deepseek/deepseek-r1:free",
        "prompt": f"Answer the following question briefly and factually.\nQ: {question}\nA:",
        "max_tokens": 150,
        "temperature": 0.5
    }

        try:
            response = requests.post("https://openrouter.ai/api/v1/completions", headers=headers, json=payload)

            if response.status_code == 200:
                data = response.json()
                answer = data.get('choices', [{}])[0].get('text', 'No answer available')

                # Clean the answer to remove unrelated content
                # Use a regex to extract the first complete sentence or paragraph
                cleaned_answer = re.split(r'Q:|A:', answer)[0]  # Stop at any new question or answer marker
                cleaned_answer = " ".join(cleaned_answer.split())  # Remove extra spaces

                return Response({"answer": cleaned_answer})
            else:
                return Response({
                    "error": "Failed to get a response from OpenRouter",
                    "status_code": response.status_code,
                    "content": response.text,
                }, status=response.status_code)

        except requests.RequestException as e:
            return Response({"error": str(e)}, status=500)
