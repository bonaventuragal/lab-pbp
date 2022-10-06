from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', wishlist_ajax, name='wishlist_ajax'),
    path('ajax/submit/', add_wishlist, name='add_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('json/<int:id>', find_by_id_json, name='find_by_id_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]