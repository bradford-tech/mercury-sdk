from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.international_wire_australia_specific_data import InternationalWireAustraliaSpecificData
    from ..models.international_wire_brazil_specific_data import InternationalWireBrazilSpecificData
    from ..models.international_wire_canada_specific_data import InternationalWireCanadaSpecificData
    from ..models.international_wire_chile_specific_data import InternationalWireChileSpecificData
    from ..models.international_wire_colombia_specific_data import InternationalWireColombiaSpecificData
    from ..models.international_wire_dominican_republic_specific_data import (
        InternationalWireDominicanRepublicSpecificData,
    )
    from ..models.international_wire_honduras_specific_data import InternationalWireHondurasSpecificData
    from ..models.international_wire_india_specific_data import InternationalWireIndiaSpecificData
    from ..models.international_wire_kazakhstan_specific_data import InternationalWireKazakhstanSpecificData
    from ..models.international_wire_pakistan_specific_data import InternationalWirePakistanSpecificData
    from ..models.international_wire_paraguay_specific_data import InternationalWireParaguaySpecificData
    from ..models.international_wire_philippines_specific_data import InternationalWirePhilippinesSpecificData
    from ..models.international_wire_russia_specific_data import InternationalWireRussiaSpecificData
    from ..models.international_wire_south_africa_specific_data import InternationalWireSouthAfricaSpecificData


T = TypeVar("T", bound="InternationalWireCountrySpecificData")


