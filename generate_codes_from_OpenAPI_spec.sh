#! /bin/bash

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/me_gateway_spec.yaml -g python -o /local/me-gateway-client
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/me_gateway_spec.yaml -g python-flask -o /local/me-gateway-server
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/sp_gateway_spec.yaml -g python -o /local/sp-gateway-client
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/sp_gateway_spec.yaml -g python-flask -o /local/sp-gateway-server
