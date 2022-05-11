from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

# Entity Pattern

class Entity(BaseModel):
    name: str
    relation: str


class MultipleEntityPatterns(BaseModel):
    entities: List[Entity]


class EntityPatterns(BaseModel):
    singleEntityPatterns: List[str]
    multipleEntityPatterns: MultipleEntityPatterns


class Pattern(BaseModel):
    entityPatterns: Optional[EntityPatterns] = None


# Story

class Story(BaseModel):
    name: str
    story: List[str]


class Stories(BaseModel):
    stories: List[Story]

# Entity

class EntitySlots(BaseModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class Entities(BaseModel):
    entitiesSlots: List[EntitySlots]