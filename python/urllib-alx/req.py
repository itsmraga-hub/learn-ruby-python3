

if __name__ == "__main__":
    import requests
    # print(dir(requests))
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    # print(dir(res))
    print(res.text)
    print("    - type: ", str(type(res.text)))
    print("    - content: ", str(res.text))
