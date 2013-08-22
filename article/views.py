# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from article.models import articles
from django.template import RequestContext

def getAllArticles():
	try:
		arts = articles.objects.all()
	except articles.DoesNotExist:
		arts = None
	return arts


def getArticleById(id_article):
	try:
		art = articles.objects.get(pk=id_article)
	except articles.DoesNotExist:
		art = None
	return art


def home(request):
	arts = getAllArticles()
	ctx ={
		"articulos" : arts
	}
	return render_to_response("index.html", ctx)


def newArticle(request):
	from article.forms import ArticleForm
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#agregado")
	else:
		form = ArticleForm()
	ctx ={
		"formulario": form
	}
	return render_to_response("form.html", ctx, context_instance=RequestContext(request))


def editArticle(request, id_article):
	art = getArticleById(id_article)
	from article.forms import ArticleForm
	if request.method == "POST":
		form = ArticleForm(request.POST, instance=art)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#editado")
	else:
		if art:
			form = ArticleForm(instance=art)
		else:
			return HttpResponseRedirect("/#no-existe-ese-articulo")
	ctx ={
		"formulario": form
	}
	return render_to_response("form.html", ctx, context_instance=RequestContext(request))


def deleteArticle(request, id_article):
	art = getArticleById(id_article)
	if art:
		art.delete()
		return HttpResponseRedirect("/#eliminado")
	return HttpResponseRedirect("/#no-hay-articulo-a-eliminar")
