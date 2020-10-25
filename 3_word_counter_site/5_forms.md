# redirect form to another page

we can use standard way of adding action attribute to form to redirect the form to another page.
However django allows us to use a label on the url that we can re-use so that we do not have to worry about it changing  in the future


## accessing the url from django/python code:
in urls.py:

```python   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ),
    # name will give us a label to access current url
    path('count/', views.count, name='count')
]
```

```html
    <h1>WORD COUNT {{ greet }}</h1>
    <!-- We can use that label inside the action attribute -->
    <form action="{% url 'count' %}">
      <textarea name="fulltext" id="" cols="30" rows="10"></textarea> <br />
      <input type="submit" value="send" />
    </form>
```