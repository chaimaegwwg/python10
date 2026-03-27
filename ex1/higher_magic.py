def fireball(target):
    return 10

def heal(target):
    return 5
def is_dragon(target):
    return target == "Dragon"

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    
    return combined

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified

def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return caster
def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence

def main():
    print("Testing spell combiner...")

    combined_spell = spell_combiner(fireball, heal)
    mega_fireball = power_amplifier(fireball, 3)
    conditional_fireball = conditional_caster(is_dragon, fireball)
    sequence_spell = spell_sequence([fireball, heal])

    print("Combined spell:", combined_spell("Dragon"))
    print("Original fireball:", fireball("Dragon"))
    print("Amplified fireball:", mega_fireball("Dragon"))
    print("Conditional (Dragon):", conditional_fireball("Dragon"))
    print("Conditional (Orc):", conditional_fireball("Orc"))   
    print("Sequence spell:", sequence_spell("Dragon"))  


main()