from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.card import Card
    from ..models.card_list_response_page import CardListResponsePage


T = TypeVar("T", bound="CardListResponse")


@_attrs_define
class CardListResponse:
    """
    Attributes:
        cards (list[Card]):  List of cards in the current page.
        page (CardListResponsePage):  Pagination cursors for navigating to next/previous pages.
    """

    cards: list[Card]
    page: CardListResponsePage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cards = []
        for cards_item_data in self.cards:
            cards_item = cards_item_data.to_dict()
            cards.append(cards_item)

        page = self.page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cards": cards,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card import Card
        from ..models.card_list_response_page import CardListResponsePage

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = Card.from_dict(cards_item_data)

            cards.append(cards_item)

        page = CardListResponsePage.from_dict(d.pop("page"))

        card_list_response = cls(
            cards=cards,
            page=page,
        )

        card_list_response.additional_properties = d
        return card_list_response

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
