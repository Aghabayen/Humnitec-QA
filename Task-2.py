import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')

print(r.elapsed.microseconds/1000)

if(r.status_code != 200):

    print("status code not 200")

else:
    if(r.elapsed.microseconds/1000 >= 200):

        print("request time more than 200ms ",r.elapsed.microseconds/1000)
    else:

        result = r.json()

        for item in result:

            if(item["company"]["name"].endswith(" Group")):

                print(item["company"]["name"])