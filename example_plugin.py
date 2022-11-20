#!/usr/bin/env python
import json
import logging
import sys
from typing import Set, Iterator, Tuple
from contextlib import contextmanager

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse
from google.protobuf.descriptor_pb2 import FileDescriptorProto
from google.protobuf.json_format import MessageToDict


logger = logging.getLogger(__name__)
logging.basicConfig(
    format="[%(asctime)s %(levelname)s] %(message)s", datefmt="%y-%m-%d %H:%M:%S", level=logging.INFO
)


def process_file(
    proto_file: FileDescriptorProto, response: CodeGeneratorResponse
) -> None:
    options = str(proto_file.options).strip().replace("\n", ", ").replace('"', "")
    file = response.file.add()
    file.name = proto_file.name + ".json"
    file.content = json.dumps(
        {
            "package": f"{proto_file.package}",
            "filename": f"{proto_file.name}",
            "dependencies": list(proto_file.dependency),
            "message_type": [MessageToDict(i) for i in proto_file.message_type],
            "service": [MessageToDict(i) for i in proto_file.service],
            "public_dependency": list(proto_file.public_dependency),
            "enum_type": [MessageToDict(i) for i in proto_file.enum_type],
            "extension": [MessageToDict(i) for i in proto_file.extension],
            "options": dict(item.split(": ") for item in options.split(", ") if options),
        },
        indent=2
    ) + "\r\n"


@contextmanager
def code_generation() -> Iterator[Tuple[CodeGeneratorRequest, CodeGeneratorResponse]]:
    """copy form mypy"""
    # Parse request
    request: CodeGeneratorResponse = CodeGeneratorRequest.FromString(sys.stdin.buffer.read())
    # Create response
    response: CodeGeneratorResponse = CodeGeneratorResponse()

    # Declare support for optional proto3 fields
    response.supported_features |= CodeGeneratorResponse.FEATURE_PROTO3_OPTIONAL

    yield request, response

    # Serialise response message
    output = response.SerializeToString()
    # Write to stdout
    sys.stdout.buffer.write(output)


def main() -> None:
    with code_generation() as (request, response):
        file_name_set: Set[str] = {i for i in request.file_to_generate}
        for proto_file in request.proto_file:
            if proto_file.name not in file_name_set:
                # Only process .proto files on the command line
                continue
            process_file(proto_file, response)


if __name__ == "__main__":
    main()
