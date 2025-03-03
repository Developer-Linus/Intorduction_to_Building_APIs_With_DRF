# Intorduction_to_Building_APIs_With_DRF

Here’s the text formatted in Markdown for improved readability on GitHub:

````markdown
# Getting Started with Django REST Framework

This concept page provides an overview of Django REST Framework (DRF), its key architecture components, and the steps to set up a basic Django project with DRF. By the end of this topic, learners will be able to understand the purpose and features of DRF, familiarize themselves with its core components, and set up a new Django project integrated with DRF.

## Concept Overview

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs. It extends Django’s capabilities to facilitate the development of RESTful APIs, providing features like serialization, authentication, permissions, and more. This concept introduces you to the fundamental aspects of DRF and guides you through setting up a basic API endpoint.

---

## Topics

1. Introduction to Django REST Framework
2. DRF Architecture: Serializers, ViewSets, Routers
3. Creating Your First API Endpoint

---

## Learning Objectives

- Understand the purpose and features of the Django REST Framework.
- Familiarize with the key components of DRF architecture.
- Learn how to create a basic API endpoint using DRF.

---

## Introduction to Django REST Framework

DRF provides a structured and efficient way to build APIs with Django. It simplifies common tasks like data serialization, validation, authentication, and permission handling. This allows you to focus on the logic of your API without worrying about the underlying details.

### Benefits of DRF:

- **Serialization**: DRF simplifies the process of converting complex data structures, such as Django models, into formats like JSON or XML, making it suitable for consumption by various clients.
- **ViewSets and Routers**: DRF offers viewsets and routers that streamline the process of creating API endpoints, reducing boilerplate code and promoting consistency.
- **Authentication and Permissions**: DRF provides built-in support for various authentication methods and permission policies, ensuring secure access to your API.
- **Browsable API**: DRF includes a browsable API interface that allows developers to easily interact with and test API endpoints directly from a web browser.

---

## Creating Your First API Endpoint

To get started with Django REST Framework, follow these steps:

1. **Create a new Django project and app:**

   ```bash
   django-admin startproject my_project
   cd my_project
   python manage.py startapp my_app
   ```
````

2. **Install the Django REST Framework package:**

   ```bash
   pip install djangorestframework
   ```

3. **Add `'rest_framework'` to your `INSTALLED_APPS` in the `settings.py` file:**

   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
   ]
   ```

4. **Define your first model in the `models.py` file of your app:**

   ```python
   from django.db import models

   class Book(models.Model):
       title = models.CharField(max_length=200)
       author = models.CharField(max_length=100)
       published_date = models.DateField()
   ```

5. **Create a serializer for your model in the `serializers.py` file:**

   ```python
   from rest_framework import serializers
   from .models import Book

   class BookSerializer(serializers.ModelSerializer):
       class Meta:
           model = Book
           fields = '__all__'
   ```

6. **Define a view for your model in the `views.py` file:**

   ```python
   from rest_framework import generics
   from .models import Book
   from .serializers import BookSerializer

   class BookListCreateAPIView(generics.ListCreateAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
   ```

7. **Add a URL pattern for your view in the `urls.py` file:**

   ```python
   from django.urls import path
   from .views import BookListCreateAPIView

   urlpatterns = [
       path("api/books", BookListCreateAPIView.as_view(), name="book_list_create"),
   ]
   ```

8. **Start the development server and access your API endpoint at `http://localhost:8000/api/books/`:**

   ```bash
   python manage.py runserver
   ```

Now you have a basic API endpoint that allows you to perform CRUD operations on your model.

---

## Practice Exercise

1. Extend the `BookSerializer` to include a custom field that displays the number of days since the model instance was created.
2. Install Django REST Framework and set up a basic API endpoint for a model in your existing Django project.
3. Use the browsable API interface to explore the available actions and test your API endpoints.
4. Experiment with different serializer fields and viewset actions.

---

## Additional Resources

- [Django REST Framework Documentation](https://intranet.alxswe.com/rltoken/QA9zgJr1kahEjildq8YOiw)
- [DRF Tutorial](https://intranet.alxswe.com/rltoken/ohhPKKgWOafYixV_x6gghQ)
- [Creating REST APIs using Django REST Framework](https://intranet.alxswe.com/rltoken/AcSbhHj7pl1Uexgh1u8i0w)
- [Authentication Introduced](https://intranet.alxswe.com/rltoken/p_nXakd30bql8jgJOM2Z6g)
- [Token-based Authentication: Django](https://intranet.alxswe.com/rltoken/n0C9vuJhWWV7kgWUIV-ZfA)
- [Session-based Authentication](https://intranet.alxswe.com/rltoken/xKiEABnsTlsXJN_9wq_M4A)
- [Video: Django Authentication Explained](https://intranet.alxswe.com/rltoken/qgNN7_ln1Pl4Dv1dFN6erA)

```

```
