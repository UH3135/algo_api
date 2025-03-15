import requests

url = 'http://127.0.0.1:8000/api/algorithm/answers/'  # API 엔드포인트 URL

while True:
    cmd = input("input your command: ")

    if cmd == "get":
        num = input("what's id number?: ")
        if num is not None:
            response = requests.get(f"{url}{num}")
        else:
            response = requests.get(url)

    elif cmd == "post":
        question_id = input("what's question id?: ")
        content = input("what's your answer?: ")

        if question_id is not None and content is not None:
            data = {"question": int(question_id), "content": content}
            response = requests.post(url=url, data=data)

    elif cmd == "delete":
        num = input("what's id number?: ")
        if num is not None:
            response = requests.delete(f"{url}{num}/")

    elif cmd == "put":
        num = input("what's id number?: ")
        subject = input("what's subject?: ")
        number = input("what's problem number?: ")

        if subject is not None or number is not None:
            data = {"subject": subject, "number": number}
            response = requests.put(url=f"{url}{num}/", data=data)

    elif cmd == "q":
        break

    else:
        print("wrong cmd")
        continue

    if response.status_code >= 200 and response.status_code < 300:
        print("success")
        print(f"{cmd}: {response.json()}")  # 응답 데이터 출력
    else:
        print("오류 발생:", response.status_code)
        print(response.json())
