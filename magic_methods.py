from dataclasses import dataclass


@dataclass
class Attr:

    name: str
    x: str = ''

    def __str__(self):
        return self.x

    def __ne__(self, other):
        self.x = f"{self.name.lower()} ne '{other}'"
        return self

    def __eq__(self, other):
        try:
            iter(other)
        except TypeError:
            other = [other]

        eqs = [f"{self.name.lower()} eq '{i}'" for i in other]
        self.x = f'({" or ".join(eqs)})'
        return self

    def __and__(self, other):
        if not isinstance(other, Attr):
            raise NotImplementedError

        x = f'{self.x} and {other.x}'
        return Attr('-and-', x)


STATES = ['Running', 'AssignedToPool', 'AssignedToAgent', 'PreProcessing', 'WaitingForRemoteSolver']
source = Attr('source')
status = Attr('status')
# ===================================================== #
result = (source != 'production') & (status == STATES)
# ===================================================== #
print(result)
