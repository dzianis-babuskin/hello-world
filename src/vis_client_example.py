#!/usr/bin/env python3
# Copyright (c) 2018 EPAM Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import logging

# import requests
#
# from aos_vis_client import VISClient, VISDataSubscription, VISDataAccessor

logger = logging.getLogger(__name__)


VIS_URL = "wss://wwwivi:8088/"

# Go to https://webhook.site/#/ copy and paste server link to HTTP_REQUEST_RECEIVER_URL
HTTP_REQUEST_RECEIVER_URL = "https://webhook.site/9f51e950-4ba8-4abd-aa19-15f7bbed998f"

DATA_SENDING_DELAY = 2
WAIT_TIMEOUT = 5
DELAY_AFTER_ERROR = 2


def main():
    while True:
        print('Hello world!')
        time.sleep(3)


if __name__ == '__main__':
    main()
