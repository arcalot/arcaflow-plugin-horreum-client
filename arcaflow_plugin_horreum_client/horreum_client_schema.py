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
        schema.name("horreum url"),
        schema.description("Base URL for the Horreum server."),
        schema.pattern(
            re.compile(
                r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\."
                r"([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
            )
        ),
    ]
    horreum_keycloak_url: typing.Annotated[
        str,
        schema.name("horreum keycloak url"),
        schema.description("Base URL for the Horreum Keycloak server."),
        schema.pattern(
            re.compile(
                r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\."
                r"([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
            )
        ),
    ]
    horreum_username: typing.Annotated[
        str,
        schema.name("horreum username"),
        schema.description("Username for the Horreum server."),
    ]
    horreum_password: typing.Annotated[
        str,
        schema.name("horreum password"),
        schema.description("Password for the Horreum server."),
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
        typing.Any,
        schema.name("data object for upload"),
        schema.description("Data object to be uploaded to the Horreum server"),
    ]


@dataclass
class SuccessOutput:
    horreum_test_id: typing.Annotated[
        int,
        schema.name("horreum test id"),
        schema.description("Integer ID of test uploaded into Horreum"),
    ]


@dataclass
class ErrorOutput:
    error: typing.Annotated[
        str,
        schema.name("error"),
        schema.description("An error has occured"),
    ]
