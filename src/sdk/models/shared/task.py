"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import externalref as shared_externalref
from ..shared import policyinstance as shared_policyinstance
from ..shared import tasktype as shared_tasktype
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any, Optional

class TaskActions(str, Enum):
    TASK_ACTION_TYPE_UNSPECIFIED = 'TASK_ACTION_TYPE_UNSPECIFIED'
    TASK_ACTION_TYPE_CLOSE = 'TASK_ACTION_TYPE_CLOSE'
    TASK_ACTION_TYPE_APPROVE = 'TASK_ACTION_TYPE_APPROVE'
    TASK_ACTION_TYPE_DENY = 'TASK_ACTION_TYPE_DENY'
    TASK_ACTION_TYPE_COMMENT = 'TASK_ACTION_TYPE_COMMENT'
    TASK_ACTION_TYPE_DELETE = 'TASK_ACTION_TYPE_DELETE'
    TASK_ACTION_TYPE_REASSIGN = 'TASK_ACTION_TYPE_REASSIGN'
    TASK_ACTION_TYPE_RESTART = 'TASK_ACTION_TYPE_RESTART'
    TASK_ACTION_TYPE_SEND_REMINDER = 'TASK_ACTION_TYPE_SEND_REMINDER'
    TASK_ACTION_TYPE_PROVISION_COMPLETE = 'TASK_ACTION_TYPE_PROVISION_COMPLETE'
    TASK_ACTION_TYPE_PROVISION_CANCELLED = 'TASK_ACTION_TYPE_PROVISION_CANCELLED'
    TASK_ACTION_TYPE_PROVISION_ERRORED = 'TASK_ACTION_TYPE_PROVISION_ERRORED'
    TASK_ACTION_TYPE_PROVISION_APP_USER_TARGET_CREATED = 'TASK_ACTION_TYPE_PROVISION_APP_USER_TARGET_CREATED'
    TASK_ACTION_TYPE_ROLLBACK_SKIPPED = 'TASK_ACTION_TYPE_ROLLBACK_SKIPPED'
    TASK_ACTION_TYPE_HARD_RESET = 'TASK_ACTION_TYPE_HARD_RESET'
    TASK_ACTION_TYPE_ESCALATE_TO_EMERGENCY_ACCESS = 'TASK_ACTION_TYPE_ESCALATE_TO_EMERGENCY_ACCESS'

class TaskProcessing(str, Enum):
    r"""The processing state of a task as defined by the `processing_enum`"""
    TASK_PROCESSING_TYPE_UNSPECIFIED = 'TASK_PROCESSING_TYPE_UNSPECIFIED'
    TASK_PROCESSING_TYPE_PROCESSING = 'TASK_PROCESSING_TYPE_PROCESSING'
    TASK_PROCESSING_TYPE_WAITING = 'TASK_PROCESSING_TYPE_WAITING'
    TASK_PROCESSING_TYPE_DONE = 'TASK_PROCESSING_TYPE_DONE'

class TaskState(str, Enum):
    r"""The current state of the task as defined by the `state_enum`"""
    TASK_STATE_UNSPECIFIED = 'TASK_STATE_UNSPECIFIED'
    TASK_STATE_OPEN = 'TASK_STATE_OPEN'
    TASK_STATE_CLOSED = 'TASK_STATE_CLOSED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Task:
    r"""A fully-fleged task object. Includes its policy, references to external apps, its type, its processing history, and more."""
    actions: Optional[list[TaskActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions'), 'exclude': lambda f: f is None }})
    r"""The actions that can be performed on the task by the current user."""
    analysis_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('analysisId'), 'exclude': lambda f: f is None }})
    r"""The ID of the analysis object associated with this task created by an analysis workflow if the analysis feature is enabled for your tenant."""
    annotations: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('annotations'), 'exclude': lambda f: f is None }})
    r"""An array of `google.protobuf.Any` annotations with various base64-encoded data."""
    comment_count: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commentCount'), 'exclude': lambda f: f is None }})
    r"""The count of comments."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    created_by_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdByUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the user that is the creator of this task. This may not always match the userId field."""
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the task. This is also known as justification."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the task."""
    emergency_access: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emergencyAccess'), 'exclude': lambda f: f is None }})
    r"""A field indicating whether this task was created using an emergency access flow, or escalated to emergency access. On task creation, it will also use the app entitlement's emergency policy when possible."""
    external_refs: Optional[list[shared_externalref.ExternalRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalRefs'), 'exclude': lambda f: f is None }})
    r"""An array of external references to the task. Historically that has been items like Jira task IDs. This is currently unused, but may come back in the future for integrations."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The ID of the task."""
    numeric_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numericId'), 'exclude': lambda f: f is None }})
    r"""A human-usable numeric ID of a task which can be included in place of the fully qualified task id in path parmeters (but not search queries)."""
    policy_instance: Optional[shared_policyinstance.PolicyInstance] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policy'), 'exclude': lambda f: f is None }})
    r"""A policy instance is an object that contains a reference to the policy it was created from, the currently executing step, the next steps, and the history of previously completed steps."""
    processing: Optional[TaskProcessing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing'), 'exclude': lambda f: f is None }})
    r"""The processing state of a task as defined by the `processing_enum`"""
    state: Optional[TaskState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""The current state of the task as defined by the `state_enum`"""
    step_approver_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stepApproverIds'), 'exclude': lambda f: f is None }})
    r"""An array of IDs belonging to Identity Users that are allowed to review this step in a task."""
    task_type: Optional[shared_tasktype.TaskType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Task Type provides configuration for the type of task: certify, grant, or revoke

    This message contains a oneof named task_type. Only a single field of the following list may be set at a time:
      - grant
      - revoke
      - certify
    """
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId'), 'exclude': lambda f: f is None }})
    r"""The ID of the user that is the target of this task. This may be empty if we're targeting a specific app user that has no known identity user."""
    
