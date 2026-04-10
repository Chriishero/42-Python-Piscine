from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officier"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self) -> "SpaceMission":
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with \"M\"")
        high_grade = False
        for member in self.crew:
            if member.rank in (Rank.commander, Rank.captain):
                high_grade = True
                break
        if high_grade is False:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced_members = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_members += 1
            if experienced_members / len(self.crew) < 0.5:
                raise ValueError(
                    "Long mission (> 365 days) need 50% " +
                    "experienced crew (5+ years)"
                    )
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    m1 = CrewMember(member_id="ID_1", name="Sarah Connor", rank=Rank.commander,
                    age=29, specialization="Mission Command",
                    years_experience=8, is_active=True)
    m2 = CrewMember(member_id="ID_2", name="John Smith", rank=Rank.lieutenant,
                    age=24, specialization="Navigation",
                    years_experience=5, is_active=True)
    m3 = CrewMember(member_id="ID_3", name="Alice Johnson", rank=Rank.officer,
                    age=26, specialization="Engineering",
                    years_experience=6, is_active=True)
    print("Space Mission Crew Validation")
    mission = SpaceMission(
        mission_id="M2024_MARS", mission_name="Mars Colony Establishment",
        destination="Mars", launch_date=datetime(2026, 12, 12),
        duration_days=900, crew=[m1, m2, m3], mission_status="planned",
        budget_millions=2500.0
    )
    print("=========================================")
    print("Valid mission created:")
    print("Mission:", mission.mission_name)
    print("ID:", mission.mission_id)
    print("Destination:", mission.destination)
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print("Crew size:", len(mission.crew))
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")
    print()
    print("=========================================")

    try:
        m = CrewMember(member_id="ID_1", name="Sarah Connor", rank=Rank.cadet,
                       age=29, specialization="Mission Command",
                       years_experience=2, is_active=True)
        SpaceMission(
            mission_id="M2024_MARS", mission_name="Mars Colony Establishment",
            destination="Mars", launch_date=datetime(2026, 12, 12),
            duration_days=900, crew=[m], mission_status="planned",
            budget_millions=2500.0
        )
    except ValidationError as e:
        print("Excepted validation error:")
        print(e.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
