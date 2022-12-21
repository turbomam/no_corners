# Auto generated from no_corners.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-20T19:16:36
# Schema: no_corners
#
# id: https://w3id.org/turbomam/no_corners
# description: Testing a reqular expression for 96-well plates, where the corner wells must not be filled with a
#              test sample
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NO_CORNERS = CurieNamespace('no_corners', 'https://w3id.org/turbomam/no_corners/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = NO_CORNERS


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class BiosampleId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NO_CORNERS.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Biosample(NamedThing):
    """
    Represents a Biosample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NO_CORNERS.Biosample
    class_class_curie: ClassVar[str] = "no_corners:Biosample"
    class_name: ClassVar[str] = "Biosample"
    class_model_uri: ClassVar[URIRef] = NO_CORNERS.Biosample

    id: Union[str, BiosampleId] = None
    well_pos: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)

        if self.well_pos is not None and not isinstance(self.well_pos, str):
            self.well_pos = str(self.well_pos)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleCollection(YAMLRoot):
    """
    A holder for Biosample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NO_CORNERS.BiosampleCollection
    class_class_curie: ClassVar[str] = "no_corners:BiosampleCollection"
    class_name: ClassVar[str] = "BiosampleCollection"
    class_model_uri: ClassVar[URIRef] = NO_CORNERS.BiosampleCollection

    entries: Optional[Union[Dict[Union[str, BiosampleId], Union[dict, Biosample]], List[Union[dict, Biosample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Biosample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=NO_CORNERS.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=NO_CORNERS.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NO_CORNERS.description, domain=None, range=Optional[str])

slots.well_pos = Slot(uri=NO_CORNERS.well_pos, name="well_pos", curie=NO_CORNERS.curie('well_pos'),
                   model_uri=NO_CORNERS.well_pos, domain=None, range=Optional[str],
                   pattern=re.compile(r'A1'))

slots.biosampleCollection__entries = Slot(uri=NO_CORNERS.entries, name="biosampleCollection__entries", curie=NO_CORNERS.curie('entries'),
                   model_uri=NO_CORNERS.biosampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, BiosampleId], Union[dict, Biosample]], List[Union[dict, Biosample]]]])