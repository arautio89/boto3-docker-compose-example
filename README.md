# boto3-docker-compose-example
Example of using boto3 for file uploading and downloading to Minio storage with docker-compose.

Run `docker-compse up --build` to see how it works.  
You could also go inside the containers and find the `my_file.txt` file with `docker exec -it <container-name> /bin/bash`.  
Print all containers with `docker ps`.  

For example go inside `minio` container with
```
docker exec -it my_minio /bin/bash
```

There do `cd my_minio/export/my-bucket/my_data` and you should find `my_file.txt` (`ls`).  
Run `exit` to leave the container.