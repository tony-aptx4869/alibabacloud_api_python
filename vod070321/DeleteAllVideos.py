#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @ Tony Chang
# Copyright (c) 1994-2021 Tony Chang aptx4869.tv
# All Rights Reserved.

from typing import List
from GetVideoIDList import GetVideoIDList
from DeleteVideo import DeleteVideo

class DeleteAllVideos:
    def __init__(self):
        pass

    @staticmethod
    def get_all_video_ids(
        access_key_id: str,
        access_key_secret: str,
    ) -> list[list]:
        video_id_list = []
        page_no = 0
        while page_no < 50 :
            page_no += 1
            temp_video_id_list = GetVideoIDList.main(access_key_id, access_key_secret, page_no, 100)
            if len(temp_video_id_list) >= 20 :
                video_id_list.append(temp_video_id_list[0:20])
            else:
                video_id_list.append(temp_video_id_list[0:len(temp_video_id_list)])
                break
            if len(temp_video_id_list) >= 40 :
                video_id_list.append(temp_video_id_list[20:40])
            else:
                video_id_list.append(temp_video_id_list[20:len(temp_video_id_list)])
                break
            if len(temp_video_id_list) >= 60 :
                video_id_list.append(temp_video_id_list[40:60])
            else:
                video_id_list.append(temp_video_id_list[40:len(temp_video_id_list)])
                break
            if len(temp_video_id_list) >= 80 :
                video_id_list.append(temp_video_id_list[60:80])
            else:
                video_id_list.append(temp_video_id_list[60:len(temp_video_id_list)])
                break
            if len(temp_video_id_list) == 100 :
                video_id_list.append(temp_video_id_list[80:100])
            else:
                video_id_list.append(temp_video_id_list[80:len(temp_video_id_list)])
                break
        return video_id_list

if __name__ == '__main__':
    video_id_list = DeleteAllVideos.get_all_video_ids('qJjlKgt1U4Qnm9u2', 'QVkQZLlajRe7ZjA44iAkVrcZ0LPWJj')
    # print(video_id_list)
    print(len(video_id_list))
    count_request = 0
    if len(video_id_list) > 0 :
        for video_id in video_id_list :
            video_id_str = ','.join(video_id)
            DeleteVideo.main('qJjlKgt1U4Qnm9u2', 'QVkQZLlajRe7ZjA44iAkVrcZ0LPWJj', video_id_str)
            count_request += 1
    print(count_request)

    # video_list = GetVideoIDList.main('qJjlKgt1U4Qnm9u2', 'QVkQZLlajRe7ZjA44iAkVrcZ0LPWJj', 0, 100)
    # print(video_list[80:100])



    # while True:
    #     video_list = GetVideoIDList.main('qJjlKgt1U4Qnm9u2', 'QVkQZLlajRe7ZjA44iAkVrcZ0LPWJj', 1, 20)
    #     if len(video_list) <= 0:
    #         break
    #     video_ids = ','.join(video_list)
    #     DeleteVideo.main('qJjlKgt1U4Qnm9u2', 'QVkQZLlajRe7ZjA44iAkVrcZ0LPWJj', video_ids)

