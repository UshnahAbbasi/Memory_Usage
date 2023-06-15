# Memory_Usage

There is a postgresql server running on my personal computer. The txt file contains the commands used to create the table. 
- database: db_ushnah
- user: ushnah
- password: abbasi
- table: memory_usage
- columns: id, timestamp, memory_footprint, cpu_usage
- entries: 150

The API (GET method) is running on 127.0.0.1:2910 

tested via Talend API tester. The timestamp is addedin the parameters in GET request and the id, timestamp, memory footprint and cpu usage at that timestamp is the response of this request.
Sample request:
http://127.0.0.1:2910/usage?timestamp='2023-06-12 17:43:26'. The response of API is:


<img width="490" alt="image" src="https://github.com/UshnahAbbasi/Memory_Usage/assets/90151235/5055a9c5-989d-4b70-a16b-d3c53dd700b4">
