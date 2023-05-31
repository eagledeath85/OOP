# An interface is like an abstract class, except it contains only abstract methods
# An interface contains no implementation details, it contains only the definition of methods
# And raise the NotImplementedError inside every single one of those methods

class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError("You must implement compile_code().")

    def execute_code(self):
        raise NotImplementedError("You must implement execute_code().")


# As GoCode implements the RunCodeInterface, it must implement all the abstract methods of RunCodeInterface.
# However, it can also implement some other concrete methods as well
class GoCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Go code")

    def execute_code(self):
        print("Execute Go code")


class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Java code")

    def execute_code(self):
        print("Execute Java code")

    def test(self):
        print("test")


def run_code(code: RunCodeInterface):
    code.compile_code()
    code.execute_code()


java = JavaCode()
run_code(java)


