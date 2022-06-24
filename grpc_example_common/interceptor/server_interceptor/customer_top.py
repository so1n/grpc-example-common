import logging
import time
from typing import Any, Callable, List, Tuple

import grpc
from grpc_status import rpc_status
from google.rpc import code_pb2
from google.rpc import status_pb2
from google.protobuf import any_pb2
from grpc_example_common.protos.common.exce_pb2 import Exec

from grpc_example_common.helper.context import context_proxy

from .base import BaseInterceptor

logger: logging.Logger = logging.getLogger()


class CustomerTopInterceptor(BaseInterceptor):
    def intercept(
        self,
        next_handler_method: Callable,
        request_proto_message: Any,
        context: grpc.ServicerContext,
    ) -> Any:
        start_time: float = time.time()
        try:
            # run grpc handler
            return next_handler_method(request_proto_message, context)
        except Exception as e:
            detail = any_pb2.Any()
            detail.Pack(
                Exec(
                    name=e.__class__.__name__,
                    msg=str(e)
                )
            )
            context.abort_with_status(
                rpc_status.to_status(
                    status_pb2.Status(
                        code=code_pb2.RESOURCE_EXHAUSTED,
                        message=str(e),
                        details=[detail],
                    )
                )
            )
            raise e
        finally:
            logging.info(
                f"Got Request. method:{self.method}, code:{context.code()}, detail:{context.details()}, duration:{time.time() - start_time}"
            )
