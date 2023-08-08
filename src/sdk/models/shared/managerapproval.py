"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ManagerApproval:
    r"""The manager approval object provides configuration options for approval when the target of the approval is the manager of the user in the task."""
    allow_self_approval: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowSelfApproval'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow self approval if the target user is their own manager. This may occur if a service account has an identity user and manager specified as the same person."""
    assigned_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedUserIds'), 'exclude': lambda f: f is None }})
    r"""The array of users determined to be the manager during processing time."""
    fallback: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallback'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow a fallback if no manager is found."""
    fallback_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallbackUserIds'), 'exclude': lambda f: f is None }})
    r"""Configuration to specific which users to fallback to if fallback is enabled and no manager is found."""
    
