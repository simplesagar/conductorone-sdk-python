"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import appactionsservicegeneratereportrequest as shared_appactionsservicegeneratereportrequest
from ...models.shared import appactionsservicegeneratereportresponse as shared_appactionsservicegeneratereportresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppReportActionServiceGenerateReportRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    app_actions_service_generate_report_request: Optional[shared_appactionsservicegeneratereportrequest.AppActionsServiceGenerateReportRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAppV1AppReportActionServiceGenerateReportResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    app_actions_service_generate_report_response: Optional[shared_appactionsservicegeneratereportresponse.AppActionsServiceGenerateReportResponse] = dataclasses.field(default=None)
    r"""Empty response body. Status code indicates success."""
    

