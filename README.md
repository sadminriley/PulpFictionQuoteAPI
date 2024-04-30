# Pulp Fiction Quote Generator API

I've also wrote a tutorial below for this repo.

I've included a packaged Helm(v3) chart.

# How run and deploy a Flask API to AWS EKS

https://fasterdevops.github.io/flask-docker-eks/


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
