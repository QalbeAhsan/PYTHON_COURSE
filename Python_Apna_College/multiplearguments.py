class Details:  # FOR TAKING MULTIPLE ARGUMENTS
    def __init__(self, *args):
        self.args = args  # Store all arguments in self.args

    def name(self):
        print(
            f"name: {self.args[0]}\n age: {self.args[1]}\n designation: {self.args[2]}\n address: {self.args[3]}"
        )


class detail(Details):  # Inheritance
    info = Details("ahsan", 14, "developer", "lodhran")  # manually put arguments by input from user
    info.name() #no comment
