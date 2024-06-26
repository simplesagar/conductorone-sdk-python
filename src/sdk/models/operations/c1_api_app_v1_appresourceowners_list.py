"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import listappresourceownersresponse as shared_listappresourceownersresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppResourceOwnersListRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    resource_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'resource_id', 'style': 'simple', 'explode': False }})
    resource_type_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'resource_type_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIAppV1AppResourceOwnersListResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_app_resource_owners_response: Optional[shared_listappresourceownersresponse.ListAppResourceOwnersResponse] = dataclasses.field(default=None)
    r"""The ListAppResourceOwnersResponse message contains a list of results and a nextPageToken if applicable"""
    

