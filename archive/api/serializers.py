from rest_framework import serializers
from record.models import Record


class RecordSerializer(serializers.ModelSerializer):
    """
    Serializer to parse Record data
    """

    class Meta:
        model = Record
        fields = ('id','date','honest_url','honest_item', 'honest_price', 'carre_item', 'carre_price')
