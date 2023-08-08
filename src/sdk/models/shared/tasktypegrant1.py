"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional

class TaskTypeGrantOutcome(str, Enum):
    r"""The outcome of the grant."""
    GRANT_OUTCOME_UNSPECIFIED = 'GRANT_OUTCOME_UNSPECIFIED'
    GRANT_OUTCOME_GRANTED = 'GRANT_OUTCOME_GRANTED'
    GRANT_OUTCOME_DENIED = 'GRANT_OUTCOME_DENIED'
    GRANT_OUTCOME_ERROR = 'GRANT_OUTCOME_ERROR'
    GRANT_OUTCOME_CANCELLED = 'GRANT_OUTCOME_CANCELLED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskTypeGrant1:
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    app_entitlement_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app entitlement."""
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app."""
    app_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app user."""
    grant_duration: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantDuration'), 'exclude': lambda f: f is None }})
    identity_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the user."""
    outcome: Optional[TaskTypeGrantOutcome] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcome'), 'exclude': lambda f: f is None }})
    r"""The outcome of the grant."""
    outcome_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcomeTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    
