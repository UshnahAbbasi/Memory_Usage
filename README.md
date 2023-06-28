# Memory_Usage

## The database
There is a postgresql server running on my personal computer. 
- database: db_ushnah
- table: memory_usage
- columns: id, timestamp, memory_footprint, cpu_usage, hour, minte, second
- entries: 150

In the database, the timestamps are total 150, each with 15 second gap. 
- Start timestamp: 2023-06-12 17:06:11
- end timestamp : 2023-06-12 17:43:26



## The API
The API (POST method) is running on 127.0.0.1:2910 

tested via Talend API tester. The query data is added in the body of the POST request and the id, timestamp, memory footprint and cpu usage at that timestamp is the response of this request.
the user can either give
- timestamp
- hour
- hour and minute
- hour, minute and second

  
Sample request:
http://127.0.0.1:2910/usage
Body:
{
  "timestamp" : "2023-06-12 17:43:26"
}
The response of API is:

[
    {
        "cpu_usage": "86.92",
        "hour": 17,
        "id": 150,
        "memory_footprint": "4bcb847458184a51e742d45d32d17d85",
        "minute": 43,
        "second": 26,
        "timestamp": "Mon, 12 Jun 2023 17:43:26 GMT"
    }
]



If the request has hour or minute or second, the number of rows(single or multiple) corresponding to that hour/minute/second will be given as an output. An example is shown below. 

Sample request:
http://127.0.0.1:2910/usage
body:
{
  "hour" : 17,
  "minute" : 43
}
The response of API is:

[
    {
        "cpu_usage": "89.13",
        "hour": 17,
        "id": 149,
        "memory_footprint": "9374a6b9cbaa514342e7bdc18f43ca19",
        "minute": 43,
        "second": 11,
        "timestamp": "Mon, 12 Jun 2023 17:43:11 GMT"
    },
    {
        "cpu_usage": "86.92",
        "hour": 17,
        "id": 150,
        "memory_footprint": "4bcb847458184a51e742d45d32d17d85",
        "minute": 43,
        "second": 26,
        "timestamp": "Mon, 12 Jun 2023 17:43:26 GMT"
    }
]

It has to be made sure that the Content-Type header should be set to application/json.
