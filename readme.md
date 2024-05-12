### Sqlalchemy
* Every operation in a sqlalchemy is by default a transaction
* If we use the session or connection object and text() for writing queries it will look like this
    ```
        Begin
        query -> if committed then saved
        rollback 
    ```