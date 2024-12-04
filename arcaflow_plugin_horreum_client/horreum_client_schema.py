#!/usr/bin/env python3

import enum
import typing
import re
from dataclasses import dataclass
from arcaflow_plugin_sdk import schema


class access(str, enum.Enum):
    PUBLIC = "PUBLIC"
    PROTECTED = "PROTECTED"
    PRIVATE = "PRIVATE"


@dataclass
class InputParams:
    horreum_url: typing.Annotated[
        str,
        schema.name("Horreum URL"),
        schema.description(
            "The complete base URL for the Horreum server,"
            " such as 'https://horreum.example.com'."
        ),
        schema.pattern(
            re.compile(
                r"(https?:\/\/)?"
                r"[a-zA-Z0-9_-]{1,63}(\.[a-zA-Z0-9_-]{1,63})*"
                r"(:[0-9]{1,5})?"
                r"\/?"
            )
        ),
    ]
    api_key_pattern = re.compile(
        r"HUSR_[A-Z0-9]{8}_[A-Z0-9]{4}_[A-Z0-9]{4}_[A-Z0-9]{4}_[A-Z0-9]{12}"
    )
    horreum_api_key: typing.Annotated[
        str,
        schema.pattern(api_key_pattern),
        schema.name("Horreum API Key"),
        schema.description("The API Key used to authenticate with the Horreum server."),
    ]
    test_name: typing.Annotated[
        str,
        schema.name("test name"),
        schema.description(
            "Name of the target test in Horreum for the object being uploaded."
        ),
    ]
    test_owner: typing.Annotated[
        str,
        schema.name("test owner"),
        schema.description("Owner of the object being uploaded."),
    ]
    test_access_rights: typing.Annotated[
        access,
        schema.name("test access rights"),
        schema.description("Access rights for the object being uploaded."),
    ]
    test_start_time: typing.Annotated[
        str,
        schema.name("test start time"),
        schema.description(
            "Datetime formatted start time for the object being uploaded."
            " Can also be provided as a JSONPath to a key in the document."
        ),
    ]
    test_stop_time: typing.Annotated[
        str,
        schema.name("test stop time"),
        schema.description(
            "Datetime formatted stop time for the object being uploaded."
            " Can also be provided as a JSONPath to a key in the document."
        ),
    ]
    data_object: typing.Annotated[
        typing.Dict[str, typing.Any],
        schema.name("data object for upload"),
        schema.description("Data object to be uploaded to the Horreum server."),
    ]
    tls_verify: typing.Annotated[
        bool,
        schema.name("TLS verify"),
        schema.description(
            "For development and testing pruposes, this can be set to False to disable"
            " TLS verification for connections to Keycloak and Horreum services."
        ),
    ] = True


@dataclass
class SuccessOutput:
    horreum_run_id: typing.Annotated[
        int,
        schema.name("Horreum run id"),
        schema.description("Integer ID for run of test uploaded into Horreum."),
    ]


@dataclass
class ErrorOutput:
    error: typing.Annotated[
        str,
        schema.name("error"),
        schema.description("An error has occured."),
    ]
