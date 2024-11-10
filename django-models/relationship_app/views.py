from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Library

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        # Ensure that we're fetching libraries from the database
        return Library.objects.all()
