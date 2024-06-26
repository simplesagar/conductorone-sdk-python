"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import userservicelistresponse as shared_userservicelistresponse
from typing import Optional


@dataclasses.dataclass
class C1APIUserV1UserServiceListRequest:
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIUserV1UserServiceListResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    user_service_list_response: Optional[shared_userservicelistresponse.UserServiceListResponse] = dataclasses.field(default=None)
    r"""The UserServiceListResponse message contains a list of results and a nextPageToken if applicable."""
    

