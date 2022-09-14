from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_xml, show_wishlist_json, find_by_id_json

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('json/<int:id>', find_by_id_json, name='find_by_id_json')
]