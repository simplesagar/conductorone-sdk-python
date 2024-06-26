"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .facetcategory import FacetCategory
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Facets:
    r"""Indicates one value of a facet."""
    UNSET='__SPEAKEASY_UNSET__'
    count: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    r"""The count of items in this facet."""
    facets: Optional[List[FacetCategory]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('facets'), 'exclude': lambda f: f is Facets.UNSET }})
    r"""The facet being referenced."""
    

