from dataclasses import dataclass, field
from enum import Enum
from typing import List
from datetime import datetime

class Rank(Enum):
    F = 0; D = 1; C = 2; B = 3; A = 4; S = 5

@dataclass
class Skill:
    name: str
    type: str
    description: str
    power: int = 0
    cooldown: int = 0
    special_effect: str = None

@dataclass
class Character:
    name: str
    rank: Rank
    power_type: str
    level: int = 1
    exp: int = 0
    hp: int = 100
    defense: int = 10
    skills: List[Skill] = field(default_factory=list)

@dataclass
class Quest:
    name: str
    category: str
    description: str
    reward_exp: int = 50
    completed: bool = False

@dataclass
class Enemy:
    name: str
    hp: int
    attack: int
    defense: int
    description: str

@dataclass
class Player:
    name: str
    rank: Rank
    characters: List[Character] = field(default_factory=list)
    quests: List[Quest] = field(default_factory=list)
    travel_points: int = 0
    system_shards: int = 0
    system_level: int = 1
    log_history: List[str] = field(default_factory=list)

    def log(self, msg: str):
        time = datetime.now().strftime("%H:%M:%S")
        entry = f"[{time}] {msg}"
        self.log_history.append(entry)
        print(entry)

class OmniDimensionSystem:
    def __init__(self, player: Player):
        self.p = player

    def accept_quest(self, quest):
        self.p.quests.append(quest)
        self.p.log(f"Nhận nhiệm vụ: {quest.name}")

    def travel_dimension(self):
        self.p.travel_points += 10
        self.p.log("Xuyên không và nhận +10 điểm xuyên")

    def spin_gacha(self):
        self.p.log("Gacha thành công! Nhận được vật phẩm huyền thoại.")

    def collect_shard(self):
        self.p.system_shards += 1
        self.p.log("Nhặt được 1 mảnh hệ thống.")

    def upgrade_system(self):
        if self.p.system_shards >= 3:
            self.p.system_shards -= 3
            self.p.system_level += 1
            self.p.log("Hệ thống được nâng cấp!")
        else:
            self.p.log("Không đủ mảnh để nâng cấp hệ thống.")