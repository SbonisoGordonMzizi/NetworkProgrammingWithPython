import http.client


def http_client():
    http_client_object = http.client.HTTPConnection("www.facebook.com")
    http_client_object.request("GET", "/")
    http_response = http_client_object.getresponse()
    print(http_response.getcode())
    print(http_response.headers)
    data = http_response.readlines()
    if data:
        print(data)


if __name__ == "__main__":
    http_client()
