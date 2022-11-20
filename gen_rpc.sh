#!/bin/bash
# set venv
export VENV_PREFIX=""
if [ -d 'venv' ] ; then
    export VENV_PREFIX="venv/bin/"
fi
if [ -d '.venv' ] ; then
    export VENV_PREFIX=".venv/bin/"
fi

echo 'use venv path:' ${VENV_PREFIX}

# gen python protos code path
target_p='grpc_example_common'
# project proto path
source_p='protos'
rm -r "${target_p:?}/${source_p:?}"*

${VENV_PREFIX}python -m grpc_tools.protoc \
  --plugin=protoc-gen-custom-plugin=./example_plugin.py --custom-plugin_out=. \
  --mypy_grpc_out=./ \
  --mypy_out=./ \
  --python_out=./ \
  --grpc_python_out=./ \
  -I protos $(find ./protos -name '*.proto')
