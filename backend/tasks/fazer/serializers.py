from rest_framework import serializers
from tasks.fazer.models import Fazer

class FazerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazer
        fields = ['id', 'titulo', 'descricao']