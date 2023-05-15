from django.shortcuts import render, HttpResponse
from .models import Book, booktype
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')

def add_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        publisher_name = request.POST['publisher_name']
        type_id = request.POST['type_id']
        new_book= Book( book_name=book_name, publisher_name= publisher_name, book_type = type_id)
        new_book.save()
        return HttpResponse("book saved")
    elif request.method=='GET':
        return render(request, 'add_book.html')
    else:   
        return HttpResponse("Failed")

def search_book(request):
    if request.method == 'POST':
        key = request.POST['key']
        type_id = request.POST['type_id']
       
        books = Book.objects.all()

        book = books.filter( (Q(book_name__icontains=key) | Q(publisher_name__icontains=key)))       
    
        context = {
            'books': book
        }

        return render(request,'view_books.html',context)
       
    elif request.method=='GET':
        return render(request,'search_book.html')
    else:   
        return HttpResponse("Failed")
    

