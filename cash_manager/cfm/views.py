from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

from .models import Transaction, Subcategory, Status, TransactionType, Category
from .forms import TransactionForm, StatusForm, TransactionTypeForm, CategoryForm, SubcategoryForm, TransactionFilterForm


def get_subcategories(request, category_id):
    """
    Retrieve subcategories based on the provided category ID.

    Args:
        request: The HTTP request object.
        category_id: The ID of the category to filter subcategories.

    Returns:
        JsonResponse containing the list of subcategories.
    """
    subcategories = Subcategory.objects.filter(
        category_id=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})


def transactions_home(request):
    """
    Display a list of transactions, with optional filtering.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML response with transactions and filter form.
    """
    form = TransactionFilterForm(request.GET or None)
    transactions = Transaction.objects.all()

    if form.is_valid():
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        status = form.cleaned_data.get('status')
        transaction_type = form.cleaned_data.get('transaction_type')
        category = form.cleaned_data.get('category')
        subcategory = form.cleaned_data.get('subcategory')

        if date_from and date_to:
            transactions = transactions.filter(
                created_at__range=[date_from, date_to])

        if status:
            transactions = transactions.filter(status=status)

        if transaction_type:
            transactions = transactions.filter(
                transaction_type=transaction_type)

        if category:
            transactions = transactions.filter(category=category)

        if subcategory:
            transactions = transactions.filter(subcategory=subcategory)

    return render(request, 'cfm/home.html', {'transactions': transactions, 'form': form})


def create_transaction(request, transaction_id=None):
    """
    Create a new transaction or update an existing one.

    Args:
        request: The HTTP request object.
        transaction_id: Optional ID of the transaction to update.

    Returns:
        Rendered HTML response with a form for creating or editing a transaction.
    """
    if transaction_id:
        transaction = get_object_or_404(Transaction, id=transaction_id)
        form = TransactionForm(instance=transaction)
    else:
        form = TransactionForm()

    if request.method == 'POST':
        form = TransactionForm(
            request.POST, instance=transaction if transaction_id else None)
        if form.is_valid():
            form.save()
            return redirect('transactions_home')

    return render(request, 'cfm/create.html', {'form': form})


def delete_transaction(request, transaction_id):
    """
    Delete a transaction based on the provided ID.

    Args:
        request: The HTTP request object.
        transaction_id: The ID of the transaction to delete.

    Returns:
        Redirects to the transaction overview after deletion.
    """
    if request.method == 'POST':
        transaction = get_object_or_404(Transaction, id=transaction_id)
        transaction.delete()
        messages.success(request, 'Transaction successfully deleted.')
        return redirect('transactions_home')

    messages.error(request, 'Error deleting transaction.')
    return redirect('transactions_home')


def manage_dicts(request):
    """
    Manage the lists of statuses, transaction types, categories, and subcategories.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML response with forms to manage dictionaries.
    """
    statuses = Status.objects.all()
    transaction_types = TransactionType.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    context = {
        'statuses': statuses,
        'transaction_types': transaction_types,
        'categories': categories,
        'subcategories': subcategories,
        'status_form': StatusForm(),
        'transaction_type_form': TransactionTypeForm(),
        'category_form': CategoryForm(),
        'subcategory_form': SubcategoryForm(),
    }

    return render(request, 'cfm/manage_dicts.html', context)


def add_status(request):
    """
    Add a new status to the database.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the manage dictionary page after adding the status.
    """
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dicts')
    return redirect('manage_dicts')


def add_transaction_type(request):
    """
    Add a new transaction type to the database.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the manage dictionary page after adding the transaction type.
    """
    if request.method == 'POST':
        form = TransactionTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dicts')
    return redirect('manage_dicts')


def add_category(request):
    """
    Add a new category to the database.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the manage dictionary page after adding the category.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dicts')
    return redirect('manage_dicts')


def add_subcategory(request):
    """
    Add a new subcategory to the database.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the manage dictionary page after adding the subcategory.
    """
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_dicts')
    return redirect('manage_dicts')


def delete_status(request, pk):
    """
    Delete a status based on the provided primary key.

    Args:
        request: The HTTP request object.
        pk: The primary key of the status to delete.

    Returns:
        Redirects to the manage dictionary page after deletion.
    """
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('manage_dicts')


def delete_transaction_type(request, pk):
    """
    Delete a transaction type based on the provided primary key.

    Args:
        request: The HTTP request object.
        pk: The primary key of the transaction type to delete.

    Returns:
        Redirects to the manage dictionary page after deletion.
    """
    transaction_type = get_object_or_404(TransactionType, pk=pk)
    transaction_type.delete()
    return redirect('manage_dicts')


def delete_category(request, pk):
    """
    Delete a category based on the provided primary key.

    Args:
        request: The HTTP request object.
        pk: The primary key of the category to delete.

    Returns:
        Redirects to the manage dictionary page after deletion.
    """
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('manage_dicts')


def delete_subcategory(request, pk):
    """
    Delete a subcategory based on the provided primary key.

    Args:
        request: The HTTP request object.
        pk: The primary key of the subcategory to delete.

    Returns:
        Redirects to the manage dictionary page after deletion.
    """
    subcategory = get_object_or_404(Subcategory, pk=pk)
    subcategory.delete()
    return redirect('manage_dicts')
