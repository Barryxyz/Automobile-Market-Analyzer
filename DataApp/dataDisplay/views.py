from django.shortcuts import render
from dataDisplay.models import imports

# Create your views here.
#Pulls information from the data bases and opens up table.html
def table(request):
	query_results = imports.objects.all()
	return render(request, 'table.html', {'query_results': query_results})