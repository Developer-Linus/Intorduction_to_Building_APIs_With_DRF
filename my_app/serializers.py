from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    def get_days_since_created(self, obj):
        from datetime import datetime, timezone
        return(datetime.now(timezone.utc)-obj.created_at).days
    
