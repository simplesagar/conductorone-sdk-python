"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .userexpandmask import UserExpandMask
from .userref import UserRef
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import List, Optional

class UserStatuses(str, Enum):
    UNKNOWN = 'UNKNOWN'
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'
    DELETED = 'DELETED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchUsersRequest:
    r"""Search for users based on some filters."""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Search for users based on their email (exact match)."""
    exclude_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeIds') }})
    r"""An array of users IDs to exclude from the results."""
    ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ids') }})
    r"""Deprecated. Use refs array instead."""
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize'), 'exclude': lambda f: f is None }})
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageToken'), 'exclude': lambda f: f is None }})
    r"""The pageToken field."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    r"""Query the apps with a fuzzy search on display name and emails."""
    refs: Optional[List[UserRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refs') }})
    r"""An array of user refs to restrict the return values to by ID."""
    role_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('roleIds') }})
    r"""Search for users that have any of the role IDs on this list."""
    user_expand_mask: Optional[UserExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The user expand mask is used to indicate which related objects should be expanded in the response.
     The supported paths are 'role_ids', 'manager_ids', 'delegated_user_id', 'directory_ids', and '*'.
    """
    user_statuses: Optional[List[UserStatuses]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userStatuses') }})
    r"""Search for users that have any of the statuses on this list. This can only be ENABLED, DISABLED, and DELETED"""
    

