from system import Quest, Character, Rank, Skill, Enemy
import random

def sample_quest() -> Quest:
    return Quest("Khám phá Rừng Cấm", "daily", "Thu thập thảo dược", reward_exp=50)

def sample_character() -> Character:
    char = Character(name="Gilgamesh", rank=Rank.S, power_type="Noble Phantasm")
    char.skills = [Skill("Gate of Babylon", "attack", "Bắn kho báu", power=999)]
    return char

def get_boss_by_map(name: str) -> Enemy:
    return Enemy(name="Treant", hp=300, attack=30, defense=10, description="Boss cây")