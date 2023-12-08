"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import listattributevaluesresponse as shared_listattributevaluesresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAttributeV1AttributesListAttributeValuesRequest:
    attribute_type_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attribute_type_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIAttributeV1AttributesListAttributeValuesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_attribute_values_response: Optional[shared_listattributevaluesresponse.ListAttributeValuesResponse] = dataclasses.field(default=None)
    r"""ListAttributeValuesResponse is the response for listing attribute values for a given AttributeType."""
    

