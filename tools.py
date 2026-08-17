from langchain_core.tools import tool



@tool
def calculate_stress(force, area):
    """Calculate the stress given force and area. it returns the stress in megapascals (MPa)."""
    stress= force / area
    return stress


@tool
def calculate_factor_of_safety(yield_strength, working_stress):
    """Calculate the factor of safety given yield strength and working stress."""
    factor_of_safety = yield_strength / working_stress
    return factor_of_safety

@tool
def convert_mm_to_inches(mm):
    """Convert millimeters to inches."""
    inches = mm * 0.0393701
    return inches


@tool
def convert_Mpa_to_psi(Mpa):
    """Convert megapascals to pounds per square inch."""
    psi =   Mpa * 145.038
    return psi


@tool
def convert_kg_to_lbs(kg):
    """Convert kilograms to pounds."""
    lbs = kg * 2.20462
    return lbs



@tool
def lookup_material(name):
    """Lookup material properties by name. Returns a dictionary with density and yield strength."""
    materials = {
        "steel": {"density": 7850, "yield_strength": 250},
        "aluminum": {"density": 2700, "yield_strength": 55},
        "copper": {"density": 8960, "yield_strength": 70},
        "titanium": {"density": 4500, "yield_strength": 140},
        "brass": {"density": 8500, "yield_strength": 200},
        "zinc": {"density": 7130, "yield_strength": 110},
        "magnesium": {"density": 1740, "yield_strength": 95},
        "nickel": {"density": 8900, "yield_strength": 150},
        "bronze": {"density": 8800, "yield_strength": 200},
        "lead": {"density": 11340, "yield_strength": 18},   

    }
    return materials[name]
