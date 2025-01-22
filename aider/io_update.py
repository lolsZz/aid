"""Temporary file containing updates to be merged into io.py"""

from prompt_toolkit.styles import merge_styles
from .dyslexic_support import DyslexicFriendlyIO

# Code to be inserted after InputOutput.__init__ parameter list:
"""
        self.dyslexic_friendly = dyslexic_friendly
        if self.dyslexic_friendly:
            self.dyslexic_io = DyslexicFriendlyIO()
            # Override colors with dyslexic-friendly ones
            colors = self.dyslexic_io.DYSLEXIC_COLORS
            self.user_input_color = colors['user_input']
            self.tool_output_color = colors['tool_output']
            self.tool_error_color = colors['error']
            self.tool_warning_color = colors['warning']
            self.completion_menu_bg_color = colors['background']
"""

# Code to be inserted in _get_style method:
"""
        if self.dyslexic_friendly:
            dyslexic_style = self.dyslexic_io.style
            style_dict = merge_styles([Style.from_dict(style_dict), dyslexic_style])
"""

# Code to be inserted in assistant_output method before console.print:
"""
        if self.dyslexic_friendly:
            show_resp = self.dyslexic_io.format_text(message)
"""

# Code to be inserted in tool_output method:
"""
        if self.dyslexic_friendly and isinstance(message, str):
            message = self.dyslexic_io.format_text(message, role='tool')
"""