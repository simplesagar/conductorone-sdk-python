"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import taskrevokesourceexpired as shared_taskrevokesourceexpired
from ..shared import taskrevokesourcenonusage as shared_taskrevokesourcenonusage
from ..shared import taskrevokesourcerequest as shared_taskrevokesourcerequest
from ..shared import taskrevokesourcereview as shared_taskrevokesourcereview
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskRevokeSource:
    r"""The TaskRevokeSource message indicates the source of the revoke task is one of expired, nonUsage, request, or review.

    This message contains a oneof named origin. Only a single field of the following list may be set at a time:
      - review
      - request
      - expired
      - nonUsage
    """
    task_revoke_source_expired: Optional[shared_taskrevokesourceexpired.TaskRevokeSourceExpired] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expired'), 'exclude': lambda f: f is None }})
    r"""The TaskRevokeSourceExpired message indicates that the source of the revoke task is due to a grant expiring."""
    task_revoke_source_non_usage: Optional[shared_taskrevokesourcenonusage.TaskRevokeSourceNonUsage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nonUsage'), 'exclude': lambda f: f is None }})
    r"""The TaskRevokeSourceNonUsage message indicates that the source of the revoke task is due to the grant not being used."""
    task_revoke_source_request: Optional[shared_taskrevokesourcerequest.TaskRevokeSourceRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request'), 'exclude': lambda f: f is None }})
    r"""The TaskRevokeSourceRequest message indicates that the source of the revoke task was a request."""
    task_revoke_source_review: Optional[shared_taskrevokesourcereview.TaskRevokeSourceReview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('review'), 'exclude': lambda f: f is None }})
    r"""The TaskRevokeSourceReview message tracks which access review was the source of the specificed revoke ticket."""
    
