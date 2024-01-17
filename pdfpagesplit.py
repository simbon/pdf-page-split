from pypdf import PdfReader, PdfWriter, Transformation, PaperSize
import io

# Open the PDF "input.pdf" whose pages you want to split in half
with open("input.pdf", "rb") as file:
    reader = PdfReader(file)
    writer = PdfWriter()
    
    # Iterate the splitting on every page
    for p in range(len(reader.pages)):
        # Get the left half
        pageleft = reader.pages[p]
        pageleft.mediabox.upper_right = (
            pageleft.mediabox.right / 2,
            pageleft.mediabox.top,
        )
        writer.add_page(pageleft)

        # Create a new reader to process the same original page
        file.seek(0)
        new_reader = PdfReader(file)
        pageright = new_reader.pages[p]
        
        # Get the right half
        pageright.mediabox.lower_left = (
            pageright.mediabox.right / 2,
            pageright.mediabox.bottom,
        )

        pageright.mediabox.upper_right = (
        pageright.mediabox.right,
        pageright.mediabox.top,
        )
        
        writer.add_page(pageright)

    # Write the new PDF as output.pdf
    with open("output.pdf", "wb") as output_file:
        writer.write(output_file)
