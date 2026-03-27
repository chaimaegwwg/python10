def mage_counter() -> callable:
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

def spell_accumulator(initial_power: int) -> callable:
    total = initial_power
    
    def accumulator(amount):
        nonlocal total
        total += amount
        return total
    
    return accumulator
def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchant

def memory_vault() -> dict[str, callable]:
    memory = {}
    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }
def main()
    counter = mage_counter()

    print(counter())  
    print(counter()) 
    print(counter())

    acc = spell_accumulator(10)

    print(acc(5))
    print(acc(10))
    print(acc(3))  
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    vault = memory_vault()

    vault["store"]("spell", "Fireball")
    vault["store"]("power", 100)

    print(vault["recall"]("spell")) 
    print(vault["recall"]("power")) 
    print(vault["recall"]("mana"))   



main()