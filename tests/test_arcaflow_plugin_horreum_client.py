#!/usr/bin/env python3

import unittest
import responses
import horreum_client_plugin
import horreum_client_schema

from arcaflow_plugin_sdk import plugin


plugin_input = horreum_client_plugin.InputParams(
    tls_verify=False,
    horreum_url="https://horreum.example.com",
    horreum_api_key="HUSR_00000000_0000_0000_0000_000000000000",
    test_name="$.test_name",
    test_owner="ownername",
    test_access_rights=horreum_client_schema.access.PUBLIC,
    test_start_time="$.start_time",
    test_stop_time="$.end_time",
    data_object={
        "test_name": "testname",
        "$schema": "urn:test-schema:02",
        "cluster_name": "foobar",
        "uuid": "ffffffff-0264-43dc-97f4-42792e8bad6b",
        "start_time": "2023-11-16T15:07:36.345179+01:00",
        "end_time": "2023-11-16T15:16:43.960644+01:00",
        "test_results": [
            {
                "lorem": {
                    "ipsum": "dolor",
                    "sit": "amet",
                },
                "consetetur": {
                    "sadipscing": "elitr",
                    "sed": "diam",
                },
            },
            {
                "nonumy": {
                    "eirmod": "tempor",
                    "invidunt": "ut",
                },
                "labore": {
                    "et": "dolore",
                    "magna": "aliquyam",
                },
            },
        ],
    },
)


class HorreumClientTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(plugin_input)

        plugin.test_object_serialization(
            horreum_client_plugin.SuccessOutput(horreum_run_id=12345)
        )

        plugin.test_object_serialization(
            horreum_client_plugin.ErrorOutput(error="This is an error")
        )

    @responses.activate
    def test_functional(self):
        input = plugin_input

        responses.add(
            responses.POST,
            f"{input.horreum_url}/api/run/data?"
            f"test={input.test_name}"
            f"&start={input.test_start_time}"
            f"&stop={input.test_stop_time}"
            f"&owner={input.test_owner}"
            f"&access={input.test_access_rights}",
            body="12345",
            status=200,
            content_type="text/html",
        )

        output_id, output_data = horreum_client_plugin.horreum_client(
            params=input, run_id="plugin_ci"
        )

        self.assertEqual("success", output_id)
        self.assertEqual(
            output_data,
            horreum_client_plugin.SuccessOutput(12345),
        )


if __name__ == "__main__":
    unittest.main()
