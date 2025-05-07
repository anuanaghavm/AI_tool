import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class AskDoubtView(APIView):
    def post(self, request):
        question = request.data.get("question", "")
        if not question:
            return Response({"error": "Question is required"}, status=400)

        api_url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer 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",  # replace with your OpenRouter key
            "Referer": "http://localhost",
            "X-Title": "DoubtPadApp"
        }

        payload = {
            "model": "mistralai/mistral-nemo:free",
            "messages": [
                {"role": "user", "content": question}
            ]
        }

        response = requests.post(api_url, headers=headers, json=payload)

        try:
            data = response.json()
            # Remove newline characters
            answer = data["choices"][0]["message"]["content"].replace("\n", " ")
            return Response({"answer": answer})
        except (KeyError, ValueError):
            return Response({
                "error": "Invalid or empty response from OpenRouter",
                "status_code": response.status_code,
                "content": response.text,
            }, status=500)
