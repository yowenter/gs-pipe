# GS-Pipe

REST API Power Your Google Spreadsheet.


The everything of the internet is all about data communication, with the help of pipeline and free public storage service like Google spreadsheet or Airtable, You'll build your own powerful service.


Here, I'm to extend the google spreadsheet ability to interact with  other website service :-)



## Usage 


### Create Task

#### HTTP API

`POST http://localhost:5000/task`

#### PARAMS

| Field | Type | Required | Description |
| --- | --- | --- | --- |
|input_argument |Array |True |Pipeline input argument|
|pipeline |Array |True |Pipeline functions |


> Example

```python
import requests

response = requests.post(
    'http://localhost:5000/task',
    json={
        "input_argument":[10, 3],
        "pipeline":["gs_pipe.mods.example.square", "gs_pipe.mods.example.minus_one"]},
    headers={
        'Authorization': 'token <your token>',
        'Content-Type': 'application/json'
    }
)
print(response.json())
```

#### Result

> Example

```json

    {
        "created_at": "2018-04-01 05:39:46.622617",
        "description": "gs_pipe.controller.evaluate_pipeline([10, '3'], ['gs_pipe.mods.example.square', 'gs_pipe.mods.example.minus_one'])",
        "id": "5d1939cc-5c63-4559-a0a4-6c25b01793a1",
        "result": null,
        "status": "queued"
    }
```

### Get Task

#### HTTP API

`GET http://localhost:5000/task/<task_id>`


#### Result

> Example

```json
{
    "created_at": "2018-04-01 05:40:20.627292",
    "description": "gs_pipe.controller.evaluate_pipeline([10, 12, 122], ['gs_pipe.mods.example.square', 'gs_pipe.mods.example.minus_one'])",
    "id": "8d78105b-fd86-441e-9a00-29a9e699c186",
    "result": [
        99,
        143,
        14883
    ],
    "status": "finished"
}
```



## RUN

Use `docker run`


## Build


Use `docker build -f Dockerfile .`


## RoadMap

- [ ] ADD Authorization
- [ ] Web Console Dashboard
- [ ] Mods extend 
