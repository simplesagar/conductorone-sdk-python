"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .user import User
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserView:
    r"""The UserView object provides a user response object, as well as JSONPATHs to related objects provided by expanders."""
    user: Optional[User] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""The User object provides all of the details for an user, as well as some configuration."""
    delegated_user_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delegatedUserPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the user objects of delegates of the current user in the expanded array."""
    directories_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('directoriesPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of directory objects in the expanded array."""
    managers_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('managersPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the user objects that managed the current user in the expanded array."""
    roles_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rolesPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the roles of the current user in the expanded array."""
    

