# 14-Page Zine

Takes a 14-page pdf and turns it into a single sheet, cut-and-fold zine. HBD

## Summary

At some point, I'll write a lengthy narrative about why I made this. Until then, long story short, formatting zines seems hard, and I like this 14-page layout.

## Setup

1. Install the necessary dependencies

```bash
pip install -r requirements.txt
```

that's it.

## Running the Formatter

As long as the input pdf has at least 14 pages, this will run.

```bash
python3 main.py -i input.pdf -o output.pdf
```

I have included an example of a 14-page pdf (`example-14-page.pdf`) and the corresponding single sheet zine (`example-zine.pdf`). I also included a reference for where to cut (`example-zine-with-cuts.pdf`).

## Notes about the Format

While the format uses 16 panels, two of those will never be seen, and those are the blank panels in the middle, vertically between panels 3 and 12. Given the exact constraints I wanted on the zine, any optimal solution would necessarily hide two panels. They don't bother you when you're flipping through the zine, so they can be safely ignored (or glued together).

