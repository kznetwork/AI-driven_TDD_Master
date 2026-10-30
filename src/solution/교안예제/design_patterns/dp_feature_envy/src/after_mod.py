from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    zip_code: str

    def format(self):                            # Move Method — 데이터가 있는 곳으로
        return f"{self.street}, {self.city} {self.zip_code}"


@dataclass
class Customer:
    name: str
    address: Address


class Invoice:
    def customer_info(self, customer):
        return customer.address.format()         # 메시지만 전달
