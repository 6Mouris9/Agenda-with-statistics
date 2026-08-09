from django import http
from django.db.models import Q
from django.http import Http404, HttpRequest, request
from django.shortcuts import render, get_object_or_404
from contact.models import Contact
# Create your views here.

def index(request):
    contacts = Contact.objects\
    .filter(show=True)\
    .order_by('-id')[:10]

    context = {
        "contacts": contacts,
    }

    return render(
        request,
        'contact/index.html',
        context=context
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': single_contact,
    }
    return render(
        request,
        'contact/contact.html',
        context,
        )

def search(request: HttpRequest):
    search_value = request.GET.get('q','').strip()

    contacts = Contact.objects\
            .filter(show=True)\
            .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value)  |
                Q(phone__icontains=search_value)  |
                Q(email__icontains=search_value)
            )\
            .order_by('-id')[10:20] 


    context = {
        "contacts": contacts,
        'site_title': 'Contatos - ',
        "search_value": search_value,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )