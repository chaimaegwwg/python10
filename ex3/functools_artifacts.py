from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return reduce(ops[operation], spells)

def base_enchantment(power, element, target):
    return f"{element} enchantment ({power}) on {target}"


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)



@spell_dispatcher.register
def _(spell: int):
    return f"Damage spell hits for {spell} points"

@spell_dispatcher.register
def _(spell: str):
    return f"Enchantment cast: {spell}"

@spell_dispatcher.register
def _(spell: list):
    results = [spell_dispatcher(s) for s in spell]
    return f"Multi-cast: {results}"

@singledispatch
def spell_dispatcher() -> callable:
    return f"Unknown spell type: {type(spell)}"


def main():

    print(spell_reducer([10, 5, 3], "add"))      
    print(spell_reducer([10, 5, 3], "multiply"))  
    print(spell_reducer([10, 5, 3], "max"))       
    print(spell_reducer([10, 5, 3], "min")) 

    enchants = partial_enchanter(base_enchantment)

    print(enchants["fire_enchant"]("Sword"))
    print(enchants["ice_enchant"]("Shield"))
    print(enchants["lightning_enchant"]("Armor"))   

    print(memoized_fibonacci(10))  
    print(memoized_fibonacci(15)) 

    print(spell_dispatcher(10))
    print(spell_dispatcher("Fireball"))  
    print(spell_dispatcher([5, "Heal"]))

main()