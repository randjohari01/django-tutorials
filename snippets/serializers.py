from rest_framework import serializers
from .models import LANGUAGE_CHOICE , STYLE_CHOICE, Snippets

"""
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = False, allow_blank = True , max_length =100 )
    code =  serializers.CharField(style = {"bas_template" : "textarea.html"})
    lineons = serializers.BooleanField(required = False)
    language = serializers.ChoiceField(choices = LANGUAGE_CHOICE , default = "python")
    style = serializers.ChoiceField(choices = STYLE_CHOICE , default = "friendly")

    def create(self , validation_data):
        return snippets.objects.create(**validation_data)
    
    def update(self,  instance ,  validation_data):
        instance.title = validation_data.get("title", instance.title)
        instance.code = validation_data.get("code", instance.code)
        instance.lineons = validation_data.get("lineons", instance.lineons)
        instance.language = validation_data.get("language", instance.language)
        instance.style = validation_data.get("style", instance.style)
        instance.save()
        return instance
"""

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets 
        fields = ["id", "title", "code", "linenos", "language", "style"]
