from typing import Callable, TypeVar

T = TypeVar('T')


class LineArgument:
    """
    Represents a single program argument. (--path)
    @param name: The name of the argument.  (path)
    @param value: The value of the argument. (~/Documents)
    @param prompt: To be given in the use case's __init__.
    @param confirm: To be given in the use case's __init__.
    """

    def __init__(self,
                 name: str,
                 value: T = None,
                 prompt: Callable[[str], T] = None,
                 confirm: Callable[[T], bool] = None,
                 is_confirmed: bool = False):
        self.name = name
        self.value = value
        self.prompt = prompt
        self.confirm = confirm
        self.is_confirmed = is_confirmed

    def set_prompts(self, *, prompt: Callable[[str], T],
                    confirm: Callable[[T], bool]):
        self.prompt = prompt
        self.confirm = confirm

    def __repr__(self):
        repr = f"{self.name}: {self.value}, "
        repr += f"{'prompt good' if self.prompt else 'prompt missing'}, "
        repr += f"{'confirm good' if self.prompt else 'confirm missing'}, "
        repr += f"{'GO' if self.is_confirmed else 'NO GO'})"
        return repr


class CommandArgs:
    """
    MrwArguments will have arguments passed from command line as a dictionary.
    """

    def __init__(self, *args: LineArgument):
        self.args = {arg.name: arg for arg in args}

    def __getitem__(self, name: str):
        return self.args.get(name)

    def arg_values(self):
        return self.args.values()

    def is_confirmed(self, name: str = None) -> bool:
        """
        Check if a specific argument or all arguments have been confirmed.
        """
        if name:
            return (self.args.get(name).is_confirmed
                    if name in self.args else False)
        return all(arg.is_confirmed for arg in self.args.values())

    def __repr__(self):
        repr = "MrwArguments(\n"
        for arg in self.args.values():
            repr += f"    {arg.__repr__()}\n"
        repr += ")"
        return repr