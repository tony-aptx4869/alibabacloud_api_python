#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @ Tony Chang
# Copyright (c) 1994-2021 Tony Chang https://github.com/tony-aptx4869
# All Rights Reserved.

import oss2

access_key_id = ''
access_key_secret = ''
auth = oss2.Auth(access_key_id, access_key_secret)

oss_region_url = ''
oss_bucket_name = ''
bucket = oss2.Bucket(auth, oss_region_url, oss_bucket_name)
try:
    bucket.delete_bucket()
except oss2.exceptions.BucketNotEmpty:
    print('Bucket is not empty.')
except oss2.exceptions.NoSuchBucket:
    print('Bucket does not exist.')

service = oss2.Service(auth, oss_region_url)

# 列举所有的存储空间。
for b in oss2.BucketIterator(service):
    print(b.name)
