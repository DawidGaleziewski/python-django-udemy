# urls.py
any time user enters url i.e /admin it goes to urls.py searching for the url:

```python

urlpatterns = [
    path('admin/', admin.site.urls),
]

```

# creating home website

## adding new view
we need to create new views.py file

Inside that file we will create a function handling incoming requests

First param in the function will be the http request incoming from client
Whatever is returned in the function will be shown on the page


```python
    def home(request):
        return 'Hello'
```

We need to return http response. We import it from django library.
After that we can return a http response to the client

```python
    from django.http import HttpResponse
    def home(request):
    return HttpResponse('Hello')

```

## adding new page url
we need to import the views

```python
    from . import views

    #we can access the home function on view object imported from the file
    urlpatterns = [
        path('admin/', views.home),
    ]
```
