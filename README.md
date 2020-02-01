# Pulp Fiction Quote Generator API


## Building the application
```
docker build -t pulpapi:latest .
```

## Running the application
```
docker run -t -p 5000:5000 pulpapi
```

## Usage

### Characters [GET]

request
```
curl -X GET http://localhost:5000/characters
```

result
```
{
  "Available Characters": [
    {
      "name": "jules"
    },
    {
      "name": "vincent"
    },
    {
      "name": "mia"
    }
  ]
}
```

### Quote [GET]

request
```
curl -X GET http://localhost:5000/quote/mia
```

result
```
{
  "mia says...": [
    {
      "quote": "When in conversation, do you listen, or do you just wait to talk?"
    }
  ]
}
```


### Quote [POST]

request
```
curl -X POST http://localhost:5000/quote/vincent -d 'quote=hi mark'
```
result
```
{
  "status": "success"
}
```
