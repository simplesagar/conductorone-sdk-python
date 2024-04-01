"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import getattributevalueresponse as shared_getattributevalueresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAttributeV1AttributesGetAttributeValueRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class C1APIAttributeV1AttributesGetAttributeValueResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_attribute_value_response: Optional[shared_getattributevalueresponse.GetAttributeValueResponse] = dataclasses.field(default=None)
    r"""GetAttributeValueResponse is the response for getting an attribute value by id."""
    

