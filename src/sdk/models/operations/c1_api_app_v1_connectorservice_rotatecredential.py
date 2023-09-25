"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectorservicerotatecredentialrequest as shared_connectorservicerotatecredentialrequest
from ..shared import connectorservicerotatecredentialresponse as shared_connectorservicerotatecredentialresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1ConnectorServiceRotateCredentialRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connector_id', 'style': 'simple', 'explode': False }})
    connector_service_rotate_credential_request: Optional[shared_connectorservicerotatecredentialrequest.ConnectorServiceRotateCredentialRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APIAppV1ConnectorServiceRotateCredentialResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connector_service_rotate_credential_response: Optional[shared_connectorservicerotatecredentialresponse.ConnectorServiceRotateCredentialResponse] = dataclasses.field(default=None)
    r"""ConnectorServiceRotateCredentialResponse is the response returned by the rotate method."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

