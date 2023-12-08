"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .appentitlement import AppEntitlement
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppEntitlementView:
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    app_entitlement: Optional[AppEntitlement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlement'), 'exclude': lambda f: f is None }})
    r"""The app entitlement represents one permission in a downstream App (SAAS) that can be granted. For example, GitHub Read vs GitHub Write.

    This message contains a oneof named max_grant_duration. Only a single field of the following list may be set at a time:
      - durationUnset
      - durationGrant
    """
    app_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the App object in the  array."""
    app_resource_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourcePath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the App Resource Type object in the expanded array."""
    app_resource_type_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceTypePath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the App Resource object in the  array."""
    

