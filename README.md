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

Here’s the text formatted in Markdown for improved readability and quality when uploaded to GitHub:

````markdown
# Serializers and QuerySets in DRF

This concept page provides a comprehensive understanding of serializers and QuerySets in Django REST Framework (DRF). It explores how serializers work to convert complex data types, such as models and querysets, into JSON (or other formats) and vice versa. Additionally, it covers how to effectively use QuerySets in DRF views to fetch data from the database.

---

## Concept Overview

Serializers and querysets are fundamental components of DRF, playing crucial roles in data handling and API interactions. Serializers manage data conversion, validation, and representation, while querysets handle data retrieval and filtering from the database. This concept explores these components in detail, providing a comprehensive understanding of their functionality and usage.

---

## Topics

1. Serializers: Data Conversion and Validation
2. Serializer Fields and Relationships
3. QuerySets and Filtering
4. Optimizing QuerySets for Performance

---

## Learning Objectives

- Understand the role and functionality of serializers in DRF.
- Learn how to create and customize serializers for different data types and relationships.
- Utilize querysets effectively to retrieve and filter data for your API endpoints.
- Implement techniques to optimize queryset performance and efficiency.

---

## Serializers: Data Conversion and Validation

Serializers in Django REST Framework are responsible for converting complex data types, such as model instances and querysets, into Python data types that can be easily rendered into various formats (e.g., JSON, XML, YAML). This process is known as **serialization**.

Serializers also handle the **deserialization** of data, converting incoming data (e.g., from a POST or PUT request) into Python data types that can be used to create or update model instances. In addition, they also handle data validation during deserialization, ensuring data integrity.

### A Basic Serializer Example

```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at']
```
````

In this example, the `MyModelSerializer` is responsible for serializing and deserializing instances of the `MyModel` model. The `fields` attribute specifies which model fields should be included in the serialized output.

### Serializer Types

- **ModelSerializer**: Automates serializer creation based on a Django model, including field definition and basic validation.
- **HyperlinkedModelSerializer**: Extends `ModelSerializer` to include hyperlinks to related models.
- **Serializer**: Provides a base class for creating custom serializers with more control over fields and validation.

---

### Validation

DRF serializers include built-in validation mechanisms to ensure data integrity. You can define validation rules using various methods, such as field-level validation, object-level validation, and custom validation functions. You can define custom validation rules by overriding the `validate` method in your serializer.

```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at']

    def validate(self, data):
        if len(data['name']) < 5:
            raise serializers.ValidationError("Name must be at least 5 characters long.")
        return data
```

In this example, the `validate` method checks if the `name` field in the incoming data is at least 5 characters long. If the validation fails, a `ValidationError` is raised, which will be returned to the client in the response.

---

### Customizing Serializers

Serializers can be customized in various ways to meet your specific requirements. Some common customization options include:

- **Adding custom fields**: You can add custom fields to your serializer that are not directly mapped to model fields.
- **Performing validation**: Serializers can validate incoming data before creating or updating model instances.
- **Handling complex data structures**: Serializers can handle nested data structures, such as one-to-many or many-to-many relationships.
- **Overriding default behavior**: You can override the default serialization and deserialization logic to implement custom logic.

Here’s an example of a customized serializer that includes a custom field:

```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at', 'days_since_created']

    def get_days_since_created(self, obj):
        from datetime import datetime, timezone
        return (datetime.now(timezone.utc) - obj.created_at).days
```

In this example, the `days_since_created` field is a custom field that calculates the number of days since the model instance was created.

---

## QuerySets and Filtering

### Querysets

Querysets are essentially a representation of a database query. They allow you to retrieve and filter data from your models efficiently. DRF integrates seamlessly with Django’s queryset API, allowing you to leverage its powerful features.

### Filtering

You can filter querysets based on various criteria using `filter()` and `exclude()` methods, providing specific data subsets for your API endpoints.

### Pagination

DRF supports pagination to handle large datasets efficiently, providing mechanisms to limit and navigate through paginated results.

### Example

Here’s an example of a view that uses a QuerySet:

```python
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
```

In this example, the `MyModelListCreateAPIView` inherits from the `ListCreateAPIView` class provided by DRF. The `queryset` attribute is set to `MyModel.objects.all()`, which fetches all instances of the `MyModel` model. The `get_queryset()` method is overridden to add a dynamic filter based on the `name` query parameter.

