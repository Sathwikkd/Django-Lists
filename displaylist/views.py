from django.shortcuts import render
from django.http import HttpResponse
def lists_view(request):
    fruits = ['Sebu', 'Karjuura', 'halasinahannu','baleHannu']
    Members = ['Savithri Bhai', 'Dini', 'Shubh', 'Sathu','Ruth', 'Mr.handa', 'Mr.Chotuu']
    context = {
        'fruits': fruits,

        'students': Members,
    }
    return render(request, 'list.html', context)