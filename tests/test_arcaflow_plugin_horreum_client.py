#!/usr/bin/env python3

import unittest
import horreum_client_plugin
import horreum_client_schema

from arcaflow_plugin_sdk import plugin


plugin_input = horreum_client_plugin.InputParams(
    mock=True,
    horreum_url="https://horreum.foo.bar.com",
    horreum_keycloak_url="https://horreum-keycloak.foo.bar.com",
    horreum_username="username",
    horreum_password="supersecret",
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

    def test_functional(self):
        input = plugin_input

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