---

## Optimizing QuerySets for Performance

As your data grows, optimizing queryset performance becomes crucial. Here are some techniques:

- **Select Related and Prefetch Related**: Optimize database queries by pre-fetching related data to avoid unnecessary database hits.
- **Using Values and Values List**: Retrieve only specific fields instead of the entire model instance to reduce data transfer.
- **Caching**: Cache frequently accessed queryset results to improve response times.

---

## Practice Exercise

1. Create a serializer for a model with nested relationships, using nested serializers to represent the data structure.
2. Implement filtering in a viewset to allow users to retrieve specific subsets of data based on query parameters.
3. Explore queryset optimization techniques like `select_related` and `prefetch_related` to improve the performance of your API endpoints.

---

## Additional Resources

- [DRF Serializers Documentation](https://intranet.alxswe.com/rltoken/ZvARQUUihKHt646dmrNmoA)
- [DRF Querysets Documentation](https://intranet.alxswe.com/rltoken/sxmX5Kvb3on_8htr4bMK6w)

```

```

Here’s the text formatted in Markdown for better readability on GitHub:

````markdown
# ViewSets and Routers in DRF

This concept page will provide an in-depth understanding of Django REST Framework’s (DRF) ViewSets and Routers. It explores how to use ViewSets to simplify the creation of CRUD (Create, Retrieve, Update, Delete) operations for model-based APIs, and how to leverage Routers to automatically generate URL patterns for these ViewSets.

---

## Concept Overview

ViewSets and Routers are powerful features of DRF that promote code reusability and maintainability. ViewSets encapsulate the logic for common CRUD operations (Create, Read, Update, Delete) on models, while Routers automatically generate URL patterns based on your ViewSets, reducing boilerplate code and ensuring consistent API structure.

---

## Topics

- **ViewSets**: Streamlining CRUD Operations
- **Routers**: Automatic URL Routing

---

## Learning Objectives

- Understand the concept and benefits of ViewSets in DRF.
- Learn how to create and use different types of ViewSets.
- Customize ViewSet actions to implement specific API behavior.
- Utilize Routers to automate URL routing for your API endpoints.
- Configure and use different types of Routers provided by DRF.

---

## ViewSets: Streamlining CRUD Operations

ViewSets provide a high-level abstraction for creating API views that handle common CRUD operations on models. Instead of defining separate views for each action (e.g., list, retrieve, create, update, delete), ViewSets group these actions together, reducing code duplication and promoting consistency.

Here’s an example of a basic ViewSet:

```python
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```
````

In this example, the `MyModelViewSet` inherits from the `ModelViewSet` class provided by DRF. This class automatically provides the following actions:

- **list**: Retrieve a list of model instances.
- **create**: Create a new model instance.
- **retrieve**: Retrieve a single model instance.
- **update**: Update a model instance.
- **partial_update**: Update a model instance with a partial set of fields.
- **destroy**: Delete a model instance.

You can further customize the ViewSet by overriding or adding new methods to handle specific business logic.

---

### Benefits of ViewSets

- **Code Reusability**: Reduces the amount of code needed to define API endpoints for common CRUD operations.
- **Maintainability**: Centralizes logic for related actions, making code easier to maintain and update.
- **Consistency**: Ensures a consistent structure and behavior across API endpoints.

---

### Types of ViewSets

DRF provides several types of ViewSets, each offering different levels of functionality:

- **ModelViewSet**: Provides a complete set of CRUD operations for a model, including list, retrieve, create, update, and delete actions.
- **ReadOnlyModelViewSet**: Offers read-only operations, such as list and retrieve, suitable for exposing data without allowing modifications.
- **ViewSet**: A base class that allows you to define custom actions and implement specific API behavior.

---

## Routers: Automatic URL Routing

Routers in DRF are used to automatically generate URL patterns for your API endpoints based on the ViewSets you’ve defined. This helps to reduce the amount of boilerplate code required to set up your API’s URL structure.

Here’s an example of how to use a Router:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'my-models', MyModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

In this example, we create a `DefaultRouter` instance and register the `MyModelViewSet` with it. The router automatically generates the following URL patterns:

- `GET /api/my-models/` : List all `MyModel` instances.
- `POST /api/my-models/` : Create a new `MyModel` instance.
- `GET /api/my-models/{id}/` : Retrieve a single `MyModel` instance.
- `PUT /api/my-models/{id}/` : Update a `MyModel` instance.
- `PATCH /api/my-models/{id}/` : Partially update a `MyModel` instance.
- `DELETE /api/my-models/{id}/` : Delete a `MyModel` instance.

---

### Benefits of Routers

- **Simplified URL Configuration**: Automatically generates URL patterns based on your ViewSets.
- **Consistency**: Ensures a consistent structure for API URLs.
- **Reduced Boilerplate**: Eliminates the need to write repetitive URL patterns.

---

### Router Types and Configuration

DRF offers different types of Routers to accommodate various API structures:

- **DefaultRouter**: Creates standard API root view and generates URLs for ViewSet actions.
- **SimpleRouter**: Similar to `DefaultRouter` but without the API root view, suitable for simpler APIs.
- **Custom Routers**: Allows you to define custom routing logic for more complex API structures.

---

## Combining ViewSets and Routers

By combining ViewSets and Routers, you can create a concise and maintainable API endpoint configuration. Here’s an example of how this can be done:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet, AnotherModelViewSet

router = DefaultRouter()
router.register(r'my-models', MyModelViewSet)
router.register(r'another-models', AnotherModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Add any additional non-viewset-based endpoints here
]
```

In this example, we’ve registered two ViewSets (`MyModelViewSet` and `AnotherModelViewSet`) with the Router. The Router then automatically generates the appropriate URL patterns for the CRUD operations on both models.

---

## Practice Exercise

1. Create a new ViewSet called `CommentViewSet` that provides CRUD operations for a `Comment` model.
2. Integrate the `CommentViewSet` with the existing Router, and verify that the correct URL patterns are generated.
3. Customize the `CommentViewSet` to add a custom action that allows users to mark a comment as “flagged” for moderation.

---

## Additional Resources

- [DRF ViewSets Documentation](https://intranet.alxswe.com/rltoken/iir4BjBfAxNQKjNZf0CDRw)
- [DRF Routers Documentation](https://intranet.alxswe.com/rltoken/MFBg2HK8KUir_n-MTX2wKg)

```

```

````markdown
# Authentication and Permissions in DRF

This concept page will provide an in-depth understanding of **authentication** and **permissions** in Django REST Framework (DRF). It will explore different authentication schemes, such as **token-based**, **session-based**, and **OAuth**, and learn how to implement them in their DRF-powered APIs.

## Concept Overview

**Authentication** and **permissions** are critical aspects of API security, ensuring that only authorized users can access and interact with your API resources. DRF provides a robust framework for implementing various authentication schemes and permission policies, allowing you to tailor access control to your specific needs. This concept explores different authentication methods and permission strategies available in DRF, empowering you to build secure and reliable APIs.

## Topics

- **Authentication in DRF**
- **Permission Policies in DRF**
- **Securing API Endpoints with Authentication and Permissions**
- **A Complete Example**

## Learning Objectives

- Understand the role and importance of **authentication** and **permissions** in API security.
- Learn how to implement various authentication methods, including **TokenAuthentication**, **SessionAuthentication**, and **JWT Authentication**.
- Explore different permission policies offered by DRF, such as **IsAuthenticated**, **IsAdminUser**, and **DjangoModelPermissions**.
- Create custom permission classes to implement granular access control based on specific requirements.

## Authentication in Django REST Framework

**Authentication** verifies the identity of a user or client attempting to access your API. DRF supports several authentication methods out-of-the-box and allows for custom implementations.

DRF provides several authentication schemes to secure your API endpoints, including:

- **Token Authentication**: Clients authenticate by providing a unique token in the request headers.
- **Session Authentication**: Clients authenticate using Django’s built-in session-based authentication.
- **OAuth Authentication**: Clients authenticate using the OAuth 2.0 protocol, which allows third-party applications to access user data without requiring their credentials.

You can configure authentication globally in your `settings.py` or at the view or viewset level using the `authentication_classes` attribute.

Here’s an example of how to implement token-based authentication in DRF:

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can access this view
        return Response({'message': 'Hello, authenticated user!'})
```
````

In this example, the `MyAPIView` class requires **token-based authentication** and the **IsAuthenticated** permission to access the `get` method.

## Permission Policies in DRF

DRF provides a wide range of built-in permission classes to control access to your API endpoints, such as:

- **AllowAny**: Allows access to anyone, regardless of authentication status.
- **IsAuthenticated**: Allows access only to authenticated users.
- **IsAdminUser**: Allows access only to users with the `is_staff` flag set to `True`.
- **IsOwner**: Allows access only to the owner of the resource.

You can also create custom permission classes to implement more complex access control logic. Here’s an example of a custom permission class:

```python
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff
```

In this example, the `IsAdminOrReadOnly` permission class allows **read-only access** to everyone, but requires the user to be an **admin (staff user)** for any write operations.

## Securing API Endpoints with Authentication and Permissions

By combining **authentication** and **permissions**, you can secure your API endpoints and control access based on user roles and permissions. Here’s an example of how to do this:

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

class MyModelListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can view the list of models
        queryset = MyModel.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

class MyModelCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        # Only admin users can create new model instances
        serializer = MyModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

In this example, the `MyModelListView` requires **token-based authentication** and the **IsAuthenticated** permission, which means only authenticated users can view the list of models. The `MyModelCreateView`, on the other hand, requires **token-based authentication** and the **IsAdminUser** permission, which means only admin users can create new model instances.

## A Complete Example

The following example demonstrates the use of **authentication** and **permissions** in a Django REST Framework (DRF) application that provides a simple blog post API. The API allows users to list, create, retrieve, update, and delete blog posts. However, it enforces certain access control rules to ensure that only authenticated users can perform these operations, and that users can only modify posts they have created.

The key components of this example include:

- A `Post` model to represent blog posts.
- A `PostSerializer` to handle the serialization and deserialization of `Post` instances.
- A custom `IsAuthorOrReadOnly` permission class to control access to `Post` instances.
- Two DRF views (`PostListCreateAPIView` and `PostRetrieveUpdateDestroyAPIView`) that leverage the authentication and permission classes to secure the API endpoints.

### models.py

```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

### serializers.py

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
```

### permissions.py

```python
from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user
```

### views.py

```python
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### urls.py

```python
from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
]
```

In this example, we have a `Post` model that represents a blog post, with a `title`, `content`, `author`, and `created_at` fields.

- The `PostSerializer` is responsible for serializing and deserializing the `Post` model instances.
- The `IsAuthorOrReadOnly` permission class is a custom permission that allows **read-only access** to anyone, but only allows the author of the post to perform CRUD operations on it.
- The `PostListCreateAPIView` handles the list and create operations for the `Post` model. It requires **token-based authentication** (`TokenAuthentication`) and the **IsAuthenticated** and **IsAuthorOrReadOnly** permissions. When creating a new post, the `perform_create` method is overridden to associate the current user as the author of the post.
- The `PostRetrieveUpdateDestroyAPIView` handles the retrieve, update, and destroy operations for individual `Post` instances. It also requires **token-based authentication** and the **IsAuthenticated** and **IsAuthorOrReadOnly** permissions.
- In the `urls.py` file, we define the URL patterns for the two views, allowing clients to access the post list and individual post details.

With this setup, only **authenticated users** can access the API, and the `IsAuthorOrReadOnly` permission ensures that users can only perform CRUD operations on posts they have authored. This provides a basic level of security and access control for the API.

## Practice Exercise

1. Implement **TokenAuthentication** in your DRF project and create API endpoints for obtaining and refreshing tokens.
2. Set up **DjangoModelPermissions** for a viewset to restrict access based on Django’s model permissions.
3. Create a custom permission class that checks if a user has a specific attribute before allowing access to a view.

## Additional Resources

- [DRF Authentication Documentation](https://intranet.alxswe.com/rltoken/v1zijFalcGGmlXiIwZd4Dg)
- [DRF Permissions Documentation](https://intranet.alxswe.com/rltoken/7ullC2koHvyTI96WF34T_Q)
- [Tutorial 4: Authentication & Permissions](https://intranet.alxswe.com/rltoken/VQCnsvuId-zbC9Bq0fUnHg)

```

```
