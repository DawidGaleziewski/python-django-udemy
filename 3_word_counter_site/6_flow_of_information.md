# in this project we will be using query params i.e:

http://localhost:8000/count/?fulltext=This+is+a+form+text+here+%21

We can get into query params on the request param in our count function

```python
def count(request):
    fulltext = request.GET["fulltext"]
    print(fulltext)
    return render(request, 'count.html')
```

Now we can pass it to our template

```python

def count(request):
    fulltext = request.GET["fulltext"]
    return render(request, 'count.html', {'fulltext' : fulltext})

```

Now we can access this dictionary from our html template:

```html

<p>Length of the text is: {{ fulltext }}</p>

```

We can caclculate the wordlist length by spliting the words and using len() method on it:

```python
    wordlist = fulltext.split()
    len(wordlist)
```

# python methods

## check if the word is present in a dictionary
```python
        if word in worddictionary:
            worddictionary[word] += 1
```

## change dictionary into a list:
word_dictionary_list = worddictionary.items()


# interpolate for loop in html template

```html

    {% for word, counttotal in worddictionary %}
     {{ word }} <br />
        {{counttotal}}
    {% endfor %}

```