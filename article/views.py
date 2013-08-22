# Create your views here.
from django.shortcuts import render_to_response

def getAllArticles():
	from article.models import articles
	try:
		arts = articles.objects.all()
	except articles.DoesNotExist:
		arts = None
	return arts


def home(request):
	arts = getAllArticles()
	ctx ={
		"articulos" : arts
	}
	return render_to_response("index.html", ctx)