# Allegro Summer e-Xperience 2021
Exercise is to create a server application that will return number of stars per repository and sum of stars for any specified user.
Server will return a JSON response as  "repositories": [list of dicts of repositories], "num_of_stars": [sum of stars in all repositories].
In example:
```json
 {"repositories": [
  {
   "repository:": "allegroTask3",
   "stars": 0
  },
  {
   "repository:": "DINO1920-testing",
   "stars": 1
  },
  {
   "repository:": "DINO201920",
   "stars": 0
  },
  {
   "repository:": "DSIK_Projekt_Chatroom",
   "stars": 2
  }],
 "num_of_stars": 3
}
```

## Requirements:
Library to access GitHub REST Api:

`pip install PyGithub`

## Setup:
Run server by writing:
` python main.py `
in cmd or terminal.

## Usage:

Use by sending a GET request to server running on port 8000.

There are two ways to get list of repositories with stargazers count by GET method.
First, to send username after in _http​://url[:port]/[username]_ format, in example: <br>
` curl -X GET http://localhost:8000/sknera `

Or  _http​://url[:port]?username=[username]_  format, in example: <br>
`curl -X GET http://localhost:8000?username=sknera `<br>
Where [username] is valid name of github user.

## To be implemented:
1. User can specify if they want a list of repositories, sum of stars, or both.
2. User can send a POST request, with username as data, in example: <br> 
   ` curl -X POST -d '{"username":"sknera"}' http://localhost:8000 `


