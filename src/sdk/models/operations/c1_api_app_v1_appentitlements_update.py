"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import updateappentitlementrequest as shared_updateappentitlementrequest
from ...models.shared import updateappentitlementresponse as shared_updateappentitlementresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppEntitlementsUpdateRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    update_app_entitlement_request: Optional[shared_updateappentitlementrequest.UpdateAppEntitlementRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAppV1AppEntitlementsUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_app_entitlement_response: Optional[shared_updateappentitlementresponse.UpdateAppEntitlementResponse] = dataclasses.field(default=None)
    r"""Successful response"""
    

