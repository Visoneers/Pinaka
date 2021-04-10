import django_filters
from django_filters import DateFilter 
from .models import* 

class productFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'
        exclude =['name','image','price']
        