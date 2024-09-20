class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if owner:
            owner.add_pet(self)
        
        Pet.all.append(self)

    def __repr__(self):
        return f"{self.name} ({self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only Pet instances can be added.")
        self._pets.append(pet)
        pet.owner = self

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return self.name
