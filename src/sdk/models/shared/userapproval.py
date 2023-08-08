"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UserApproval:
    r"""The user approval object describes the approval configuration of a policy step that needs to be approved by a specific list of users."""
    allow_self_approval: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowSelfApproval'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow self approval of if the user is specified and also the target of the ticket."""
    user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIds'), 'exclude': lambda f: f is None }})
    r"""Array of users configured for approval."""
    
