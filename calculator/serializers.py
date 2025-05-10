# serializers.py
from rest_framework import serializers
from .models import Conversion

class ConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversion
        fields = [
            'id', 'conversion_type',
            'obtained_marks', 'total_marks',
            'value', 'percentage', 'created_at'
        ]
        read_only_fields = ['percentage', 'created_at']

    def validate(self, data):
        conversion_type = data.get('conversion_type')

        try:
            if conversion_type == 'marks_to_percentage':
                obtained = data.get('obtained_marks')
                total = data.get('total_marks')

                if obtained is None or total is None:
                    raise serializers.ValidationError("Both obtained_marks and total_marks are required.")
                if total == 0:
                    raise serializers.ValidationError("Total marks cannot be zero.")

                percentage = (obtained / total) * 100
                data['percentage'] = round(percentage, 2)

            elif conversion_type == 'cgpa_to_percentage':
                cgpa = float(data.get('value'))
                data['percentage'] = round(cgpa * 9.5, 2)

            elif conversion_type == 'letter_to_percentage':
                letter = data.get('value', '').upper()
                grade_map = {
                    'A+': 95, 'A': 90, 'B+': 85, 'B': 75, 'C+': 65,
                    'C': 55, 'D': 45, 'F': 35
                }
                if letter not in grade_map:
                    raise serializers.ValidationError("Invalid letter grade.")
                data['percentage'] = grade_map[letter]

            elif conversion_type == 'board_specific':
                value = float(data.get('value'))
                adjusted = value * 1.05 if value < 80 else value
                data['percentage'] = round(adjusted, 2)

            else:
                raise serializers.ValidationError("Invalid conversion type.")

        except (TypeError, ValueError):
            raise serializers.ValidationError("Invalid input value.")

        return data
