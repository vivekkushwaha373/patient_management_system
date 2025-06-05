from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    age = models.IntegerField(verbose_name="Age")
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        verbose_name="Gender"
    )
    insurance_provider = models.CharField(
        max_length=100, 
        verbose_name="Insurance Provider"
    )
    policy_number = models.CharField(
        max_length=50, 
        verbose_name="Policy Number",
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ['full_name']
    
    def __str__(self):
        return f"{self.full_name} - {self.policy_number}"
    
    def get_gender_display_icon(self):
        """Return icon class for gender display"""
        if self.gender == 'M':
            return 'fas fa-mars text-primary'
        elif self.gender == 'F':
            return 'fas fa-venus text-danger'
        else:
            return 'fas fa-genderless text-secondary'