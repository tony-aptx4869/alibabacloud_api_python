#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @ Tony Chang
# Copyright (c) 1994-2021 Tony Chang https://github.com/tony-aptx4869
# All Rights Reserved.

import sys

from typing import List

from alibabacloud_vod20170321.client import Client as vod20170321Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_vod20170321 import models as vod_20170321_models


class DeleteVideo:
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
        config.endpoint = 'vod.cn-beijing.aliyuncs.com'
        return vod20170321Client(config)

    @staticmethod
    def main(
        access_key_id: str,
        access_key_secret: str,
        video_ids: str,
    ) -> None:
        client = DeleteVideo.create_client(access_key_id, access_key_secret)
        delete_video_request = vod_20170321_models.DeleteVideoRequest(
            video_ids = video_ids
        )
        response = client.delete_video(delete_video_request).body
        print(response)

    @staticmethod
    async def main_async(
        access_key_id: str,
        access_key_secret: str,
        video_ids: str,
    ) -> None:
        client = DeleteVideo.create_client(access_key_id, access_key_secret)
        delete_video_request = vod_20170321_models.DeleteVideoRequest(
            video_ids = video_ids
        )
        response = await client.delete_video_async(delete_video_request).body
        print(response)
