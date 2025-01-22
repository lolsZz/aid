"""
Dyslexia-friendly terminal interface improvements for Aider.

This module provides specialized settings and utilities to make Aider more
accessible for users with dyslexia, implementing research-based recommendations
for improving readability.
"""

from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.formatted_text import FormattedText
import pyttsx3
import threading
import re
from dataclasses import dataclass
from typing import List, Dict, Optional
import time

class DyslexicFriendlyIO:
    """
    Enhanced IO handling with dyslexia-friendly features.
    Implements recommendations from typography research for dyslexic readers.
    """
    
    # Default color scheme optimized for dyslexic users
    # Using high contrast colors that are easier to distinguish
    DYSLEXIC_COLORS = {
        'background': '#F2F2F2',  # Light grey background reduces white glare
        'text': '#2E2E2E',       # Dark grey text - softer than pure black
        'user_input': '#006699',  # Navy blue - high contrast but not harsh
        'tool_output': '#2E5B1F', # Dark green - distinctive but gentle
        'error': '#CC0000',      # Dark red - clear but not aggressive
        'warning': '#B35900',    # Dark orange - clear but warm
    }

    # Character spacing multiplier for improved readability
    LETTER_SPACING = 1.2
    
    # Default rhythm marker settings
    RHYTHM_MARKER_INTERVAL = 4  # Words between markers
    RHYTHM_MARKER_COLOR = "rgba(0, 0, 255, 0.1)"  # Subtle blue
    
    # Animation settings
    DEFAULT_ANIMATION_SPEED = 1.0
    
    # Word chunking settings
    MAX_CHUNK_SIZE = 4  # Maximum words per chunk
    PAUSE_BETWEEN_CHUNKS = 0.2  # seconds
    
    def __init__(self):
        self.style = self._create_dyslexic_style()
        self.current_line = 0
        self.reading_guide_active = False
        self.rhythm_markers_active = False
        self.bionic_reading_active = True  # Enable by default
        self.animation_speed = self.DEFAULT_ANIMATION_SPEED
        self.tts_engine = None
        self._initialize_tts()
        self.last_chunk_time = time.time()

    def _initialize_tts(self):
        """Initialize text-to-speech engine in a separate thread."""
        try:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', 150)  # Slightly slower than default
            self.tts_engine.setProperty('volume', 0.9)
        except Exception:
            self.tts_engine = None  # Graceful fallback if TTS isn't available
        
    def _create_dyslexic_style(self):
        """
        Creates a prompt_toolkit style optimized for dyslexic users.
        Implements increased spacing and custom colors.
        """
        return Style.from_dict({
            '': f'bg:{self.DYSLEXIC_COLORS["background"]} {self.DYSLEXIC_COLORS["text"]}',
            'user-input': self.DYSLEXIC_COLORS["user_input"],
            'tool-output': self.DYSLEXIC_COLORS["tool_output"],
            'error': self.DYSLEXIC_COLORS["error"],
            'warning': self.DYSLEXIC_COLORS["warning"],
            'completion-menu': f'bg:{self.DYSLEXIC_COLORS["background"]}',
            'completion-menu.completion': f'bg:{self.DYSLEXIC_COLORS["background"]}',
            'completion-menu.completion.current': 'bg:#00A5FF #FFFFFF',
        })

    def format_text(self, text, role='normal', add_reading_guide=True):
        """
        Formats text with dyslexia-friendly styling including:
        - Increased letter and line spacing
        - Clear paragraph separation
        - Consistent left alignment
        - Reading guide (optional)
        - Text-to-speech for code blocks
        - Bionic reading format
        - Rhythm markers
        - Smart word chunking
        """
        # Process text through various enhancement methods
        enhanced_text = text
        
        if self.bionic_reading_active:
            enhanced_text = self._apply_bionic_reading(enhanced_text)
            
        if self.rhythm_markers_active:
            enhanced_text = self._add_rhythm_markers(enhanced_text)
            
        # Smart word chunking for better comprehension
        enhanced_text = self._apply_word_chunking(enhanced_text)
        
        # Add proper line height and paragraph spacing
        formatted_text = HTML(
            f'<div style="line-height: 1.5; margin-bottom: 1em; '
            f'letter-spacing: {self.LETTER_SPACING}em; '
            f'animation: fadeIn {self.animation_speed}s ease-in-out;">'
            f'{enhanced_text}</div>'
        )
        
        if role == 'code' and self.tts_engine:
            self._add_code_tts_controls(text)

        if add_reading_guide:
            formatted_text = self._add_reading_guide(formatted_text)

        return formatted_text

    def _add_reading_guide(self, text):
        """Add a subtle reading guide that helps track lines of text."""
        if not self.reading_guide_active:
            return text

        guide_style = f'background-color: rgba(255, 255, 0, 0.1);'
        guide_html = f'<div class="reading-guide" style="{guide_style}"></div>'
        
        return HTML(f'{guide_html}{text}')

    def _add_code_tts_controls(self, code_text):
        """Add text-to-speech controls for code blocks."""
        def speak_code():
            if self.tts_engine:
                # Format code for speech (add pauses, explain symbols)
                speech_text = self._format_code_for_speech(code_text)
                self.tts_engine.say(speech_text)
                self.tts_engine.runAndWait()

        # Run in separate thread to avoid blocking
        threading.Thread(target=speak_code, daemon=True).start()

    def _format_code_for_speech(self, code):
        """Format code for better text-to-speech output."""
        # Replace common symbols with spoken equivalents
        replacements = {
            '{': 'open brace',
            '}': 'close brace',
            '(': 'open parenthesis',
            ')': 'close parenthesis',
            '[': 'open bracket',
            ']': 'close bracket',
            '=': 'equals',
            '=>': 'arrow',
            ';': 'semicolon',
            '\n': ' new line ',
        }
        
        result = code
        for symbol, spoken in replacements.items():
            result = result.replace(symbol, f' {spoken} ')
            
        return result

    def _apply_bionic_reading(self, text):
        """Apply bionic reading format (bold first part of words)."""
        if not self.bionic_reading_active:
            return text
            
        words = text.split()
        processed_words = []
        
        for word in words:
            if len(word) <= 1:
                processed_words.append(word)
                continue
                
            # Calculate bold length (roughly first 40% of word)
            bold_length = max(1, int(len(word) * 0.4))
            bold_part = word[:bold_length]
            rest = word[bold_length:]
            
            processed_words.append(f'<b>{bold_part}</b>{rest}')
            
        return ' '.join(processed_words)
        
    def _add_rhythm_markers(self, text):
        """Add visual rhythm markers to help with text tracking."""
        if not self.rhythm_markers_active:
            return text
            
        words = text.split()
        marked_words = []
        
        for i, word in enumerate(words):
            if i % self.RHYTHM_MARKER_INTERVAL == 0:
                word = f'<span style="background-color: {self.RHYTHM_MARKER_COLOR}">{word}</span>'
            marked_words.append(word)
            
        return ' '.join(marked_words)
        
    def _apply_word_chunking(self, text):
        """Group words into small, manageable chunks with subtle visual separation."""
        words = text.split()
        chunks = []
        current_chunk = []
        
        for word in words:
            current_chunk.append(word)
            if len(current_chunk) >= self.MAX_CHUNK_SIZE:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                
                # Add timing-based pause between chunks
                current_time = time.time()
                if current_time - self.last_chunk_time >= self.PAUSE_BETWEEN_CHUNKS:
                    chunks.append('<span class="chunk-separator"> </span>')
                    self.last_chunk_time = current_time
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
            
        return ' '.join(chunks)
        
    def toggle_reading_guide(self):
        """Toggle the reading guide on/off."""
        self.reading_guide_active = not self.reading_guide_active
        return self.reading_guide_active
        
    def toggle_rhythm_markers(self):
        """Toggle rhythm markers on/off."""
        self.rhythm_markers_active = not self.rhythm_markers_active
        return self.rhythm_markers_active
        
    def toggle_bionic_reading(self):
        """Toggle bionic reading format on/off."""
        self.bionic_reading_active = not self.bionic_reading_active
        return self.bionic_reading_active
        
    def adjust_animation_speed(self, factor):
        """Adjust animation speed (0.5 = slower, 2.0 = faster)."""
        self.animation_speed = max(0.1, min(2.0, self.animation_speed * factor))

    def get_recommended_settings(self):
        """
        Returns a dictionary of recommended terminal settings for dyslexic users.
        These can be applied to the user's terminal emulator.
        """
        return {
            'font_family': 'OpenDyslexic, Verdana, Arial',
            'font_size': '14',
            'line_spacing': '1.5',
            'paragraph_spacing': '2.0',
            'colors': self.DYSLEXIC_COLORS,
        }