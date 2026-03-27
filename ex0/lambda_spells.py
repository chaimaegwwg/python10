def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key = lambda x:x["power"],
        reverse=True
        )

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)
    
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def test() -> None:
    artifacts = [
    {"name": "Crystal Orb", "power": 85, "type": "magic"},
    {"name": "Fire Staff", "power": 92, "type": "fire"},
    {"name": "Shadow Dagger", "power": 78, "type": "dark"}
    ]
    artifacts = artifact_sorter(artifacts)
    for artifact in artifacts:
        print(artifact)
    mages = [
        {"name": "Gandalf", "power": 95, "element": "fire"},
        {"name": "Merlin", "power": 80, "element": "water"},
        {"name": "Saruman", "power": 60, "element": "earth"}
        ]
    strong_mages = power_filter(mages, 70)
    for m in strong_mages:
        print(m["name"], m["power"])
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(transformed)
    stats = mage_stats(mages)
    print(stats)


test()