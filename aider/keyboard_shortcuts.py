"""Keyboard shortcuts for dyslexia-friendly features."""

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys

def create_dyslexic_friendly_bindings(io_instance):
    """Create keyboard shortcuts for dyslexia-friendly features."""
    kb = KeyBindings()

    @kb.add('c-g')  # Ctrl+G
    def _(event):
        """Toggle reading guide."""
        if io_instance.dyslexic_io:
            active = io_instance.dyslexic_io.toggle_reading_guide()
            status = "enabled" if active else "disabled"
            io_instance.tool_output(f"Reading guide {status}")

    @kb.add('c-r')  # Ctrl+R
    def _(event):
        """Toggle rhythm markers."""
        if io_instance.dyslexic_io:
            active = io_instance.dyslexic_io.toggle_rhythm_markers()
            status = "enabled" if active else "disabled"
            io_instance.tool_output(f"Rhythm markers {status}")
            
    @kb.add('c-b')  # Ctrl+B
    def _(event):
        """Toggle bionic reading format."""
        if io_instance.dyslexic_io:
            active = io_instance.dyslexic_io.toggle_bionic_reading()
            status = "enabled" if active else "disabled"
            io_instance.tool_output(f"Bionic reading {status}")
            
    @kb.add('c-up')  # Ctrl+Up
    def _(event):
        """Increase animation speed."""
        if io_instance.dyslexic_io:
            io_instance.dyslexic_io.adjust_animation_speed(1.2)
            io_instance.tool_output("Animation speed increased")
            
    @kb.add('c-down')  # Ctrl+Down
    def _(event):
        """Decrease animation speed."""
        if io_instance.dyslexic_io:
            io_instance.dyslexic_io.adjust_animation_speed(0.8)
            io_instance.tool_output("Animation speed decreased")
            
    @kb.add('c-t')  # Ctrl+T
    def _(event):
        """Toggle text-to-speech for current text."""
        if io_instance.dyslexic_io and io_instance.dyslexic_io.tts_engine:
            current_line = event.current_buffer.document.current_line
            io_instance.dyslexic_io.tts_engine.say(current_line)
            io_instance.dyslexic_io.tts_engine.runAndWait()

    return kb