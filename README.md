# RESTful-web-service using DOCKER container

Creating a Python RESTful services using Flask and using docker to run the application. But before, we need to install latest version of docker. Once docker is installed into our system see docker quick terminal

## Steps to build and run docker
1. Get inside the app folder in terminal                          
2. Build the docker image:                                           

      ```bash
      docker build -t flask-sample .
      ```
3. once the docker image is created, run the "flask-test-sample" in docker container                                                            
      ```bash
      docker run -d -p 5000:5000 flask-sample
      ```
4. Web Service contains four GET routes as examples shown below with docker IP address.                  
  **GET request1**: Go to http://192.168.99.100:5000/getbestdeals/  to list all bestdeals data.     
  **GET request2**: Go to http://192.168.99.100:5000/getbestdeals/6/  to list the bestdeal with id 6  
  **GET request3**: Go to http://192.168.99.100:5000/getbestdeals/categories/hoodies/  to list the bestdeals with category "Hoodies"  
  **GET request4**: Go to http://192.168.99.100:5000/getbestdeals/city/chicago/  to list the bestdeals with location city "Chicago"        
  **GET request5**: Go to http://192.168.99.100:5000/getbestdeals/city/chicago/categories/suits/  to list the bestdeals with location city "chicago" and with caterory "Suits"    
  
  
  
  
