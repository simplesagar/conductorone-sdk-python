"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import webhooksservicetestrequest as shared_webhooksservicetestrequest
from ...models.shared import webhooksservicetestresponse as shared_webhooksservicetestresponse
from typing import Optional


@dataclasses.dataclass
class C1APIWebhooksV1WebhooksServiceTestRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    webhooks_service_test_request: Optional[shared_webhooksservicetestrequest.WebhooksServiceTestRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIWebhooksV1WebhooksServiceTestResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhooks_service_test_response: Optional[shared_webhooksservicetestresponse.WebhooksServiceTestResponse] = dataclasses.field(default=None)
    r"""Successful response"""
    

