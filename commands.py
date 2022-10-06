import requests

# An idea of using an api as a code compiler for python. Having issues puhsing code to api, does not work. 
def python_code():
    my_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    my_response = {
        "code": "print(hello)",
        "language": "py",
        "input": ""
    }
    response = requests.post("https://codex-api.herokuapp.com/", json=my_response, headers=my_headers).text
    print(response)

if __name__ == "__main__":
  python_code()