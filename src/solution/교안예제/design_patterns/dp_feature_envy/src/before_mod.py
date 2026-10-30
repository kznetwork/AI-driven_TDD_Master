from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    zip_code: str


@dataclass
class Customer:
    name: str
    address: Address


class Invoice:
    def customer_info(self, customer):
        a = customer.address                     # Address 의 데이터만 잔뜩 쓴다 → 기능 편애
        return f"{a.street}, {a.city} {a.zip_code}"
