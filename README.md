# GAE Instant API

Easily create a RESTful interface to JSON documents hosted on Google App Engine.

> Only supports GET requests
	
## Example

![img](https://monosnap.com/file/JPyl9yisg29AsdlpeQ1QqcjTsOuqZV.png)

You could use this: 

`http://gae-instantapi.appspot.com/locations/0/city`

To retrieve this:

```
{
    "city": "San Francisco",
    "state": "CA"
}
```

### ```GET /```

```
{
    "avatar_url": "https://avatars.githubusercontent.com/u/139472?v=3",
    "blog": "http://twitter.com/tzmartin",
    "company": "Semantic Press, Inc.",
    "current_location": "Mountain View, CA",
    "description": "Designer and coder. Founder of Semantic Press.",
    "languages": [
        "English",
        "Chinese"
    ],
    "locations": [
        {
            "city": "San Francisco",
            "state": "CA"
        },
        {
            "city": "Buffalo",
            "state": "NY"
        },
        {
            "city": "Santa Monica",
            "state": "CA"
        },
        {
            "city": "Raleigh",
            "state": "NC"
        },
        {
            "city": "Dallas",
            "state": "TX"
        },
        {
            "city": "Joplin",
            "state": "MO"
        }
    ],
    "name": "TZ Martin",
    "organizations_url": "https://api.github.com/users/tzmartin/orgs"
}
```

## Todo

- Add verbs (PUT,POST,DELETE)
- Add Memcache support 
- Add Cloud Storage support
- Add Google Sheets support
- Add CSV->JSON conversion

## Contact

TZ Martin - [@tzmartin](http://twitter.com/tzmartin)

Based on [https://github.com/jbradforddillon/instant-api-py](https://github.com/jbradforddillon/instant-api-py) and [https://github.com/waldoj/instant-api](https://github.com/waldoj/instant-api).

## License

MIT License (MIT)