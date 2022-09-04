
class Navigation:
    def __init__(self, navigation_data):
        # define horizontal and depth position of sub
        self.navigation_data = navigation_data
        self.horizontal_pos = 0
        self.depth_pos = 0
        self.aim = 0

        for line in self.navigation_data:
            if line.startswith("forward"):
                value = ""
                for m in line:
                    if m.isdigit():
                        value = value + m
                self.change_aim(int(value), "forward")

            if line.startswith("up"):
                value = ""
                for m in line:
                    if m.isdigit():
                        value = value + m
                self.change_aim(int(value), "up")

            if line.startswith("down"):
                value = ""
                for m in line:
                    if m.isdigit():
                        value = value + m
                self.change_aim(int(value), "down")

    # Increase/decrease horizontal
    def change_horizontal(self, value):
        self.horizontal_pos += value
        return

    # increase/decrease depth
    def change_depth(self, value):
        self.depth_pos += value
        return

    # calculate final position
    def final_pos(self):
        return f"The final position is - Horizontal: " \
               f"{self.horizontal_pos} Depth: {self.depth_pos}" \
               f"\nFinal Position: {self.horizontal_pos * self.depth_pos}"

    # change the aim
    def change_aim(self, value, position):
        match position:

            case "forward":
                self.change_horizontal(value)
                self.change_depth(self.aim * value)

            case "up":
                self.aim += (value * -1)

            case "down":
                self.aim += value


with open("resources/navigation report", "r") as f:
    lines = f.readlines()
    data = [position.strip() for position in lines]
    current_pos = Navigation(navigation_data=data)
    print(current_pos.final_pos())
