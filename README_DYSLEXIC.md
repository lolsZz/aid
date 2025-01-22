# Dyslexia-Friendly Features in Aider

Aider now includes comprehensive support for users with dyslexia, implementing research-based features to improve readability and reduce visual stress. These features can be enabled by adding the `--dyslexic-friendly` flag when starting Aider.

## Key Features

### 1. Optimized Color Scheme
- Light grey background to reduce white glare
- Dark grey text instead of pure black for reduced contrast
- Carefully selected colors for different message types:
  - Navy blue for user input
  - Dark green for tool output
  - Dark red for errors
  - Dark orange for warnings

### 2. Typography Improvements
- Increased letter spacing (1.2x normal)
- Larger line height (1.5x)
- Clear paragraph separation
- Consistent left alignment
- Support for OpenDyslexic font (when available)

### 3. Advanced Reading Aids
- Bionic Reading format (toggle with Ctrl+B) - highlights word beginnings for faster recognition
- Customizable Rhythm Markers (toggle with Ctrl+R) - adds visual guides for text tracking
- Smart Word Chunking - breaks text into manageable groups
- Adjustable Animation Speed (Ctrl+Up/Down) - customize text transition effects
- Reading Guide feature (toggle with Ctrl+G)
- Reading Guide feature (toggle with Ctrl+G)
- Text-to-Speech support for code (toggle with Ctrl+T)
- Smart code narration with symbol explanation
- Visual focus assistance

### 4. Text Formatting
- Enhanced spacing between characters
- Clear visual separation between different types of content
- Improved readability of code blocks
- Optimized completion menu visibility

## Usage

To enable dyslexia-friendly features:

```bash
aider --dyslexic-friendly
```

## Terminal Configuration

For the best experience, configure your terminal with these recommended settings:

- Font: OpenDyslexic (or Verdana/Arial as alternatives)
- Font Size: 14pt or larger
- Line Spacing: 1.5x
- Paragraph Spacing: 2.0x

## Research Background

These features are based on established research on improving text readability for users with dyslexia:

1. Increased letter spacing reduces letter confusion and improves reading speed
2. Careful color selection reduces visual stress
3. Clear visual hierarchy helps with content navigation
4. Consistent formatting reduces cognitive load

## Feedback

We welcome feedback from users with dyslexia to help us further improve these features. Please submit issues or suggestions through our GitHub repository.