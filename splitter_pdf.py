from PyPDF2 import PdfReader, PdfWriter
import sys
import os
from tkinter import simpledialog, Tk

def extract_pages(file_path, page_selection):
    reader = PdfReader(file_path)
    writer = PdfWriter()

    # Parse of the selection
    pages_to_keep = []
    for part in page_selection.split(','):
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            pages_to_keep.extend(range(int(start), int(end) + 1))
        else:
            pages_to_keep.append(int(part))

    # Index correction (0-based to 1-based)
    for page_num in pages_to_keep:
        if 1 <= page_num <= len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])
        else:
            print(f"{page_num} doesn't exist in the document.")

    # Name output file
    base_name, ext = os.path.splitext(file_path)
    safe_selection = page_selection.replace(',', '_').replace('-', 'à')
    output_filename = f"{base_name}_pages_{safe_selection}{ext}"

    # Writing of the file
    with open(output_filename, "wb") as f_out:
        writer.write(f_out)

    print(f"extract PDF saved : {output_filename}")
    print(f"Pages kept : {pages_to_keep}")

def main():
    if len(sys.argv) != 2:
        print("Usage: split_pdf.py <path>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Tkinter page selection dialog
    root = Tk()
    root.withdraw()  # hide the main window
    page_selection = simpledialog.askstring("Split PDF", f"Enter pages to extract from:\n{os.path.basename(file_path)}\nEx: 1-3,5,7")

    if page_selection:
        extract_pages(file_path, page_selection)
    else:
        print("No pages entered.")

if __name__ == "__main__":
    main()
