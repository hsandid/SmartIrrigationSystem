---
layout: post
parent: In-Progress
title:  "Back-End API Documentation"
nav_order: 2
---

# Back-End API

Current server path will not be displayed here to avoid any abuse. It is still available as a *secret* variable in the *Web Interface* and *Mobile Application* repositories. 

## Available API Calls

### POST ```/signup ```

  - Description: Call allowing new users to sign-up and receive an authentication token/user-id.

  - Request body (in *JSON* format) : 

    ```json
    {
        mobile_number: "+961<phoneNumber>",
        town_id: "<townID>"
    }
    ```

    

    Response body (in *JSON* format) :

    ```json
    {
        user_id: "<userID>",
        auth_token: :"<auth_token>"
    }
    ```

  

### POST ```/login```

  - Description: Allows users to log-in based on a verification code. *Currently not included in features*.

  - Request body (in *JSON* format) : 

    ```json
    {
        mobile_number: "<mobileNumber>",
        verification_code: "<verificationCode>"
    }
    ```

    

  - Response body (in *JSON* format) :
    
    ```json
    {
        user_id: "<userID>",
        auth_token: "<authToken>"
    }
    ```
    
    

  

### POST ```/fields```

  - Description: Call for users to create a new field

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
        name: "<fieldName>",
        area: "<areaID>",
        latitude: <number>,
        longitude: <number>,
        irrigation_system_id: "<irrigationSystemID",
        crop_type_id: "<cropTypeID>",
        town_id: "<townID>"
    }
    ```
    
    
    
  - Response body (in *JSON* format) :
    
    ```json
    {
    	field_id: "<fieldID>"
    }
    ```

  

### GET ```/fields```

  - Description: Returns all fields registered by a specific user

  - Required Header : ``` auth_token ```

  - Response body (in *JSON* format) :
    
    ```json
    {
    	fields: 
        [
        	{
            	name: "<fieldID>",
                area: <number>,
                latitude: <number>,
                longitude: <number>,
                crop_type_id: "<cropTypeID>",
                Irrigation_system_id: "<irrigationSystemID>",
                town_id: "<townID>",
                user_id: "<userID>",
                created_at: <timestamp>,
                updated_at: <timestamp>
        	}
    	]
    }
    ```
    
    

### GET ```/fields/<id>```

  - Description: Returns a specific field which belong to the current user

  - Required Header : ``` auth_token ```

  - Response body (in *JSON* format) :
    
    ```json
    {
        name: "<fieldID>",
        area: <number>,
        latitude: <number>,
        longitude: <number>,
        crop_type_id: "<cropTypeID>",
        Irrigation_system_id: "<irrigationSystemID>",
        town_id: "<townID>",
        user_id: "<userID>",
        created_at: <timestamp>,
        updated_at: <timestamp>
    }
    ```
    
    

  

### PUT ```/fields/<id>```

  - Description: Updates a field created by the current user

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
        name: "<fieldID>",
        area: <number>,
        latitude: <number>,
        longitude: <number>,
        crop_type_id: "<cropTypeID>",
        Irrigation_system_id: "<irrigationSystemID>",
        town_id: "<townID>",
        user_id: "<userID>",
        created_at: <timestamp>,
        updated_at: <timestamp>
    }
    ```
    
    

  

