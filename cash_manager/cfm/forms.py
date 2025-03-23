from django import forms
from typing import Dict, Any
from .models import Transaction, Category, Subcategory, Status, TransactionType


class TransactionFilterForm(forms.Form):
    """Form to filter transactions based on date range, status, type, and categories."""
    date_from: forms.DateField = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    date_to: forms.DateField = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    status: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=Status.objects.all(), required=False)
    transaction_type: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=TransactionType.objects.all(), required=False)
    category: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False)
    subcategory: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=Subcategory.objects.all(), required=False)


class TransactionForm(forms.ModelForm):
    """Form to create or update a transaction."""

    class Meta:
        model = Transaction
        fields = ['created_at', 'status', 'transaction_type',
                  'category', 'subcategory', 'amount', 'comment']

        widgets: Dict[str, Any] = {
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-input',
                'placeholder': 'Created at',
            })
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['subcategory'].widget.attrs['disabled'] = 'disabled'
        self.fields['created_at'].widget.attrs.update(
            {'type': 'datetime-local'})

    def clean(self) -> Dict[str, Any]:
        cleaned_data: Dict[str, Any] = super().clean()
        category = cleaned_data.get('category')

        if category:
            subcategories = Subcategory.objects.filter(
                category=category).exists()
            if not subcategories:
                self.fields['subcategory'].widget.attrs['disabled'] = 'disabled'
                raise forms.ValidationError(
                    'Please select a suitable subcategory for this category.')

        return cleaned_data


class StatusForm(forms.ModelForm):
    """Form to create or update a status."""

    class Meta:
        model = Status
        fields = ['name']


class TransactionTypeForm(forms.ModelForm):
    """Form to create or update a transaction type."""

    class Meta:
        model = TransactionType
        fields = ['name']


class CategoryForm(forms.ModelForm):
    """Form to create or update a category."""

    class Meta:
        model = Category
        fields = ['name']


class SubcategoryForm(forms.ModelForm):
    """Form to create or update a subcategory."""

    class Meta:
        model = Subcategory
        fields = ['category', 'name']
