"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import searchattributevaluesresponse as shared_searchattributevaluesresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAttributeV1AttributeSearchSearchAttributeValuesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    search_attribute_values_response: Optional[shared_searchattributevaluesresponse.SearchAttributeValuesResponse] = dataclasses.field(default=None)
    r"""SearchAttributeValuesResponse is the response for searching AttributeValues."""
    

