import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import re

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
            raw_answer = data["choices"][0]["message"]["content"]

            # Clean up the raw answer
            cleaned_text = re.sub(r'[\n*]+', ' ', raw_answer)  # Remove newline and asterisk
            cleaned_text = re.sub(r'[-]+', ' ', cleaned_text)   # Remove dashes

            # Use regex to capture points with numbers or dashes as bullet points
            points = re.findall(r'\d+\.\s*([^\d].*?)(?=\d+\.|\Z)', cleaned_text)

            # Reformat points with correct numbering and no extra symbols
            formatted_points = [f"{i+1}. {point.strip()}" for i, point in enumerate(points)]
            
            # Return the points as a list
            return Response({"answer": formatted_points})

        except (KeyError, ValueError):
            return Response({
                "error": "Invalid or empty response from OpenRouter",
                "status_code": response.status_code,
                "content": response.text,
            }, status=500)
