from django.conf.urls import patterns  # , url

articles_urls = patterns('article',
    (r'^$', 'views.home'),
    (r'^new', 'views.newArticle'),
    (r'^edit/(?P<id_article>.*)', 'views.editArticle'),
    (r'^delete/(?P<id_article>.*)', 'views.deleteArticle'),
)
