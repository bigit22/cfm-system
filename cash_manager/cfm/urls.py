from django.urls import path

from .views import (
    get_subcategories,
    create_transaction,
    transactions_home,
    manage_dicts,
    add_status,
    add_transaction_type,
    add_category,
    add_subcategory,
    delete_status,
    delete_transaction_type,
    delete_category,
    delete_subcategory,
    delete_transaction,
)


urlpatterns = [
    path('', transactions_home, name='transactions_home'),

    path('create-edit', create_transaction, name='create'),
    path('create-edit/<int:transaction_id>/',
         create_transaction, name='create_edit_transaction'),
    path('get_subcategories/<int:category_id>/',
         get_subcategories, name='get_subcategories'),
    path('delete/<int:transaction_id>/',
         delete_transaction, name='delete_transaction'),

    path('manage-dicts/', manage_dicts, name='manage_dicts'),
    path('add-status/', add_status, name='add_status'),
    path('add-transaction-type/', add_transaction_type,
         name='add_transaction_type'),
    path('add-category/', add_category, name='add_category'),
    path('add-subcategory/', add_subcategory, name='add_subcategory'),
    path('delete-status/<int:pk>/', delete_status, name='delete_status'),
    path('delete-transaction-type/<int:pk>/',
         delete_transaction_type, name='delete_transaction_type'),
    path('delete-category/<int:pk>/', delete_category, name='delete_category'),
    path('delete-subcategory/<int:pk>/',
         delete_subcategory, name='delete_subcategory'),
]
