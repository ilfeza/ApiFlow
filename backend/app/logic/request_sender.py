import requests


from backend.app import crud


def send_request(test_id: int):
    description = crud.get_test_by_id(test_id)

    result = start_test(description.url,
                        description.method,
                        description.header,
                        description.body)

    print(result)
    return result





def start_test(url, method='GET', data=None, headers=None):
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, data=data, headers=headers)
        elif method.upper() == 'PUT':
            response = requests.put(url, data=data, headers=headers)
        elif method.upper() == 'PATCH':
            response = requests.patch(url, data=data, headers=headers)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers)
        elif method.upper() == 'HEAD':
            response = requests.head(url, headers=headers)
        elif method.upper() == 'OPTIONS':
            response = requests.options(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return response

    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return None

print(send_request(3))