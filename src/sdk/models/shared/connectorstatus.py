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

class ConnectorStatusStatus(str, Enum):
    r"""The status of the connector sync."""
    SYNC_STATUS_UNSPECIFIED = 'SYNC_STATUS_UNSPECIFIED'
    SYNC_STATUS_RUNNING = 'SYNC_STATUS_RUNNING'
    SYNC_STATUS_DONE = 'SYNC_STATUS_DONE'
    SYNC_STATUS_ERROR = 'SYNC_STATUS_ERROR'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ConnectorStatus:
    r"""The status field on the connector is used to track the status of the connectors sync, and when syncing last started, completed, or caused the connector to update."""
    completed_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    last_error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastError'), 'exclude': lambda f: f is None }})
    r"""The last error encountered by the connector."""
    started_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    status: Optional[ConnectorStatusStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the connector sync."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    
