"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listappentitlementgroupsresponse as shared_listappentitlementgroupsresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppEntitlementsListGroupsRequest:
    app_entitlement_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_entitlement_id', 'style': 'simple', 'explode': False }})
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class C1APIAppV1AppEntitlementsListGroupsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_app_entitlement_groups_response: Optional[shared_listappentitlementgroupsresponse.ListAppEntitlementGroupsResponse] = dataclasses.field(default=None)
    r"""The ListAppEntitlementGroupsResponse message contains a list of results and a nextPageToken if applicable."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