@_attrs_define
class InternationalWireCountrySpecificData:
    """
    Attributes:
        australia (InternationalWireAustraliaSpecificData | None | Unset):
        brazil (InternationalWireBrazilSpecificData | None | Unset):
        canada (InternationalWireCanadaSpecificData | None | Unset):
        chile (InternationalWireChileSpecificData | None | Unset):
        colombia (InternationalWireColombiaSpecificData | None | Unset):
        dominican_republic (InternationalWireDominicanRepublicSpecificData | None | Unset):
        honduras (InternationalWireHondurasSpecificData | None | Unset):
        india (InternationalWireIndiaSpecificData | None | Unset):
        kazakhstan (InternationalWireKazakhstanSpecificData | None | Unset):
        pakistan (InternationalWirePakistanSpecificData | None | Unset):
        paraguay (InternationalWireParaguaySpecificData | None | Unset):
        philippines (InternationalWirePhilippinesSpecificData | None | Unset):
        russia (InternationalWireRussiaSpecificData | None | Unset):
        south_africa (InternationalWireSouthAfricaSpecificData | None | Unset):
    """

    australia: InternationalWireAustraliaSpecificData | None | Unset = UNSET
    brazil: InternationalWireBrazilSpecificData | None | Unset = UNSET
    canada: InternationalWireCanadaSpecificData | None | Unset = UNSET
    chile: InternationalWireChileSpecificData | None | Unset = UNSET
    colombia: InternationalWireColombiaSpecificData | None | Unset = UNSET
    dominican_republic: InternationalWireDominicanRepublicSpecificData | None | Unset = UNSET
    honduras: InternationalWireHondurasSpecificData | None | Unset = UNSET
    india: InternationalWireIndiaSpecificData | None | Unset = UNSET
    kazakhstan: InternationalWireKazakhstanSpecificData | None | Unset = UNSET
    pakistan: InternationalWirePakistanSpecificData | None | Unset = UNSET
    paraguay: InternationalWireParaguaySpecificData | None | Unset = UNSET
    philippines: InternationalWirePhilippinesSpecificData | None | Unset = UNSET
    russia: InternationalWireRussiaSpecificData | None | Unset = UNSET
    south_africa: InternationalWireSouthAfricaSpecificData | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.international_wire_australia_specific_data import InternationalWireAustraliaSpecificData
        from ..models.international_wire_brazil_specific_data import InternationalWireBrazilSpecificData
        from ..models.international_wire_canada_specific_data import InternationalWireCanadaSpecificData
        from ..models.international_wire_chile_specific_data import InternationalWireChileSpecificData
        from ..models.international_wire_colombia_specific_data import InternationalWireColombiaSpecificData
        from ..models.international_wire_dominican_republic_specific_data import (
            InternationalWireDominicanRepublicSpecificData,
        )
        from ..models.international_wire_honduras_specific_data import InternationalWireHondurasSpecificData
        from ..models.international_wire_india_specific_data import InternationalWireIndiaSpecificData
        from ..models.international_wire_kazakhstan_specific_data import InternationalWireKazakhstanSpecificData
        from ..models.international_wire_pakistan_specific_data import InternationalWirePakistanSpecificData
        from ..models.international_wire_paraguay_specific_data import InternationalWireParaguaySpecificData
        from ..models.international_wire_philippines_specific_data import InternationalWirePhilippinesSpecificData
        from ..models.international_wire_russia_specific_data import InternationalWireRussiaSpecificData
        from ..models.international_wire_south_africa_specific_data import InternationalWireSouthAfricaSpecificData

        australia: dict[str, Any] | None | Unset
        if isinstance(self.australia, Unset):
            australia = UNSET
        elif isinstance(self.australia, InternationalWireAustraliaSpecificData):
            australia = self.australia.to_dict()
        else:
            australia = self.australia

        brazil: dict[str, Any] | None | Unset
        if isinstance(self.brazil, Unset):
            brazil = UNSET
        elif isinstance(self.brazil, InternationalWireBrazilSpecificData):
            brazil = self.brazil.to_dict()
        else:
            brazil = self.brazil

        canada: dict[str, Any] | None | Unset
        if isinstance(self.canada, Unset):
            canada = UNSET
        elif isinstance(self.canada, InternationalWireCanadaSpecificData):
            canada = self.canada.to_dict()
        else:
            canada = self.canada

        chile: dict[str, Any] | None | Unset
        if isinstance(self.chile, Unset):
            chile = UNSET
        elif isinstance(self.chile, InternationalWireChileSpecificData):
            chile = self.chile.to_dict()
        else:
            chile = self.chile

        colombia: dict[str, Any] | None | Unset
        if isinstance(self.colombia, Unset):
            colombia = UNSET
        elif isinstance(self.colombia, InternationalWireColombiaSpecificData):
            colombia = self.colombia.to_dict()
        else:
            colombia = self.colombia

        dominican_republic: dict[str, Any] | None | Unset
        if isinstance(self.dominican_republic, Unset):
            dominican_republic = UNSET
        elif isinstance(self.dominican_republic, InternationalWireDominicanRepublicSpecificData):
            dominican_republic = self.dominican_republic.to_dict()
        else:
            dominican_republic = self.dominican_republic

        honduras: dict[str, Any] | None | Unset
        if isinstance(self.honduras, Unset):
            honduras = UNSET
        elif isinstance(self.honduras, InternationalWireHondurasSpecificData):
            honduras = self.honduras.to_dict()
        else:
            honduras = self.honduras

        india: dict[str, Any] | None | Unset
        if isinstance(self.india, Unset):
            india = UNSET
        elif isinstance(self.india, InternationalWireIndiaSpecificData):
            india = self.india.to_dict()
        else:
            india = self.india

        kazakhstan: dict[str, Any] | None | Unset
        if isinstance(self.kazakhstan, Unset):
            kazakhstan = UNSET
        elif isinstance(self.kazakhstan, InternationalWireKazakhstanSpecificData):
            kazakhstan = self.kazakhstan.to_dict()
        else:
            kazakhstan = self.kazakhstan

        pakistan: dict[str, Any] | None | Unset
        if isinstance(self.pakistan, Unset):
            pakistan = UNSET
        elif isinstance(self.pakistan, InternationalWirePakistanSpecificData):
            pakistan = self.pakistan.to_dict()
        else:
            pakistan = self.pakistan

        paraguay: dict[str, Any] | None | Unset
        if isinstance(self.paraguay, Unset):
            paraguay = UNSET
        elif isinstance(self.paraguay, InternationalWireParaguaySpecificData):
            paraguay = self.paraguay.to_dict()
        else:
            paraguay = self.paraguay

        philippines: dict[str, Any] | None | Unset
        if isinstance(self.philippines, Unset):
            philippines = UNSET
        elif isinstance(self.philippines, InternationalWirePhilippinesSpecificData):
            philippines = self.philippines.to_dict()
        else:
            philippines = self.philippines

        russia: dict[str, Any] | None | Unset
        if isinstance(self.russia, Unset):
            russia = UNSET
        elif isinstance(self.russia, InternationalWireRussiaSpecificData):
            russia = self.russia.to_dict()
        else:
            russia = self.russia

        south_africa: dict[str, Any] | None | Unset
        if isinstance(self.south_africa, Unset):
            south_africa = UNSET
        elif isinstance(self.south_africa, InternationalWireSouthAfricaSpecificData):
            south_africa = self.south_africa.to_dict()
        else:
            south_africa = self.south_africa

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if australia is not UNSET:
            field_dict["australia"] = australia
        if brazil is not UNSET:
            field_dict["brazil"] = brazil
        if canada is not UNSET:
            field_dict["canada"] = canada
        if chile is not UNSET:
            field_dict["chile"] = chile
        if colombia is not UNSET:
            field_dict["colombia"] = colombia
        if dominican_republic is not UNSET:
            field_dict["dominicanRepublic"] = dominican_republic
        if honduras is not UNSET:
            field_dict["honduras"] = honduras
        if india is not UNSET:
            field_dict["india"] = india
        if kazakhstan is not UNSET:
            field_dict["kazakhstan"] = kazakhstan
        if pakistan is not UNSET:
            field_dict["pakistan"] = pakistan
        if paraguay is not UNSET:
            field_dict["paraguay"] = paraguay
        if philippines is not UNSET:
            field_dict["philippines"] = philippines
        if russia is not UNSET:
            field_dict["russia"] = russia
        if south_africa is not UNSET:
            field_dict["southAfrica"] = south_africa

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.international_wire_australia_specific_data import InternationalWireAustraliaSpecificData
        from ..models.international_wire_brazil_specific_data import InternationalWireBrazilSpecificData
        from ..models.international_wire_canada_specific_data import InternationalWireCanadaSpecificData
        from ..models.international_wire_chile_specific_data import InternationalWireChileSpecificData
        from ..models.international_wire_colombia_specific_data import InternationalWireColombiaSpecificData
        from ..models.international_wire_dominican_republic_specific_data import (
            InternationalWireDominicanRepublicSpecificData,
        )
        from ..models.international_wire_honduras_specific_data import InternationalWireHondurasSpecificData
        from ..models.international_wire_india_specific_data import InternationalWireIndiaSpecificData
        from ..models.international_wire_kazakhstan_specific_data import InternationalWireKazakhstanSpecificData
        from ..models.international_wire_pakistan_specific_data import InternationalWirePakistanSpecificData
        from ..models.international_wire_paraguay_specific_data import InternationalWireParaguaySpecificData
        from ..models.international_wire_philippines_specific_data import InternationalWirePhilippinesSpecificData
        from ..models.international_wire_russia_specific_data import InternationalWireRussiaSpecificData
        from ..models.international_wire_south_africa_specific_data import InternationalWireSouthAfricaSpecificData

        d = dict(src_dict)

        def _parse_australia(data: object) -> InternationalWireAustraliaSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                australia_type_0 = InternationalWireAustraliaSpecificData.from_dict(data)

                return australia_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireAustraliaSpecificData | None | Unset, data)

        australia = _parse_australia(d.pop("australia", UNSET))

        def _parse_brazil(data: object) -> InternationalWireBrazilSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                brazil_type_0 = InternationalWireBrazilSpecificData.from_dict(data)

                return brazil_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireBrazilSpecificData | None | Unset, data)

        brazil = _parse_brazil(d.pop("brazil", UNSET))

        def _parse_canada(data: object) -> InternationalWireCanadaSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                canada_type_0 = InternationalWireCanadaSpecificData.from_dict(data)

                return canada_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireCanadaSpecificData | None | Unset, data)

        canada = _parse_canada(d.pop("canada", UNSET))

        def _parse_chile(data: object) -> InternationalWireChileSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                chile_type_0 = InternationalWireChileSpecificData.from_dict(data)

                return chile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireChileSpecificData | None | Unset, data)

        chile = _parse_chile(d.pop("chile", UNSET))

        def _parse_colombia(data: object) -> InternationalWireColombiaSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                colombia_type_0 = InternationalWireColombiaSpecificData.from_dict(data)

                return colombia_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireColombiaSpecificData | None | Unset, data)

        colombia = _parse_colombia(d.pop("colombia", UNSET))

        def _parse_dominican_republic(data: object) -> InternationalWireDominicanRepublicSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dominican_republic_type_0 = InternationalWireDominicanRepublicSpecificData.from_dict(data)

                return dominican_republic_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireDominicanRepublicSpecificData | None | Unset, data)

        dominican_republic = _parse_dominican_republic(d.pop("dominicanRepublic", UNSET))

        def _parse_honduras(data: object) -> InternationalWireHondurasSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                honduras_type_0 = InternationalWireHondurasSpecificData.from_dict(data)

                return honduras_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireHondurasSpecificData | None | Unset, data)

        honduras = _parse_honduras(d.pop("honduras", UNSET))

        def _parse_india(data: object) -> InternationalWireIndiaSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                india_type_0 = InternationalWireIndiaSpecificData.from_dict(data)

                return india_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireIndiaSpecificData | None | Unset, data)

        india = _parse_india(d.pop("india", UNSET))

        def _parse_kazakhstan(data: object) -> InternationalWireKazakhstanSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kazakhstan_type_0 = InternationalWireKazakhstanSpecificData.from_dict(data)

                return kazakhstan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireKazakhstanSpecificData | None | Unset, data)

        kazakhstan = _parse_kazakhstan(d.pop("kazakhstan", UNSET))

        def _parse_pakistan(data: object) -> InternationalWirePakistanSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pakistan_type_0 = InternationalWirePakistanSpecificData.from_dict(data)

                return pakistan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWirePakistanSpecificData | None | Unset, data)

        pakistan = _parse_pakistan(d.pop("pakistan", UNSET))

        def _parse_paraguay(data: object) -> InternationalWireParaguaySpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                paraguay_type_0 = InternationalWireParaguaySpecificData.from_dict(data)

                return paraguay_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireParaguaySpecificData | None | Unset, data)

        paraguay = _parse_paraguay(d.pop("paraguay", UNSET))

        def _parse_philippines(data: object) -> InternationalWirePhilippinesSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                philippines_type_0 = InternationalWirePhilippinesSpecificData.from_dict(data)

                return philippines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWirePhilippinesSpecificData | None | Unset, data)

        philippines = _parse_philippines(d.pop("philippines", UNSET))

        def _parse_russia(data: object) -> InternationalWireRussiaSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                russia_type_0 = InternationalWireRussiaSpecificData.from_dict(data)

                return russia_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireRussiaSpecificData | None | Unset, data)

        russia = _parse_russia(d.pop("russia", UNSET))

        def _parse_south_africa(data: object) -> InternationalWireSouthAfricaSpecificData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                south_africa_type_0 = InternationalWireSouthAfricaSpecificData.from_dict(data)

                return south_africa_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireSouthAfricaSpecificData | None | Unset, data)

        south_africa = _parse_south_africa(d.pop("southAfrica", UNSET))

        international_wire_country_specific_data = cls(
            australia=australia,
            brazil=brazil,
            canada=canada,
            chile=chile,
            colombia=colombia,
            dominican_republic=dominican_republic,
            honduras=honduras,
            india=india,
            kazakhstan=kazakhstan,
            pakistan=pakistan,
            paraguay=paraguay,
            philippines=philippines,
            russia=russia,
            south_africa=south_africa,
        )

        international_wire_country_specific_data.additional_properties = d
        return international_wire_country_specific_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
