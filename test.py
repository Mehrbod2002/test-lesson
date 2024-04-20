import requests
import json

url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYmE5ZDA0NGRhYTA0NmYzZmM0NTdkODVkZmViNDdhNSIsInN1YiI6IjY0ZjBiOWZiZTBjYTdmMDEyZWIyNzM3YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4RxWv3pIpFLrC5MDrIJysTChlNMfTY7nSlqhK5dj4Ps"
}

data = []

url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={500}"
response = requests.get(url, headers=headers).json()


# for i in range(41444):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={i+1}"
#         response = requests.get(url, headers=headers).json()
#         data.extend(response["results"])
#         print("Added")
#     except Exception as e:
#         print(e, response, i)
#         with open("movies.json", 'a+') as json_file:
#             json_file.seek(0)
#             try:
#                 existing_data = json.load(json_file)
#             except json.JSONDecodeError:
#                 existing_data = []
#             existing_data.append(data)
#             json_file.seek(0)
#             json.dump(existing_data, json_file, indent=2)
#             break
# print("done")

print("hello world")