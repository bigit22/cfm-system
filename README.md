# CFM System

## Overview

The CFM System is a Django-based web application designed to streamline financial transaction management for users. It provides a user-friendly interface for creating, viewing, and managing financial transactions, enabling users to filter transactions by various criteria such as date range, status, transaction type, category, and subcategory. The application also includes functionalities for managing dictionaries of statuses, transaction types, categories, and subcategories, allowing users to customize their financial categorization effectively.

With the CFM System, users can easily add or delete entries related to statuses, transaction types, categories, and subcategories, ensuring that their financial records remain organized and up-to-date. Additionally, the application supports transaction creation and editing, making it simple to document financial activities accurately. Overall, the CFM System aims to enhance financial tracking and reporting, catering to individuals and businesses seeking better control over their financial data.

## Prerequisites

Before you begin, make sure you have the following installed:

- [Git](https://git-scm.com/) (for cloning the repository)
- [Python 3.x](https://www.python.org/downloads/) (preferably Python 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (optional but recommended for virtual environments)

## Installation

Follow these steps to set up your project locally.

## 1. Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
    git clone https://github.com/bigit22/cfm-system.git
```
Move into the project directory:

```bash
    cd cfm-system
```

## 2. Set Up a Virtual Environment

Create a virtual environment
```bash
    python3 -m venv venv
```

Activate the virtual environment

```bash
    source venv/bin/activate
```

Install Dependencies

```bash
    pip install -r requirements.txt
```

## 3. Set Up the Database

```bash
    python3 cash_manager/manage.py makemigrations
```

```bash
    python3 cash_manager/manage.py migrate
```

## 4. Create Superuser (optional)

```bash
    python3 cash_manager/manage.py createsuperuser
```

## 5. Run the server

```bash
    python3 cash_manager/manage.py runserver
```

## Get http://127.0.0.1:8000/transactions
