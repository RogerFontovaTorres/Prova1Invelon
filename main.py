import requests


def get_api_data(url):
    response = requests.get(url)
    json = response.json()
    parsed_data = [(key, json[key]) for key in json]
    return parsed_data


def main():
    data = get_api_data("https://invelonjobinterview.herokuapp.com/api/test2")
    print(data)


if __name__ == '__main__':
    main()


