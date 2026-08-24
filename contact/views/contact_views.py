from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }

    return render(request, 'contact/index.html', context=context)


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': single_contact,
        'site_title': f'{single_contact.first_name} {single_contact.last_name} - ',
    }

    return render(request, 'contact/contact.html', context)


def search(request: HttpRequest):
    search_value = request.GET.get('q', '').strip()

    contacts = Contact.objects.filter(show=True)

    if search_value:
        search_terms = search_value.split()
        query = Q()

        for term in search_terms:
            query |= Q(first_name__icontains=term)
            query |= Q(last_name__icontains=term)
            query |= Q(phone__icontains=term)
            query |= Q(email__icontains=term)

        contacts = contacts.filter(query)

    contacts = contacts.order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Busca - ',
        'search_value': search_value,
    }

    return render(request, 'contact/index.html', context)
