PATHS

# sign up - /api/users
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"shanky","password":"!QAZxsw2"}' http://127.0.0.1:5001/api/users

# to get token 
curl -u shanky:!QAZxsw2 -i -X GET http://127.0.0.1:5001/api/token

# POST location
curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ3ODM0OTI1NCwiaWF0IjoxNDc4MzQ4NjU0fQ.eyJpZCI6MX0.oo5p63kVnVwPdauR1o8GZHQ729QoCNsydmocXqebxlk:anything  -i -X POST  -H "Content-Type: application/json" -d '{"name":"saket", "latitude":1.09238, "longitude":1.433423}' http://127.0.0.1:5001/api/locations

# GET location
curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ3ODM0OTI1NCwiaWF0IjoxNDc4MzQ4NjU0fQ.eyJpZCI6MX0.oo5p63kVnVwPdauR1o8GZHQ729QoCNsydmocXqebxlk:sdhjsd  -i -X GET http://127.0.0.1:5001/api/locations/saket

Note- 
* As from current code, we are not supporting location name with space. It won't throw an error in POST but while using name of location in GET we cannot pass space in URL so it will say location not found
* Instead of token we can also pass username and password in curl request


