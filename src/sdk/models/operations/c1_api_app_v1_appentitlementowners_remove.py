"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import removeappentitlementownerrequest as shared_removeappentitlementownerrequest
from ...models.shared import removeappentitlementownerresponse as shared_removeappentitlementownerresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppEntitlementOwnersRemoveRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    entitlement_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entitlement_id', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    remove_app_entitlement_owner_request: Optional[shared_removeappentitlementownerrequest.RemoveAppEntitlementOwnerRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAppV1AppEntitlementOwnersRemoveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    remove_app_entitlement_owner_response: Optional[shared_removeappentitlementownerresponse.RemoveAppEntitlementOwnerResponse] = dataclasses.field(default=None)
    r"""The empty response message for removing an app entitlement owner."""
    

