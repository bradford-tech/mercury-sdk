from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.main_questionnaire_company_structure import MainQuestionnaireCompanyStructure
from ..models.main_questionnaire_entity_formation_document_type import MainQuestionnaireEntityFormationDocumentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIFormationDetails")


@_attrs_define
class APIFormationDetails:
    """
    Attributes:
        federal_ein (None | str): Field should be null (no value), 'Pending' (value will be provided at a later date),
            or a valid value Example: 12-3456789.
        formation_document_file_blob (None | str): Field should be null (no value), 'Pending' (value will be provided at
            a later date), or a valid value Example: 12-3456789.
        company_origin_country (None | str | Unset):
        company_structure (MainQuestionnaireCompanyStructure | None | Unset):
        e_in_document_file_blob (None | str | Unset):
        ein_document_file_blob (None | str | Unset):
        foreign_business_number (None | str | Unset):
        formation_document_type (MainQuestionnaireEntityFormationDocumentType | None | Unset):
    """

    federal_ein: None | str
    formation_document_file_blob: None | str
    company_origin_country: None | str | Unset = UNSET
    company_structure: MainQuestionnaireCompanyStructure | None | Unset = UNSET
    e_in_document_file_blob: None | str | Unset = UNSET
    ein_document_file_blob: None | str | Unset = UNSET
    foreign_business_number: None | str | Unset = UNSET
    formation_document_type: MainQuestionnaireEntityFormationDocumentType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        federal_ein: None | str
        federal_ein = self.federal_ein

        formation_document_file_blob: None | str
        formation_document_file_blob = self.formation_document_file_blob

        company_origin_country: None | str | Unset
        if isinstance(self.company_origin_country, Unset):
            company_origin_country = UNSET
        else:
            company_origin_country = self.company_origin_country

        company_structure: None | str | Unset
        if isinstance(self.company_structure, Unset):
            company_structure = UNSET
        elif isinstance(self.company_structure, MainQuestionnaireCompanyStructure):
            company_structure = self.company_structure.value
        else:
            company_structure = self.company_structure

        e_in_document_file_blob: None | str | Unset
        if isinstance(self.e_in_document_file_blob, Unset):
            e_in_document_file_blob = UNSET
        else:
            e_in_document_file_blob = self.e_in_document_file_blob

        ein_document_file_blob: None | str | Unset
        if isinstance(self.ein_document_file_blob, Unset):
            ein_document_file_blob = UNSET
        else:
            ein_document_file_blob = self.ein_document_file_blob

        foreign_business_number: None | str | Unset
        if isinstance(self.foreign_business_number, Unset):
            foreign_business_number = UNSET
        else:
            foreign_business_number = self.foreign_business_number

        formation_document_type: None | str | Unset
        if isinstance(self.formation_document_type, Unset):
            formation_document_type = UNSET
        elif isinstance(self.formation_document_type, MainQuestionnaireEntityFormationDocumentType):
            formation_document_type = self.formation_document_type.value
        else:
            formation_document_type = self.formation_document_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "federalEin": federal_ein,
                "formationDocumentFileBlob": formation_document_file_blob,
            }
        )
        if company_origin_country is not UNSET:
            field_dict["companyOriginCountry"] = company_origin_country
        if company_structure is not UNSET:
            field_dict["companyStructure"] = company_structure
        if e_in_document_file_blob is not UNSET:
            field_dict["eINDocumentFileBlob"] = e_in_document_file_blob
        if ein_document_file_blob is not UNSET:
            field_dict["einDocumentFileBlob"] = ein_document_file_blob
        if foreign_business_number is not UNSET:
            field_dict["foreignBusinessNumber"] = foreign_business_number
        if formation_document_type is not UNSET:
            field_dict["formationDocumentType"] = formation_document_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_federal_ein(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        federal_ein = _parse_federal_ein(d.pop("federalEin"))

        def _parse_formation_document_file_blob(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        formation_document_file_blob = _parse_formation_document_file_blob(d.pop("formationDocumentFileBlob"))

        def _parse_company_origin_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_origin_country = _parse_company_origin_country(d.pop("companyOriginCountry", UNSET))

        def _parse_company_structure(data: object) -> MainQuestionnaireCompanyStructure | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_structure_type_0 = MainQuestionnaireCompanyStructure(data)

                return company_structure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MainQuestionnaireCompanyStructure | None | Unset, data)

        company_structure = _parse_company_structure(d.pop("companyStructure", UNSET))

        def _parse_e_in_document_file_blob(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_in_document_file_blob = _parse_e_in_document_file_blob(d.pop("eINDocumentFileBlob", UNSET))

        def _parse_ein_document_file_blob(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ein_document_file_blob = _parse_ein_document_file_blob(d.pop("einDocumentFileBlob", UNSET))

        def _parse_foreign_business_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        foreign_business_number = _parse_foreign_business_number(d.pop("foreignBusinessNumber", UNSET))

        def _parse_formation_document_type(data: object) -> MainQuestionnaireEntityFormationDocumentType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                formation_document_type_type_0 = MainQuestionnaireEntityFormationDocumentType(data)

                return formation_document_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MainQuestionnaireEntityFormationDocumentType | None | Unset, data)

        formation_document_type = _parse_formation_document_type(d.pop("formationDocumentType", UNSET))

        api_formation_details = cls(
            federal_ein=federal_ein,
            formation_document_file_blob=formation_document_file_blob,
            company_origin_country=company_origin_country,
            company_structure=company_structure,
            e_in_document_file_blob=e_in_document_file_blob,
            ein_document_file_blob=ein_document_file_blob,
            foreign_business_number=foreign_business_number,
            formation_document_type=formation_document_type,
        )

        api_formation_details.additional_properties = d
        return api_formation_details

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
