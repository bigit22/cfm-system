# CFM System

## Overview

The CFM System is a Django-based web application designed to... [provide a brief description of what your project does].

## Prerequisites

Before you begin, make sure you have the following installed:

- [Git](https://git-scm.com/) (for cloning the repository)
- [Python 3.x](https://www.python.org/downloads/) (preferably Python 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (optional but recommended for virtual environments)

## Getting Started

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
    python3 manage.py makemigrations
```

```bash
    python3 manage.py migrate
```

## 4. Create Superuser

```bash
    python3 manage.py createsuperuser
```

## 5. Run the server

```bash
    python3 manage.py runserver
```
