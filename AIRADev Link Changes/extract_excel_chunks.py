import pandas as pd
import io
from typing import List, Dict, Union

def dataframe_to_markdown(df: pd.DataFrame, max_rows: int = 50) -> str:
    """
    Convert a DataFrame (or a slice) to Markdown table text.
    Caps output rows to keep prompts small.
    """
    if len(df) > max_rows:
        df = df.head(max_rows)
    buf = io.StringIO()
    df.to_markdown(buf, index=False)
    return buf.getvalue()

def extract_excel_chunks(
        file_path: str,
        chunk_size: int = 200,
        include_sheet_names: bool = True
    ) -> List[Dict[str, Union[str, int]]]:
    chunks: List[Dict[str, str]] = []
    # pandas automatically chooses engine: openpyxl (xlsx) or xlrd (xls)
    xls = pd.ExcelFile(file_path)

    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        if df.empty:
            continue

        # Reset index so row numbers start at 1 (Excel‑style)
        df.reset_index(drop=True, inplace=True)
        total_rows = len(df)

        for i in range(0, total_rows, chunk_size):
            df_slice = df.iloc[i : i + chunk_size]
            row_start = i + 1
            row_end = min(i + chunk_size, total_rows)
            markdown_tbl = dataframe_to_markdown(df_slice)

            # build chunk text
            if include_sheet_names:
                content = f"### Sheet: {sheet_name}\n### Rows: {row_start}-{row_end}\n\n{markdown_tbl}"
            else:
                content = markdown_tbl

            chunks.append({
                "content": content,
                "sheet": sheet_name,
                "row_range": f"{row_start}-{row_end}"
            })

    return chunks
