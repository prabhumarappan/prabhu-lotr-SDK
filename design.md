## Design

I intially looked at all of the API calls, and this is what I came up with:
- Each resource will have a data type
- Each resource will have a couple of methods you can interact with to get results
- URL params will be prepared at the respective resource layer, and then sent along with the resource URL
- Each resource will also have an attribute which states weather access token is required to access it
- And in the resource layer, each of the response will be converted to specific data type

![Design](/images/lotr%20sdk.png?raw=true "Design")


### Book (data type)
```
- _id
- name
- list_chapters (function)
```

### Books (resource)
```
-  list
-  next_page
-  get_page
-  get_book
```

### Chapter (data type)
```
- _id
- chapter_name
```
### Chapters (resource)
```
- list
- next_page
- get_page
- get_chapter
```

### Character (data type)
```
- _id
- height,
- race
- gender
- birth
- spouse
- death
- realm
- hair
- name
- wiki_url
- list_quotes (function)
```

### Characters (resource)
```
- list
- next_page
- get_page
- get_character
```

### Movie (data type)
```
- _id
- name
- runtime
- budget
- box_office
- academy_nominations
- academy_wins
- rotten_tomatoes_score
- list_quotes (function)
```

### Movies (resource)
```
- list
- next_page
- get_page
- get_movie
```

### Quote (data type)
```
- _id
- dialog
- movie
- character
```

### Quotes (resource)
```
- list
- next_page
- get_page
- get_quote
```