#!/usr/bin/env python3

import sys
import typing
import requests
import json

from arcaflow_plugin_sdk import plugin
from horreum_client_schema import InputParams, SuccessOutput, ErrorOutput


@plugin.step(
    id="horreum-client",
    name="Horreum Client",
    description="Uploads an object to the Horreum server",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def horreum_client(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    
    auth_url = params.horreum_keycloak_url + "/realms/horreum/protocol/openid-connect/token"
    auth_obj = {
        "username": params.horreum_username,
        "password": params.horreum_password,
        "grant_type": "password",
        "client_id": "horreum-ui",
    }
    
    auth_return = requests.post(auth_url, json=auth_obj, verify=False)
    token = json.loads(auth_return.text)["access_token"]

    send_url = params.horreum_url + "/api/run/data"
    send_headers = {f"Authorization: Bearer {token}"}
    send_obj = {
        "test": params.test_name,
        "owner": params.test_owner,
        "access": params.test_access_rights,
        "start": params.test_start_time,
        "stop": params.test_stop_time,
        params.data_object,
    }

    send_return = requests.post(send_url, headers=send_headers, json=send_obj, verify=False)

    
    return "success", SuccessOutput(send_return.text)


# # # #!/bin/bash

# # # TOKEN=$(curl -k https://horreum-keycloak.corp.redhat.com/realms/horreum/protocol/openid-connect/token \
# # #     -d 'username=foo@bar.com' --data-urlencode 'password=foobar' \
# # #     -d 'grant_type=password' -d 'client_id=horreum-ui' \
# # #     | jq -r .access_token)
# # # TEST='boot-time-verbose'
# # # START='$.start_time'
# # # STOP='$.end_time'
# # # OWNER='rhivos-perf-team'
# # # ACCESS='PUBLIC'
# # # curl 'https://horreum.corp.redhat.com/api/run/data?test='$TEST'&start='$START'&stop='$STOP'&owner='$OWNER'&access='$ACCESS \
# # #     -k -X POST -H 'content-type: application/json' \
# # #     -H 'Authorization: Bearer '$TOKEN \
# # #     -d @$1



if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                horreum_client,
            )
        )
    )
