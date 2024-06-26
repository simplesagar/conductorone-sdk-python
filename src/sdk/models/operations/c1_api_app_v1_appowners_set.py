"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import setappownersrequest as shared_setappownersrequest
from ...models.shared import setappownersresponse as shared_setappownersresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppOwnersSetRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    set_app_owners_request: Optional[shared_setappownersrequest.SetAppOwnersRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAppV1AppOwnersSetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    set_app_owners_response: Optional[shared_setappownersresponse.SetAppOwnersResponse] = dataclasses.field(default=None)
    r"""The empty response message for setting the app owners."""
    

