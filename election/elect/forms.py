from django import forms
from .models import Election


class ElectionForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = "__all__"

        widgets = {
            "candidate_name": forms.TextInput(attrs={'class': 'form-control'}),
            "constituency": forms.TextInput(attrs={'class': 'form-control'}),
            "total_voters": forms.NumberInput(attrs={'class': 'form-control'}),
            "secured_votes ": forms.NumberInput(attrs={'class': 'form-control'}),
            "choice": forms.Select(attrs={'class': 'form-control'}),
        }
