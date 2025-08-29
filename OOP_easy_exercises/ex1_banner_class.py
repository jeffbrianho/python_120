# Banner Class

# Behold this incomplete class for constructing boxed banners:


class Banner:
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"| {' ' * len(self._message)} |"

    def _horizontal_rule(self):
        return f"+-{'-' * len(self._message)}-+"

    def _message_line(self):
        return f"| {self._message} |"
    
# Complete this class so that the test cases shown below work as intended. You are free to add 
# any methods or instance variables you need. However, methods prefixed with an underscore are
#  intended for internal use and should not be called externally.

# You may assume that the input will always fit in your terminal window.\

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+