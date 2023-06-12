# Memory_Usage

There is a postgresql server running on my personal computer. The txt file contains the commands used to create the table. 
- database: db_ushnah
- user: ushnah
- password: abbasi
- table: memory_usage
- columns: id, timestamp, memory_footprint, cpu_usage
- entries: 150

The API (GET method) is running on 127.0.0.1:2910 

tested via Talend API tester. Sample request:
http://127.0.0.1:2910/usage?timestamp='2023-06-12 17:43:26'
