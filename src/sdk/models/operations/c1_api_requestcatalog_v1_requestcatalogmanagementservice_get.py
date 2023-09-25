"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import requestcatalogmanagementservicegetresponse as shared_requestcatalogmanagementservicegetresponse
from typing import Optional



@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceGetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_get_response: Optional[shared_requestcatalogmanagementservicegetresponse.RequestCatalogManagementServiceGetResponse] = dataclasses.field(default=None)
    r"""The request catalog management service get response returns a request catalog view with the expanded items in the expanded array indicated by the expand mask in the request."""
    

