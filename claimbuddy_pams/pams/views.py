
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from .models import Patient

def dashboard(request):
    """Dashboard view with summary statistics"""
    total_patients = Patient.objects.count()
    male_count = Patient.objects.filter(gender='M').count()
    female_count = Patient.objects.filter(gender='F').count()
    other_count = Patient.objects.filter(gender='O').count()
    
    # Insurance provider statistics
    insurance_stats = {}
    for patient in Patient.objects.all():
        provider = patient.insurance_provider
        insurance_stats[provider] = insurance_stats.get(provider, 0) + 1
    
    # Sort insurance stats by count (descending)
    insurance_stats = dict(sorted(insurance_stats.items(), key=lambda x: x[1], reverse=True))
    
    context = {
        'total_patients': total_patients,
        'male_count': male_count,
        'female_count': female_count,
        'other_count': other_count,
        'insurance_stats': insurance_stats,
    }
    
    return render(request, 'pams/dashboard.html', context)

def patient_list(request):
    """View to display list of all patients with search and pagination"""
    # patients = Patient.objects.all()
    patients = Patient.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        patients = patients.filter(
            Q(full_name__icontains=search_query) |
            Q(policy_number__icontains=search_query) |
            Q(insurance_provider__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(patients, 10)  # Show 10 patients per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_patients': Patient.objects.count(),
    }
    
    return render(request, 'pams/patient_list.html', context)

def patient_detail(request, patient_id):
    """View to display individual patient details"""
    patient = get_object_or_404(Patient, id=patient_id)
    
    context = {
        'patient': patient,
    }
    
    return render(request, 'pams/patient_detail.html', context)