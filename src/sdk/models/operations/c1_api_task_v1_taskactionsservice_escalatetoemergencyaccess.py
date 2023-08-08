"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import taskactionsserviceescalatetoemergencyaccessrequest as shared_taskactionsserviceescalatetoemergencyaccessrequest
from ..shared import taskserviceactionresponse as shared_taskserviceactionresponse
from typing import Optional



@dataclasses.dataclass
class C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessRequest:
    task_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'task_id', 'style': 'simple', 'explode': False }})
    task_actions_service_escalate_to_emergency_access_request: Optional[shared_taskactionsserviceescalatetoemergencyaccessrequest.TaskActionsServiceEscalateToEmergencyAccessRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    task_service_action_response: Optional[shared_taskserviceactionresponse.TaskServiceActionResponse] = dataclasses.field(default=None)
    r"""Successful response"""
    
