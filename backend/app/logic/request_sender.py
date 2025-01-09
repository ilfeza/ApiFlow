import requests

from backend.app.crud import get_test_by_id, create_result


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

        # Выводим статус и JSON-ответ
        status_code = response.status_code
        try:
            json_response = response.json()
        except ValueError:
            json_response = None

        return status_code, json_response

    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return None, None


def send_request(test_id: int):
    description = get_test_by_id(test_id)
    status_code, json_response = start_test(description.url,
                                            description.method,
                                            description.header,
                                            description.body)

    # Возвращаем результат в формате JSON
    result = {
        'status': status_code,
        'result': json_response
    }

    # Здесь возможно нужно просто вернуть результат или использовать его
    create_result(test_id, status_code, json_response)
    return result
