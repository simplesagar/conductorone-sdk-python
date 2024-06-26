"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import userservicegetresponse as shared_userservicegetresponse
from typing import Optional


@dataclasses.dataclass
class C1APIUserV1UserServiceGetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class C1APIUserV1UserServiceGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    user_service_get_response: Optional[shared_userservicegetresponse.UserServiceGetResponse] = dataclasses.field(default=None)
    r"""The UserServiceGetResponse returns a user view which has a user including JSONPATHs to the expanded items in the expanded array."""
    

