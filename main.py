import fitz

def merge_pdfs_fitz(pdf_list, output_pdf):
    merged_pdf = fitz.open()

    for pdf in pdf_list:
        doc = fitz.open(pdf)
        merged_pdf.insert_pdf(doc)

    merged_pdf.save(output_pdf)
    merged_pdf.close()
    print(f"Đã gộp các file PDF thành {output_pdf}")

# Ví dụ: Gộp 3 file PDF
merge_pdfs_fitz(["C:\workspace\pythonn-project-only\Gop-file\ile_1.pdf", "C:\workspace\pythonn-project-only\Gop-file\ile_2.pdf", "C:\workspace\pythonn-project-only\Gop-file\ile_3.pdf","C:\workspace\pythonn-project-only\Gop-file\ile_4.pdf","C:\workspace\pythonn-project-only\Gop-file\ile_5.pdf"], "final.pdf")


# # Ví dụ: Gộp 3 file PDF
# merge_pdfs(["C:\workspace\pythonn-project-only\Gộp-file\file_1.pdf", "C:\workspace\pythonn-project-only\Gộp-file\file_2.pdf", "C:\workspace\pythonn-project-only\Gộp-file\file_3.pdf","C:\workspace\pythonn-project-only\Gộp-file\file_4.pdf","C:\workspace\pythonn-project-only\Gộp-file\file_5.pdf"], "final.pdf")
