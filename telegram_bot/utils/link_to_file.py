import requests
from urllib.parse import unquote
from tqdm import tqdm
from config import DEBUG
import os 
from dotenv import load_dotenv
import mimetypes

load_dotenv(override=True)

PROXY_SCHEME = os.getenv('PROXY_SCHEME')
PROXY_HOSTNAME = os.getenv('PROXY_HOSTNAME')
PROXY_PORT = os.getenv('PROXY_PORT')

proxies = {
        'http': f'{PROXY_SCHEME}://{PROXY_HOSTNAME}:{PROXY_PORT}',
        'https': f'{PROXY_SCHEME}://{PROXY_HOSTNAME}:{PROXY_PORT}'
}

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def get_file_type(url):
    mime_type, _ = mimetypes.guess_type(url)
    return mime_type


def get_url_info(url, filename=None):

    try:


        if DEBUG == 'True':response = requests.get(url, stream=True, timeout=5, proxies=proxies, allow_redirects=True)
        else:response = requests.get(url, stream=True, timeout=5, allow_redirects=True)
        main_file_size = int(response.headers.get('content-length', 0))

        if filename is None:
            content_disposition = response.headers.get('Content-Disposition')

            try :
                if content_disposition:filename = unquote(content_disposition.split("filename=")[1])
                else:filename = url.split('/')[-1]
            except : filename = url.split('/')[-1]

        data = {
                    'file_name': filename,
                    'file_size_str': sizeof_fmt(main_file_size),
                    'file_size': main_file_size / (1024 * 1024),
                  }
        
        if main_file_size != 0:
            return data
        return None
    


    except Exception as e:
        print(e)
        return None
