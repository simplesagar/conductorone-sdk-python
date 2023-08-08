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

class AppPopulationReportState(str, Enum):
    r"""The state field tracks the state of the AppPopulationReport. This state field can be one of REPORT_STATE_PENDING, REPORT_STATE_UNSPECIFIED, REPORT_STATE_OK, REPORT_STATE_ERROR."""
    REPORT_STATE_UNSPECIFIED = 'REPORT_STATE_UNSPECIFIED'
    REPORT_STATE_PENDING = 'REPORT_STATE_PENDING'
    REPORT_STATE_OK = 'REPORT_STATE_OK'
    REPORT_STATE_ERROR = 'REPORT_STATE_ERROR'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppPopulationReport:
    r"""The AppPopulationReport is a generated report for a specific app that gives details about the app's users. These details include what groups, roles, and other entitlements the users have access to."""
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The appId is the Id of the app which the report is generated for."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    download_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('downloadUrl'), 'exclude': lambda f: f is None }})
    r"""The downloadUrl is the url used for downloading the AppPopulationReport."""
    hashes: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hashes'), 'exclude': lambda f: f is None }})
    r"""The hashes field contains the file hashes of the report."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The id field."""
    state: Optional[AppPopulationReportState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""The state field tracks the state of the AppPopulationReport. This state field can be one of REPORT_STATE_PENDING, REPORT_STATE_UNSPECIFIED, REPORT_STATE_OK, REPORT_STATE_ERROR."""
    
