# Actions plan

+ 1. run webserver (Flask)
+ 2. find data source
+ 3. get data
4. basic architecture
    + frontend
        + registration (sign up)
        + login (sing in)
            - form to get location data + button (weather forecast)
                - result
    - backend
        - DB
            + connect
            + save data
            + get data
        - registration/login
            + signup logic
            - login
        - request:
            - try to external API to get weather forecast
                - show result && save to DB
                - else get data from DB
5. save to DB
6. implement API endpoints
