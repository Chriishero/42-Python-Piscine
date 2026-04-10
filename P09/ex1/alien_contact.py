from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validator(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\"")
        if (self.contact_type == ContactType.physical
                and self.is_verified is False):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witness"
                )
        if (self.signal_strength > 7.0 and self.message_received is None):
            raise ValueError(
                "Strong signals (>7.0) should include received messages"
                )
        return self


def main() -> None:
    print("Space Station data Validation")
    valid_report = AlienContact(
        contact_id="AC_2024_001", contact_type=ContactType.radio,
        timestamp=datetime(2024, 1, 1), location="Area 51, Nevada",
        signal_strength=8.5, duration_minutes=45, witness_count=5,
        message_received="Greetings from Zeta Reticulli", is_verified=False
        )
    print("========================================")
    print("Valid contact report")
    print("ID:", valid_report.contact_id)
    print("Type:", valid_report.contact_type.value)
    print("Location:", valid_report.location)
    print(f"Signal: {valid_report.signal_strength}/10")
    print(f"Duration: {valid_report.duration_minutes} minutes")
    print("Witnesses:", valid_report.witness_count)
    print(f"Message: '{valid_report.message_received}'")
    print("========================================")
    print()

    try:
        AlienContact(
            contact_id="AC_2024_001", contact_type=ContactType.telepathic,
            timestamp=datetime(2024, 1, 1), location="Area 51, Nevada",
            signal_strength=8.5, duration_minutes=45, witness_count=2,
            message_received="Greetings from Zeta Reticulli", is_verified=False
            )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
