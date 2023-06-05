import os
import re
import shutil
import urllib.request

from convert import *


def merge_videos(dir_name):
    video_list = sorted(os.listdir(dir_name), key=lambda x: (len(x), x))
    # print(video_list)
    print('Merge Start')
    with open(f'{dir_name}.ts', 'wb') as f1:
        for t in video_list:
            with open(os.path.join(dir_name, t), 'rb') as f2:
                shutil.copyfileobj(f2, f1)
    print('Merge complete')


def delete_directory_and_file(dir_name):
    print('Delete Start')
    try:
        for video in os.listdir(dir_name):
            video_path = os.path.join(dir_name, video)
            print(f'Delete {video_path}')
            os.remove(video_path)
    except:
        print(f'Error - Cannot delete file {video}')

    try:
        os.rmdir(dir_name)
    except:
        print(f'Error - Cannot delete directory')
    print('Delete Complete')


def save_video_stream(video_url, extension, num_of_videos, save_directory_path=None):
    '''
    Download video streaming
    video_url: In chrome or edge browser, developer tools - network tab - find xhr(media file)
    extension: ts or mp4, etc. (I write ts)
    num_of_videos: if you don't know number of videos, write big number
    '''

    # make directory
    print('Make directory')
    dir_name = save_directory_path
    if dir_name:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
    else:
        p = re.compile('.mp4$')
        for s in video_url.split('/'):
            m = p.search(s)
            if m:
                dir_name = s[:m.span()[0]]

        if os.path.exists(dir_name):
            pass
        elif dir_name:
            os.mkdir(dir_name)
        else:
            dir_name = video_url
            os.mkdir(dir_name)

    # download videos
    print('Download videos')

    base_zero = count_how_much_zero(num_of_videos)

    try:
        for num in range(num_of_videos + 1):
            save_name = os.path.join(dir_name, f'{str(num).zfill(3)}.{extension}')
            real_video_url = f'{video_url}{"0" * (base_zero - count_how_much_zero(num))}{num}.{extension}'
            urllib.request.urlretrieve(real_video_url, save_name)
    except:
        print('No File Error or The End')
    print("Download complete.")

    # merge files
    merge_videos(dir_name=dir_name)

    # delete directory
    delete_directory_and_file(dir_name=dir_name)

    return dir_name


def count_how_much_zero(num):
    zero_count = 0
    while num >= 10:
        zero_count += 1
        num /= 10
    return zero_count


if __name__ == '__main__':
    urls = [
        # 'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/44378/480288/1289258_720p.mp4/playlist.m3u8',
        'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/44378/489286/1337455_720p.mp4/media_w199851551_'
    ]
    # urls = [
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443341/1103797_720p.mp4/media_w1973923018_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443345/1103831_720p.mp4/media_w38553806_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443346/1103903_720p.mp4/media_w1810745627_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443401/1104026_720p.mp4/media_w1809294832_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443402/1104032_720p.mp4/media_w1483480967_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443403/1104033_720p.mp4/media_w261335892_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443441/1104117_720p.mp4/media_w2110623520_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443457/1104156_720p.mp4/media_w474090097_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443460/1104181_720p.mp4/media_w1118677842_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443465/1104274_720p.mp4/media_w1566130088_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443466/1104281_720p.mp4/media_w123840566_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443559/1104648_720p.mp4/media_w36234175_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443581/1104698_720p.mp4/media_w1153702461_',
    #     'https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/41882/443587/1104713_720p.mp4/media_w372647377_',

    # ]
    for url in urls:
        title = save_video_stream(url, 'ts', 1000)
        convert_ts_to_mp3(title)


# anyio==3.6.2
# boltons==23.0.0
# Bottleneck==1.3.5
# certifi==2023.5.7
# cffi==1.15.1
# charset-normalizer==2.0.4
# conda==23.3.1
# conda-package-handling==1.9.0
# cryptography==38.0.1
# fastapi==0.89.1
# ffmpeg-python==0.2.0
# future==0.18.3
# grpcio==1.42.0
# h5py==3.6.0
# idna==3.4
# jsonpatch==1.32
# jsonpointer==2.1
# numexpr==2.8.4
# numpy==1.23.2
# packaging==23.0
# pandas==1.5.3
# pip==22.3.1
# pluggy==1.0.0
# protobuf==3.19.1
# pycosat==0.6.4
# pycparser==2.21
# pydantic==1.10.4
# pyOpenSSL==22.0.0
# PySocks==1.7.1
# python-dateutil==2.8.2
# pytz==2022.7
# requests==2.28.1
# ruamel.yaml==0.17.21
# ruamel.yaml.clib==0.2.6
# setuptools==65.5.0
# six==1.16.0
# sniffio==1.3.0
# starlette==0.22.0
# toolz==0.12.0
# tqdm==4.64.1
# typing_extensions==4.4.0
# urllib3==1.24.3
# wheel==0.37.1