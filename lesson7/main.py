import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def get_data_file(headers):
    url = "https://www.landingfolio.com/"

    r = requests.get(url=url,headers=headers)

    with open ("index.html",'w') as file:
        file.write(r.text)


def download_imgs(file_path):
    pass

def main():
    get_data_file(headers=headers)

if __name__ == '__main__':
    main()