from django.conf.urls import url
from . import views      

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_user$', views.add_user),
    url(r'^login$', views.login),
    url(r'^travels$', views.travels_dashboard),
    url(r'^travels/(?P<id>\d+)$', views.display_destination_dashboard),
    url(r'^travels/add$', views.travels_add_dashboard),
    url(r'^add_trip$', views.add_trip),
    url(r'^logout$', views.logout)
	
	]








	# url(r'^$', views.index),     # This line has changed!
 #    url(r'^add_user$', views.add_user), 
 #    url(r'^books$', views.books_dashboard), 
 #    url(r'^delete/(?P<id>\d+)$', views.delete_review), 
 #    url(r'^books/add$', views.books_add_dashboard), 
 #    url(r'^books/(?P<id>\d+)$', views.display_book_reviews), 
 #    url(r'^login$', views.login), 
 #    url(r'^logout$', views.logout),
 #    url(r'^books/add_process$', views.process_all_info), 
 #    url(r'^users/(?P<id>\d+)$', views.display_user), 