"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import getappusagecontrolsresponse as shared_getappusagecontrolsresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppUsageControlsServiceGetRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class C1APIAppV1AppUsageControlsServiceGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_app_usage_controls_response: Optional[shared_getappusagecontrolsresponse.GetAppUsageControlsResponse] = dataclasses.field(default=None)
    r"""The GetAppUsageControlsResponse message contains the retrieved AppUsageControls object."""
    

