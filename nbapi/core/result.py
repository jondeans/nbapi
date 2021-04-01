"""Basic Results class functionality."""


class Result:

    _frame = None

    def to_csv(self, filename=None):
        self._frame.to_csv(filename)

    def get_frame(self):
        return self._frame
