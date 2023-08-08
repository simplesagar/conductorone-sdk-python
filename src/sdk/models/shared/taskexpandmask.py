"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskExpandMask:
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    paths: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paths'), 'exclude': lambda f: f is None }})
    r"""A list of paths to expand in the response. May be any combination of \\"*\\", \\"access_review_id\\", \\"user_id\\", \\"created_by_user_id\\", \\"app_id\\", \\"app_user_id\\", \\"app_entitlement_ids\\", \\"step_approver_ids\\", and \\"identity_user_id\\"."""
    
