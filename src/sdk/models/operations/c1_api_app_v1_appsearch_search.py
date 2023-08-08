"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import searchappsresponse as shared_searchappsresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppSearchSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    search_apps_response: Optional[shared_searchappsresponse.SearchAppsResponse] = dataclasses.field(default=None)
    r"""The SearchAppsResponse message contains a list of results and a nextPageToken if applicable."""
    
