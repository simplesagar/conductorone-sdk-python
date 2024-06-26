"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connector import Connector
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorView:
    r"""The ConnectorView object provides a connector response object, as well as JSONPATHs to related objects provided by expanders."""
    connector: Optional[Connector] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connector'), 'exclude': lambda f: f is None }})
    r"""A Connector is used to sync objects into Apps"""
    app_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the App object in the expanded array."""
    users_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usersPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the User object in the expanded array. This is the user that is a direct target of the ticket without a specific relationship to a potentially non-existent app user."""
    

