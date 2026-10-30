from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    zip_code: str


def create_user(name, email, phone, address: Address):
    a = address
    return f"{name} <{email}> {phone} / {a.street}, {a.city} {a.zip_code}"
