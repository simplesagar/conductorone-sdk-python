"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import addappownerrequest as shared_addappownerrequest
from ..shared import addappownerresponse as shared_addappownerresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppOwnersAddRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    add_app_owner_request: Optional[shared_addappownerrequest.AddAppOwnerRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APIAppV1AppOwnersAddResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_app_owner_response: Optional[shared_addappownerresponse.AddAppOwnerResponse] = dataclasses.field(default=None)
    r"""Empty response with a status code indicating success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
