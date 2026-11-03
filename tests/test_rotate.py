import pytest
import io
import pikepdf
from pdfjin_rotate.core import rotate_pdf


def test_rotate_pdf():
    pdf = pikepdf.new()
    pdf.add_blank_page()
    buf = io.BytesIO()
    pdf.save(buf)

    rotated = rotate_pdf(buf.getvalue(), angle=90)
    with pikepdf.open(io.BytesIO(rotated)) as doc:
        assert doc.pages[0].Rotate == 90
