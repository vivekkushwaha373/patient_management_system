from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    full_name = models.CharField(
        max_length=200, 
        verbose_name="Full Name",
        help_text="Enter the patient's full name"
    )
    age = models.IntegerField(
        verbose_name="Age",
        validators=[MinValueValidator(0), MaxValueValidator(150)],
        help_text="Enter age in years"
    )
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        verbose_name="Gender"
    )
    insurance_provider = models.CharField(
        max_length=100, 
        verbose_name="Insurance Provider",
        help_text="Name of the insurance company"
    )
    policy_number = models.CharField(
        max_length=50, 
        verbose_name="Policy Number",
        unique=True,
        help_text="Unique policy identification number"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ['full_name']
        indexes = [
            models.Index(fields=['full_name']),
            models.Index(fields=['policy_number']),
            models.Index(fields=['insurance_provider']),
        ]
    
    def __str__(self):
        return f"{self.full_name}"
    