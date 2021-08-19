#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @ Tony Chang
# Copyright (c) 1994-2021 Tony Chang aptx4869.tv
# All Rights Reserved.

import sys

from typing import List

from alibabacloud_vod20170321.client import Client as vod20170321Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_vod20170321 import models as vod_20170321_models


class GetVideoIDList:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> vod20170321Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'vod.cn-shanghai.aliyuncs.com'
        return vod20170321Client(config)

    @staticmethod
    def main(
        access_key_id: str,
        access_key_secret: str,
        page_no: int,
        page_size: int,
    ) -> list[str]:
        video_id_list = []
        client = GetVideoIDList.create_client(access_key_id, access_key_secret)
        get_video_list_request = vod_20170321_models.GetVideoListRequest(
            page_no = page_no,
            page_size = page_size
        )
        video_infos = client.get_video_list(get_video_list_request).body.video_list.video
        for video in video_infos:
            video_id_list.append(video.video_id)
        # print(video_id_list)
        return video_id_list

    @staticmethod
    async def main_async(
        access_key_id: str,
        access_key_secret: str,
        page_no: int,
        page_size: int,
    ) -> list[str]:
        video_id_list = []
        client = GetVideoIDList.create_client(access_key_id, access_key_secret)
        get_video_list_request = vod_20170321_models.GetVideoListRequest(
            page_no = page_no,
            page_size = page_size
        )
        video_infos = await client.get_video_list_async(get_video_list_request).body.video_list.video
        for video in video_infos:
            video_id_list.append(video.video_id)
        # print(video_id_list)
        return video_id_list
