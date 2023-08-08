"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SelfApproval:
    r"""The self approval object describes the configuration of a policy step that needs to be approved by the target of the request."""
    assigned_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedUserIds'), 'exclude': lambda f: f is None }})
    r"""The array of users determined to be themselves during approval. This should only ever be one person, but is saved because it may change if the owner of an app user changes while the ticket is open."""
    fallback: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallback'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow a fallback if the identity user of the target app user cannot be determined."""
    fallback_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallbackUserIds'), 'exclude': lambda f: f is None }})
    r"""Configuration to specific which users to fallback to if fallback is enabled and the identity user of the target app user cannot be determined."""
    
