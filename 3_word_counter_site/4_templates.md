# adding templates
Best to create templates folder in root of the project

## tell django where to search for templates
this can be setup in setting.py TEMPLATES list

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

## send templates
in views.py import django render method

We return the render method with two params: request and the .html file

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

## passing data to the template

3rd param in render is the dictionary with values we want to send

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {"test":"test"})
```
we can interpolate python code inside the template:

```html

<h1>WORD COUNT {{ greet }}</h1>

```
