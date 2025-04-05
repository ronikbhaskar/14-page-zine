"""
While this was intented only for making 14-page zines,
this can easily be extended to 8-page and other formats.
"""

import pymupdf

LETTER_WIDTH = 612 # 8.5 inches in points
LETTER_HEIGHT = 792 # 11 inches in points

def create_pdf_grid(
    input_pdf_path,
    output_pdf_path,
    page_map,
    rotate_flags=None,
    grid_size=(4, 4),
    page_width=LETTER_WIDTH,
    page_height=LETTER_HEIGHT,
    draw_dots=True
):
    """
    Given some input pdf at input_pdf_path,
    take the pages and arrange them onto a grid on a single sheet.

    Ideally for single-sheet zines
    """
    input_pdf = pymupdf.open(input_pdf_path)
    output_pdf = pymupdf.open()

    output_page = output_pdf.new_page(width=page_width, height=page_height)

    rows, cols = grid_size
    cell_width = page_width / cols
    cell_height = page_height / rows

    for idx, page_idx in enumerate(page_map):
        if page_idx is None:
            continue  # leave cell blank

        row = idx // cols
        col = idx % cols

        x0 = col * cell_width
        y0 = row * cell_height
        x1 = x0 + cell_width
        y1 = y0 + cell_height
        dest_rect = pymupdf.Rect(x0, y0, x1, y1)

        page = input_pdf.load_page(page_idx)
        if rotate_flags and rotate_flags[idx]:
            # rasterized, so sorry about the fidelity
            page.set_rotation(180)
            output_page.insert_image(dest_rect, pixmap=page.get_pixmap())
        else:
            output_page.show_pdf_page(dest_rect, input_pdf, page_idx)
        
    if draw_dots:
        for col in range(1, cols):
            for row in range(1, rows):
                output_page.draw_circle(
                    center=(col * cell_width, row * cell_height),
                    radius=0.5,
                    color=(0.8, 0.8, 0.8), # light grey
                    fill=(0.8, 0.8, 0.8), # light grey
                )
    
    output_pdf.save(output_pdf_path)
    output_pdf.close()
    input_pdf.close()

# create_pdf_grid(
#     "/Users/ronikbhaskar/Documents/Projects/14-page-zine/example-14-page.pdf",
#     "/Users/ronikbhaskar/Documents/Projects/14-page-zine/example-zine-with-cuts.pdf",
#     page_map=[12, 11, 10, 9, 13, None, 7, 8, 0, None, 6, 5, 1, 2, 3, 4],
#     rotate_flags=([True] * 4 + [False] * 4) * 2
# )