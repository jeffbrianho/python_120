class Cat:
    _total_cats = 0

    def __init__(self, name):
        self._name = name
        self.__class__._total_cats += 1
    
    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    def jump(self):
        return f'{self.name} is jumping!'

    @classmethod
    def total_cats(cls):
        return cls._total_cats

mitzi = Cat('Mitzi')
print(mitzi.jump())                  # Mitzi is jumping!
print(Cat.total_cats())                # 1
print(f"The cat's name is {mitzi}")  # The cat's name is Mitzi

fluffy = Cat('Fluffy')
print(Cat.total_cats())               # 2