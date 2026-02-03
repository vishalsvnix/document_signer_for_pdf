__version__ = '0.0.1'

try:
    from document_signer_for_pdf.document_signer_for_pdfs.patches import pdf
except ImportError:
    # Dependencies not yet installed (during bench build)
    pass
