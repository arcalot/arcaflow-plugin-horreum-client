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
    auth_url = (
        f"{params.horreum_keycloak_url}/realms/horreum/protocol/openid-connect/token"
    )
    auth_obj = {
        "username": params.horreum_username,
        "password": params.horreum_password,
        "grant_type": "password",
        "client_id": "horreum-ui",
    }

    try:
        print("==> Authenticating with keycloak...")
        auth_return = requests.post(auth_url, data=auth_obj, verify=params.tls_verify)
        auth_return.raise_for_status()
        token = json.loads(auth_return.text)["access_token"]

    except requests.exceptions.SSLError as e:
        return "error", ErrorOutput(
            f"Unable to establish SSL connection with the Keycloak server: {e}"
        )

    except (requests.ConnectionError, requests.HTTPError, requests.Timeout):
        return "error", ErrorOutput(
            f"Error communicating with the Keycloak server: {auth_return.text}"
        )

    send_url = (
        f"{params.horreum_url}/api/run/data?"
        f"test={params.test_name}"
        f"&start={params.test_start_time}"
        f"&stop={params.test_stop_time}"
        f"&owner={params.test_owner}"
        f"&access={params.test_access_rights}"
    )
    send_headers = {
        "Authorization": f"Bearer {token}",
        "content-type": "application/json",
    }

    try:
        print("==> Uploading object to Horreum...")
        send_return = requests.post(
            send_url,
            headers=send_headers,
            json=params.data_object,
            verify=params.tls_verify,
        )

    except requests.exceptions.SSLError as e:
        return "error", ErrorOutput(
            f"Unable to establish SSL connection with the Horreum server: {e}"
        )

    except (requests.ConnectionError, requests.HTTPError, requests.Timeout):
        return "error", ErrorOutput(
            f"Error communicating with the Horreum server: {auth_return.text}"
        )

    if int(send_return.status_code) != 200 or not send_return.text.isdigit():
        return "error", ErrorOutput(f"Failed to upload object: {send_return.text}")

    print("==> Upload complete")
    return "success", SuccessOutput(int(send_return.text))


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                horreum_client,
            )
        )
    )
