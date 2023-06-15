# Memory_Usage

## The database
There is a postgresql server running on my personal computer. 
- database: db_ushnah
- user: ushnah
- password: abbasi
- table: memory_usage
- columns: id, timestamp, memory_footprint, cpu_usage
- entries: 150

In the database, the timestamps are total 150, each with 15 second gap. 
- Start timestamp: 2023-06-12 17:06:11
- end timestamp : 2023-06-12 17:43:26

## The API
The API (GET method) is running on 127.0.0.1:2910 

tested via Talend API tester. The timestamp is added in the parameters in GET request and the id, timestamp, memory footprint and cpu usage at that timestamp is the response of this request.
Sample request:
http://127.0.0.1:2910/usage?timestamp='2023-06-12 17:43:26'. The response of API is:


<img width="490" alt="image" src="https://github.com/UshnahAbbasi/Memory_Usage/assets/90151235/5055a9c5-989d-4b70-a16b-d3c53dd700b4">
