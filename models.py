from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, Integer

PG_DSN = f""

engine = create_async_engine(PG_DSN)
DbSession = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase, AsyncAttrs):
    pass

class SwapiPeople(Base):
    __tablename__ = "swapi_people"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    birth_year: Mapped[str] = mapped_column(String, nullable=True)
    eye_color: Mapped[str] = mapped_column(String, nullable=True)
    films: Mapped[str] = mapped_column(String, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=True)
    hair_color: Mapped[str] = mapped_column(String, nullable=True)
    height: Mapped[str] = mapped_column(String, nullable=True)
    homeworld: Mapped[str] = mapped_column(String, nullable=True)
    mass: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    skin_color: Mapped[str] = mapped_column(String, nullable=True)
    created: Mapped[str] = mapped_column(String, nullable=True)
    edited: Mapped[str] = mapped_column(String, nullable=True)
    species: Mapped[str] = mapped_column(String)
    starships: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String, nullable=True)
    vehicles: Mapped[str] = mapped_column(String, nullable=True)

    def __init__(self, id: int, name: str, height: str, mass: str, hair_color: str,
                 skin_color: str, eye_color: str, films: str, birth_year: str,
                 gender: str, homeworld: str, species: str, edited: str,
                 starships: str, vehicles: str, url: str, created: str,):
        self.id = id
        self.name = name
        self.films = films
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.species = species
        self.starships = starships
        self.vehicles = vehicles
        self.url = url
        self.created = created
        self.edited = edited


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def close_orm():
    await engine.dispose()

