This is a SDK for the Lord of the Rings API at https://the-one-api.dev

# Installation & Setup
You can install this package using pip 
```
pip install plotrsdk
```

## Account Creation
Signup at https://the-one-api.dev/sign-up and copy your Access token

## Setup Environment Variable
Since, most of the APIs are protected using a access token, you will have to set an enviornment variable before using the SDK

```
export LOTR_TOKEN=xxxxxxxxx
```

# Usage

## How to use Pagination
list function has a default limit of 10. If you want a bigger limit, you can do the following
```python
.limit({"limit": 1000})
```

by default, the offset is set to 0. If you want to start from a custom offset, you can do the following
```python
.limit({"limit": 1000, "offset": 493})
.limit({"offset": 493}) ## in this case, limit is defaulted to 10
```

## How to use Sorting
You can use the sorting function along with the limit function
```python
.limit({}, {"name": "desc"}) # to do sorting by asc order
.limit({}, {"_id": "asc"}) # to do sorting by desc order
```

## How to use Filtering
You can use filtering of data like this
```python
.limit({}, {}, {"name": "Gandalf"}) # to do equal matching
.limit({}, {"_id": "asc"}, {"name!": "Gandalf"}) # to do not equal matching
.limit({}, {}, {"race": "Hobbit,Human"}) # to do include
.limit({"limit": 500}, {"_id": "asc"}, {"race!": "Orc,Goblin"}) # to do exclude
.limit({}, {}, {"race!": "/regex/"}) # to do regex matching
.limit({}, {}, {"name": "/King/"}) # to do regex matching
```

## Pagination Response
All of the resources which are an array/list are always returned as a Pagination Response object. It contains the following properties
- items
- limit
- offset
- page
- pages
- total

This helps more granular access to filtering

## Types of Objects

### Data Type
- Book (This is the actual data type)
- Chapter (This is the actual data type)
- Character (This is the actual data type)
- Movie (This is the actual data type)
- Quote (This is the actual data type)

### Resource
- Books (This contains all the functions, and always returns an array of Book or single Book)
- Chapters (This contains all the functions, and always returns an array of Chapter or single Chapter)
- Characters (This contains all the functions, and always returns an array of Character or single Character)
- Movies (This contains all the functions, and always returns an array of Movie or single Movie)
- Quotes (This contains all the functions, and always returns an array of Quote or single Quote)

## Example

The below example is for the books resource, but the flow is the same for every other resource as well.

To list the books 
```python
from plotrsdk.books import Books
b = Books()
bl = b.list()
for item in bl.items:
  print(x)
```

To list the next set of books (you must have called list() function like in the earlier snippet before you can do next_page)
```python
...
bl.next_page()
```

To query for a specific page (you must have called list() function like in the earlier snippet before you can do next_page)
```python
...
bl.get_page()
```

To get a book by it's id
```python
from plotrsdk.books import Books
b = Books()
b.get_book(<id>)
```


# TODO
- There is some code that is repeated (like each of the resource, have majority of the function same except the part where they have to convert JSON data into objects). Can create a super class and just the differeing functions can change
- Incase of failures, we would want to do a retry requests with backoff
- Pagination Resource should also be able to get the next page or a specific page