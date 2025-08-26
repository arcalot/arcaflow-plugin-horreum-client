#!/usr/bin/env python3

import sys
import typing
import requests

import warnings
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

    # Conditionally suppress SSL warnings only if TLS verification is disabled
    if not params.tls_verify:
        warnings.filterwarnings("ignore", message="Unverified HTTPS request")

    send_url = (
        f"{params.horreum_url}/api/run/data?"
        f"test={params.test_name}"
        f"&start={params.test_start_time}"
        f"&stop={params.test_stop_time}"
        f"&owner={params.test_owner}"
        f"&access={params.test_access_rights}"
    )
    send_headers = {
        "X-Horreum-API-Key": params.horreum_api_key,
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

    except (requests.ConnectionError, requests.Timeout) as e:
        return "error", ErrorOutput(f"Error communicating with the Horreum server: {e}")

    except requests.HTTPError as e:
        return "error", ErrorOutput(f"Error returned from the Horreum server: {e}")

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
