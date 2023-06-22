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
The API (GET method) is running on 127.0.0.1:2910 

tested via Talend API tester. The timestamp is added in the parameters of the GET request and the id, timestamp, memory footprint and cpu usage at that timestamp is the response of this request.
Sample request:
http://127.0.0.1:2910/usage?timestamp='2023-06-12 17:43:26'. The response of API is:

[
    [
        150,
        "Mon, 12 Jun 2023 17:43:26 GMT",
        "4bcb847458184a51e742d45d32d17d85",
        "86.92",
        17,
        43,
        26
    ]
]



If the request has hour or minute or second, the number of rows(single or multiple) corresponding to that hour/minute.second will be given as an output. An example is shown below. 

Sample request:
http://127.0.0.1:2910/usage?hour=17&minute=43. The response of API is:
[
    [
        149,
        "Mon, 12 Jun 2023 17:43:11 GMT",
        "9374a6b9cbaa514342e7bdc18f43ca19",
        "89.13",
        17,
        43,
        11
    ],
    [
        150,
        "Mon, 12 Jun 2023 17:43:26 GMT",
        "4bcb847458184a51e742d45d32d17d85",
        "86.92",
        17,
        43,
        26
    ]
]

