import re

def get_foods():
    foods = []
    with open("day21.txt") as f:
        for line in f:
            tokens = re.findall(r"\w+", line)
            if len(tokens) == 0:
                continue
            i = tokens.index("contains")
            ingreeds = set(tokens[:i])
            allergens = set(tokens[i + 1:])
            foods.append((ingreeds, allergens))
    return foods


def get_allergen_src(foods):
    # find all possible ingredients that each allergen could be
    allergen_candidates = {}
    for ingreeds, allergens in foods:
        for allergen in allergens:
            if allergen in allergen_candidates:
                allergen_candidates[allergen] &= ingreeds
            else:
                allergen_candidates[allergen] = set(ingreeds)
    # find exact ingredient for each
    allergen_src = {}
    while len(allergen_candidates) > 0:
        # find allergens with one possible ingredient
        found = {}
        for allergen, candidates in allergen_candidates.items():
            if len(candidates) == 1:
                ingreed = tuple(candidates)[0]
                found[allergen] = ingreed
        # update found allergens and ingredients
        allergen_src.update(found)
        for allergen in found:
            allergen_candidates.pop(allergen)
        ingreeds = set(found.values())
        for candidates in allergen_candidates.values():
            candidates -= ingreeds
    return allergen_src


def part1():
    foods = get_foods()
    allergen_src = get_allergen_src(foods)
    # count ingredients without allergens
    count = 0
    allergen_names = set(allergen_src.values())
    for ingreeds, _ in foods:
        count += sum(1 for x in ingreeds if x not in allergen_names)
    print(allergen_src)
    return count


def part2():
    foods = get_foods()
    allergen_src = get_allergen_src(foods)
    # get allergens in alphabetical order
    allergens = sorted(allergen_src.items())
    return ",".join(x[1] for x in allergens)


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
