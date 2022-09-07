from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(req):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Bona'
    }
    return render(req, "wishlist.html", context)