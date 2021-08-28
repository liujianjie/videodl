'''
Function:
    下载器类
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import click
import warnings
import requests
from .misc import *
warnings.filterwarnings('ignore')


'''下载器类'''
class Downloader():
    def __init__(self, videoinfo, session=None, **kwargs):
        self.videoinfo = videoinfo
        self.session = requests.Session() if session is None else session
        self.__setheaders(videoinfo['source'])
    '''外部调用'''
    def start(self):
        videoinfo, session, headers = self.videoinfo, self.session, self.headers
        checkDir(videoinfo['savedir'])
        try:
            is_success = False
            with session.get(videoinfo['download_url'], headers=headers, stream=True, verify=False) as response:
                if response.status_code == 200:
                    total_size, chunk_size = int(response.headers['content-length']), 1024
                    label = '[FileSize]: %0.2fMB' % (total_size / 1024 / 1024)
                    with click.progressbar(length=total_size, label=label) as progressbar:
                        with open(os.path.join(videoinfo['savedir'], videoinfo['savename']+'.'+videoinfo['ext']), 'wb') as fp:
                            for chunk in response.iter_content(chunk_size=chunk_size):
                                if chunk:
                                    fp.write(chunk)
                                    progressbar.update(len(chunk))
                    is_success = True
        except:
            is_success = False
        return is_success
    '''设置请求头'''
    def __setheaders(self, source):
        self.douyin_headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66',
        }
        self.headers = getattr(self, f'{source}_headers')