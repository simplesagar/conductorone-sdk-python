"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import directoryservicedeleterequest as shared_directoryservicedeleterequest
from ...models.shared import directoryservicedeleteresponse as shared_directoryservicedeleteresponse
from typing import Optional


@dataclasses.dataclass
class C1APIDirectoryV1DirectoryServiceDeleteRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    directory_service_delete_request: Optional[shared_directoryservicedeleterequest.DirectoryServiceDeleteRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIDirectoryV1DirectoryServiceDeleteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    directory_service_delete_response: Optional[shared_directoryservicedeleteresponse.DirectoryServiceDeleteResponse] = dataclasses.field(default=None)
    r"""Empty response with a status code indicating success."""
    

