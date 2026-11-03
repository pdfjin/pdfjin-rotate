from pathlib import Path
from typing import Union, BinaryIO, Optional
import io
import pikepdf


def rotate_pdf(
    input_pdf: Union[str, Path, bytes, BinaryIO],
    angle: int = 90,
    output: Optional[Union[str, Path, BinaryIO]] = None,
) -> Union[bytes, Path]:
    """
    Rotate all pages in a PDF document by angle (degrees, clockwise).
    """
    if isinstance(input_pdf, (str, Path)):
        src = pikepdf.open(str(input_pdf))
    elif isinstance(input_pdf, bytes):
        src = pikepdf.open(io.BytesIO(input_pdf))
    else:
        src = pikepdf.open(input_pdf)

    with src:
        for page in src.pages:
            page.rotate(angle, relative=True)

        if output is None:
            buf = io.BytesIO()
            src.save(buf)
            return buf.getvalue()

        if isinstance(output, (str, Path)):
            out_path = Path(output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            src.save(str(out_path))
            return out_path

        src.save(output)
        return output
