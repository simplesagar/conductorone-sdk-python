"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deleteattributevaluerequest as shared_deleteattributevaluerequest
from ...models.shared import deleteattributevalueresponse as shared_deleteattributevalueresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAttributeV1AttributesDeleteAttributeValueRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    delete_attribute_value_request: Optional[shared_deleteattributevaluerequest.DeleteAttributeValueRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAttributeV1AttributesDeleteAttributeValueResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    delete_attribute_value_response: Optional[shared_deleteattributevalueresponse.DeleteAttributeValueResponse] = dataclasses.field(default=None)
    r"""DeleteAttributeValueResponse is the empty response for deleting an attribute value."""
    

