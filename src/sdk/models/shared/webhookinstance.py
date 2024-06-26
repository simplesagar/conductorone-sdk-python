"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .webhooksource import WebhookSource
from .webhookspec import WebhookSpec
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import Optional

class WebhookInstanceState(str, Enum):
    r"""The state field."""
    WEBHOOK_STATE_UNSPECIFIED = 'WEBHOOK_STATE_UNSPECIFIED'
    WEBHOOK_STATE_PENDING = 'WEBHOOK_STATE_PENDING'
    WEBHOOK_STATE_RUNNING = 'WEBHOOK_STATE_RUNNING'
    WEBHOOK_STATE_ERROR = 'WEBHOOK_STATE_ERROR'
    WEBHOOK_STATE_WAITING_CALLBACK = 'WEBHOOK_STATE_WAITING_CALLBACK'
    WEBHOOK_STATE_PROCESS_RESPONSE = 'WEBHOOK_STATE_PROCESS_RESPONSE'
    WEBHOOK_STATE_SUCCESS = 'WEBHOOK_STATE_SUCCESS'
    WEBHOOK_STATE_FATAL_ERROR = 'WEBHOOK_STATE_FATAL_ERROR'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebhookInstance:
    r"""The WebhookInstance message."""
    webhook_source: Optional[WebhookSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The WebhookSource message.

    This message contains a oneof named source. Only a single field of the following list may be set at a time:
      - test
      - policyPostAction
      - approvalStep
      - provisionStep
    """
    webhook_spec: Optional[WebhookSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spec'), 'exclude': lambda f: f is None }})
    r"""The WebhookSpec message."""
    attempts: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attempts'), 'exclude': lambda f: f is None }})
    r"""The attempts field."""
    completed_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiresAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The id field."""
    last_attempted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastAttemptedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    state: Optional[WebhookInstanceState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""The state field."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    webhook_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhookId'), 'exclude': lambda f: f is None }})
    r"""The webhookId field."""
    

