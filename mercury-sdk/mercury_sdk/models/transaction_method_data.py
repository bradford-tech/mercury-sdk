from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_data import AddressData
    from ..models.credit_card_info import CreditCardInfo
    from ..models.debit_card_info import DebitCardInfo
    from ..models.domestic_wire_routing_info import DomesticWireRoutingInfo
    from ..models.electronic_routing_info import ElectronicRoutingInfo
    from ..models.international_wire_routing_info import InternationalWireRoutingInfo


T = TypeVar("T", bound="TransactionMethodData")


@_attrs_define
class TransactionMethodData:
    """
    Attributes:
        address (AddressData | None | Unset):
        credit_card_info (CreditCardInfo | None | Unset):
        debit_card_info (DebitCardInfo | None | Unset):
        domestic_wire_routing_info (DomesticWireRoutingInfo | None | Unset):
        electronic_routing_info (ElectronicRoutingInfo | None | Unset):
        international_wire_routing_info (InternationalWireRoutingInfo | None | Unset):
    """

    address: AddressData | None | Unset = UNSET
    credit_card_info: CreditCardInfo | None | Unset = UNSET
    debit_card_info: DebitCardInfo | None | Unset = UNSET
    domestic_wire_routing_info: DomesticWireRoutingInfo | None | Unset = UNSET
    electronic_routing_info: ElectronicRoutingInfo | None | Unset = UNSET
    international_wire_routing_info: InternationalWireRoutingInfo | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address_data import AddressData
        from ..models.credit_card_info import CreditCardInfo
        from ..models.debit_card_info import DebitCardInfo
        from ..models.domestic_wire_routing_info import DomesticWireRoutingInfo
        from ..models.electronic_routing_info import ElectronicRoutingInfo
        from ..models.international_wire_routing_info import InternationalWireRoutingInfo

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, AddressData):
            address = self.address.to_dict()
        else:
            address = self.address

        credit_card_info: dict[str, Any] | None | Unset
        if isinstance(self.credit_card_info, Unset):
            credit_card_info = UNSET
        elif isinstance(self.credit_card_info, CreditCardInfo):
            credit_card_info = self.credit_card_info.to_dict()
        else:
            credit_card_info = self.credit_card_info

        debit_card_info: dict[str, Any] | None | Unset
        if isinstance(self.debit_card_info, Unset):
            debit_card_info = UNSET
        elif isinstance(self.debit_card_info, DebitCardInfo):
            debit_card_info = self.debit_card_info.to_dict()
        else:
            debit_card_info = self.debit_card_info

        domestic_wire_routing_info: dict[str, Any] | None | Unset
        if isinstance(self.domestic_wire_routing_info, Unset):
            domestic_wire_routing_info = UNSET
        elif isinstance(self.domestic_wire_routing_info, DomesticWireRoutingInfo):
            domestic_wire_routing_info = self.domestic_wire_routing_info.to_dict()
        else:
            domestic_wire_routing_info = self.domestic_wire_routing_info

        electronic_routing_info: dict[str, Any] | None | Unset
        if isinstance(self.electronic_routing_info, Unset):
            electronic_routing_info = UNSET
        elif isinstance(self.electronic_routing_info, ElectronicRoutingInfo):
            electronic_routing_info = self.electronic_routing_info.to_dict()
        else:
            electronic_routing_info = self.electronic_routing_info

        international_wire_routing_info: dict[str, Any] | None | Unset
        if isinstance(self.international_wire_routing_info, Unset):
            international_wire_routing_info = UNSET
        elif isinstance(self.international_wire_routing_info, InternationalWireRoutingInfo):
            international_wire_routing_info = self.international_wire_routing_info.to_dict()
        else:
            international_wire_routing_info = self.international_wire_routing_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if credit_card_info is not UNSET:
            field_dict["creditCardInfo"] = credit_card_info
        if debit_card_info is not UNSET:
            field_dict["debitCardInfo"] = debit_card_info
        if domestic_wire_routing_info is not UNSET:
            field_dict["domesticWireRoutingInfo"] = domestic_wire_routing_info
        if electronic_routing_info is not UNSET:
            field_dict["electronicRoutingInfo"] = electronic_routing_info
        if international_wire_routing_info is not UNSET:
            field_dict["internationalWireRoutingInfo"] = international_wire_routing_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_data import AddressData
        from ..models.credit_card_info import CreditCardInfo
        from ..models.debit_card_info import DebitCardInfo
        from ..models.domestic_wire_routing_info import DomesticWireRoutingInfo
        from ..models.electronic_routing_info import ElectronicRoutingInfo
        from ..models.international_wire_routing_info import InternationalWireRoutingInfo

        d = dict(src_dict)

        def _parse_address(data: object) -> AddressData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = AddressData.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddressData | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_credit_card_info(data: object) -> CreditCardInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credit_card_info_type_0 = CreditCardInfo.from_dict(data)

                return credit_card_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreditCardInfo | None | Unset, data)

        credit_card_info = _parse_credit_card_info(d.pop("creditCardInfo", UNSET))

        def _parse_debit_card_info(data: object) -> DebitCardInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debit_card_info_type_0 = DebitCardInfo.from_dict(data)

                return debit_card_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DebitCardInfo | None | Unset, data)

        debit_card_info = _parse_debit_card_info(d.pop("debitCardInfo", UNSET))

        def _parse_domestic_wire_routing_info(data: object) -> DomesticWireRoutingInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                domestic_wire_routing_info_type_0 = DomesticWireRoutingInfo.from_dict(data)

                return domestic_wire_routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomesticWireRoutingInfo | None | Unset, data)

        domestic_wire_routing_info = _parse_domestic_wire_routing_info(d.pop("domesticWireRoutingInfo", UNSET))

        def _parse_electronic_routing_info(data: object) -> ElectronicRoutingInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                electronic_routing_info_type_0 = ElectronicRoutingInfo.from_dict(data)

                return electronic_routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ElectronicRoutingInfo | None | Unset, data)

        electronic_routing_info = _parse_electronic_routing_info(d.pop("electronicRoutingInfo", UNSET))

        def _parse_international_wire_routing_info(data: object) -> InternationalWireRoutingInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                international_wire_routing_info_type_0 = InternationalWireRoutingInfo.from_dict(data)

                return international_wire_routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireRoutingInfo | None | Unset, data)

        international_wire_routing_info = _parse_international_wire_routing_info(
            d.pop("internationalWireRoutingInfo", UNSET)
        )

        transaction_method_data = cls(
            address=address,
            credit_card_info=credit_card_info,
            debit_card_info=debit_card_info,
            domestic_wire_routing_info=domestic_wire_routing_info,
            electronic_routing_info=electronic_routing_info,
            international_wire_routing_info=international_wire_routing_info,
        )

        transaction_method_data.additional_properties = d
        return transaction_method_data

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
