"""
Edit a pose for Lilypond maarkup
"""

class Pose:

    def __init__(self):

        self.xy_resolution = 9
        self.beta_resolution = 8
        self.size = 0.6
        self.unloaded = 4
        self.loaded = 9

        # here positions and orientation are float, in [m] and [deg]
        self.feet = {"ll": {"x": -0.1,
                            "y": 0.1,
                            "b": 0,
                            "w": self.unloaded},
                     "lr": {"x": -0.1,
                            "y": 0.1,
                            "b": 0,
                            "w": self.loaded},
                     "fl": {"x": -0.1,
                            "y": 0.1,
                            "b": 0,
                            "w": self.loaded},
                     "fr": {"x": -0.1,
                            "y": 0.1,
                            "b": 0,
                            "w": self.unloaded}
                     }

        self.duration = "1  "

    def to_start_pose_bt(self):

        self.feet = {"ll": {"x": -0.1,
                            "y": 0.1,
                            "b": 0,
                            "w": self.unloaded},
                     "lr": {"x": -0.1,
                            "y": -0.1,
                            "b": 0,
                            "w": self.loaded},
                     "fl": {"x": 0.1,
                            "y": -0.1,
                            "b": 180,
                            "w": self.loaded},
                     "fr": {"x": 0.1,
                            "y": 0.1,
                            "b": 180,
                            "w": self.unloaded}
                     }

    def to_start_pose_lr(self):
        track_width = 0.035
        self.feet = {"ll": {"x": -0.1,
                            "y": track_width,
                            "b": 270,
                            "w": self.unloaded},
                     "lr": {"x": -0.1,
                            "y": -track_width,
                            "b": 270,
                            "w": self.loaded},
                     "fl": {"x": 0.1,
                            "y": -track_width,
                            "b": 90,
                            "w": self.loaded},
                     "fr": {"x": 0.1,
                            "y": track_width,
                            "b": 90,
                            "w": self.unloaded}
                     }

    def re_center(self):

        com_x = sum([self.feet[foot]["x"] for foot in self.feet.keys()])/4.  # center of mass
        com_y = sum([self.feet[foot]["y"] for foot in self.feet.keys()])/4.

        for foot in self.feet.keys():
            self.feet[foot]["x"] = self.feet[foot]["x"] + com_x
            self.feet[foot]["y"] = self.feet[foot]["y"] + com_y



    def print_pose(self):

        print(self.feet)

    def set_duration(self, duration):

        self.duration = duration

    def to_lilypond(self):

        grid_size = self.size / self.xy_resolution
        to_hex_string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' ]

        for foot in self.feet.keys():
            self.feet[foot]["c_x"] = int(round(self.feet[foot]["x"] / grid_size +  self.xy_resolution/2))
            self.feet[foot]["c_y"] = int(round(self.feet[foot]["y"] / grid_size +  self.xy_resolution/2))
            self.feet[foot]["c_b"] = int(round(self.feet[foot]["b"] / 359. * self.beta_resolution))

        lilypond_str_args = []
        for foot in ["ll", "lr", "fl", "fr"]:
            for attr in ["c_x", "c_y", "c_b", "w"]:
                lilypond_str_args.append(to_hex_string[self.feet[foot][attr]])
        lilypond_str = "ll %s%s%s%s lr %s%s%s%s fl %s%s%s%s fr %s%s%s%s dur "%tuple(lilypond_str_args) + self.duration

        print(lilypond_str)

    def hello_world(self):
        print('hello world')

    def right_step(self):
        pass

if __name__ == '__main__':

    pose = Pose()
    pose.to_start_pose_lr()
    pose.re_center()
    pose.to_lilypond()
    pose.right_step()