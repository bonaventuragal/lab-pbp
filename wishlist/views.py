from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(req):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Bona'
    }
    return render(req, "wishlist.html", context)

def show_wishlist_xml(req):
    data_barang_wishlist = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_barang_wishlist), content_type="application/xml")

def show_wishlist_json(req):
    data_barang_wishlist = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_barang_wishlist), content_type="application/json")

def find_by_id_json(req, id):
    data = BarangWishlist.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")