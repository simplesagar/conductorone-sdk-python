"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import createattributevalueresponse as shared_createattributevalueresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAttributeV1AttributesCreateAttributeValueResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    create_attribute_value_response: Optional[shared_createattributevalueresponse.CreateAttributeValueResponse] = dataclasses.field(default=None)
    r"""CreateAttributeValueResponse is the response for creating an attribute value."""
    

