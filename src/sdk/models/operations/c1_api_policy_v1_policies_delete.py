"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deletepolicyrequest as shared_deletepolicyrequest
from ..shared import deletepolicyresponse as shared_deletepolicyresponse
from typing import Optional



@dataclasses.dataclass
class C1APIPolicyV1PoliciesDeleteRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    delete_policy_request: Optional[shared_deletepolicyrequest.DeletePolicyRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APIPolicyV1PoliciesDeleteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_policy_response: Optional[shared_deletepolicyresponse.DeletePolicyResponse] = dataclasses.field(default=None)
    r"""Empty response with a status code indicating success."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
