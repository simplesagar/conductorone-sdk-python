"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .userview import UserView
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserServiceGetResponseExpanded:
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    UNSET='__SPEAKEASY_UNSET__'
    at_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    r"""The type of the serialized message."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserServiceGetResponse:
    r"""The UserServiceGetResponse returns a user view which has a user including JSONPATHs to the expanded items in the expanded array."""
    UNSET='__SPEAKEASY_UNSET__'
    user_view: Optional[UserView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userView'), 'exclude': lambda f: f is None }})
    r"""The UserView object provides a user response object, as well as JSONPATHs to related objects provided by expanders."""
    expanded: Optional[List[UserServiceGetResponseExpanded]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expanded'), 'exclude': lambda f: f is UserServiceGetResponse.UNSET }})
    r"""List of serialized related objects."""
    

