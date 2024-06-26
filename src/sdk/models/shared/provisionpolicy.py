"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connectorprovision import ConnectorProvision
from .delegatedprovision import DelegatedProvision
from .manualprovision import ManualProvision
from .webhookprovision import WebhookProvision
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProvisionPolicy:
    r"""ProvisionPolicy is a oneOf that indicates how a provision step should be processed.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
      - connector
      - manual
      - delegated
      - webhook
    """
    UNSET='__SPEAKEASY_UNSET__'
    connector_provision: Optional[ConnectorProvision] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connector'), 'exclude': lambda f: f is ProvisionPolicy.UNSET }})
    r"""Indicates that a connector should perform the provisioning. This object has no fields."""
    delegated_provision: Optional[DelegatedProvision] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delegated'), 'exclude': lambda f: f is ProvisionPolicy.UNSET }})
    r"""This provision step indicates that we should delegate provisioning to the configuration of another app entitlement. This app entitlement does not have to be one from the same app, but MUST be configured as a proxy binding leading into this entitlement."""
    manual_provision: Optional[ManualProvision] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manual'), 'exclude': lambda f: f is ProvisionPolicy.UNSET }})
    r"""Manual provisioning indicates that a human must intervene for the provisioning of this step."""
    webhook_provision: Optional[WebhookProvision] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook'), 'exclude': lambda f: f is ProvisionPolicy.UNSET }})
    r"""This provision step indicates that a webhook should be called to provision this entitlement."""
    