### GET ```/irrigation```

  - Description: Returns the irrigation schedule/history for a field

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	field_id: "<fieldID>",
    	scheduled: <boolean>
    }
    ```
    
    
    
  - Response body (in *JSON* format) :
    
    ```json
    {
        field_id: "<fieldID>",
        watered: <boolean>,
        duration_needed: <number>,
        actual_duration: <number>,
        water_needed: <number>,
        actual_water_used: <number>,
        scheduler_irrigation_time: <timestamp>,
        actual_irrigation_time: <number>,
        current_fuel_price: <number>,
        actual_fuel_cost: <int>,
        emissions: <int>,
        created_at: <timestamp>,
        updated_at: <timestamp>
    }
    ```
    
    

  

- 

### GET ```/irrigation/<irrigation_id>```

  - Description: Returns the irrigation schedule/history for a field

  - Response body (in *JSON* format) :
    
    ```json
    {
        field_id: "<fieldID>",
        watered: <boolean>,
        duration_needed: <number>,
        actual_duration: <number>,
        water_needed: <number>,
        actual_water_used: <number>,
        scheduler_irrigation_time: <timestamp>,
        actual_irrigation_time: <number>,
        current_fuel_price: <number>,
        actual_fuel_cost: <number>,
        emissions: <number>,
        created_at: <timestamp>,
        updated_at: <timestamp>
    }
    ```
    
    

  

### PUT ```/irrigation/<irrigation_id>```

  - Description: Call which allows the user to notify that he irrigated one of his fields

  - Request body (in *JSON* format) : 
    
    ```json
    {
        field_id: "<fieldID>",
        watered: <boolean>,
        actual_duration: <number>,
        actual_water_used: <number>,
        actual_irrigation_time: <number>,
        actual_fuel_cost: <number>,
        emissions: <number>,
        created_at: <timestamp>,
        updated_at: <timestamp>
    }
    ```
    
    

  

### GET ```/tiff/last_updated```

  - Description : Call to get the time at which the TIFF map was last updated
  - Response body (in *JSON* format) : 

  ```json
  {
  	last_updated: <Datestring>
  }
  ```

  

### POST ```/app_logs/device```

  - Description: Get user device model. This will be stored for each user, overwritten at each request

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	device_model: "<deviceModel>"
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```

  

### POST ```/app_logs/app_lang```

  - Description: Get language to which the application is currently set. This will be stored for each user, overwritten at each request

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	app_lang: "<appLanguage>"
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```

  

### POST ```/app_logs/device_lang```

  - Description: Get language to which the user device is currently set. This will be stored for each user, overwritten at each request

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	device_lang: "<deviceLanguage>"
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```

  

### POST ```/app_logs/region```

  - Description: Get the current region of the user. This will be stored for each user, overwritten at each request

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	region: "<regionName>"
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```

  

### POST ```/app_logs/exit_screen```

  - Description: Get the screen from where the user exits the application the most frequently. This will be stored for each user, overwritten at each request

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	screen_name: "<screenName>"
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```

  

### POST ```/app_logs/ui_errors```

  - Description:  Periodically check if any UI error occurred when using the application.This will be stored on a system-level. Contents of this list will be added to the list of errors already stored in database

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	ui_errors: 
        [
            {
                "error_msg": "<errorMsg>",
                "time": <timestamp>
            }
        ]
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```

  

### POST ```/app_logs/server_errors```

  - Description: Periodically check if any server error occurred when using the application. This will be stored on a system-level. Contents of this list will be added to the list of errors already stored in database

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	server_errors: 
        [
            {
                "error_msg": "<errorMsg>",
                "time": <timestamp>
            }
        ]
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```


### POST ```/app_logs/lang_change```

  - Description: Check if the user has changed the application language manually.This will be stored on a user-level. It will be added to the stored total value, please reset to zero locally after sending request

  - Required Header : ``` auth_token ```

  - Request body (in *JSON* format) : 
    
    ```json
    {
    	lang_change: <int>
    }
    ```
    
    
    
  - Response: ```status 204 [NO_CONTENT]```

  

### POST ```/app_logs/ui_response```

  - Description: Get the average UI response time for each user.This will be stored on a user-level. It will be added to the stored total value and a counter of total numbers this response time has been logged will be incremented. Therefore calculating average response time per user.
  
  - Required Header : ``` auth_token ```	
  
  - Request body (in *JSON* format) : 
    
    ```json
    {
    	response_time: <int>
    }
    ```
    
  - Response: ```status 204 [NO_CONTENT]```
