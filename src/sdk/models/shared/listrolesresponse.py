"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .role import Role
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListRolesResponse:
    r"""The ListRolesResponse message contains a list of results and a nextPageToken if applicable."""
    UNSET='__SPEAKEASY_UNSET__'
    list: Optional[List[Role]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list'), 'exclude': lambda f: f is ListRolesResponse.UNSET }})
    r"""The list of results containing up to X results, where X is the page size defined in the request."""
    next_page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nextPageToken'), 'exclude': lambda f: f is None }})
    r"""The nextPageToken is shown for the next page if the number of results is larger than the max page size.
     The server returns one page of results and the nextPageToken until all results are retreived.
     To retrieve the next page, use the same request and append a pageToken field with the value of nextPageToken shown on the previous page.
    """
    

