from pathlib import Path

import pandas as pd

from openpyxl.worksheet.worksheet import Worksheet


def create_excel_report(findings_by_sheet, output_path):
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    # with keyword schließt den geöffneten writer automatisch
    # ExcelWriter nutz den übergebenen Pfad wo die Datei erstellt werden soll und verwaltet es
    # to_excel schreibt und erstellt die Blätter anahnd der DataFrame Instanz
    with pd.ExcelWriter(report_path, engine='openpyxl') as writer:
        for sheet_name, dataframe in findings_by_sheet.items():
            dataframe.to_excel(writer, sheet_name=sheet_name,
                               index=False)

            worksheet: Worksheet = writer.sheets[sheet_name]
            # A1 also die Überschirft geht beim Scrollen mit
            worksheet.freeze_panes = "A2"
            worksheet.auto_filter.ref = worksheet.dimensions

            # Sammlung der Spalte (A1-An) dann 2 Iteration (B1-Bn)
            for column in worksheet.columns:
                max_length = 0
                # Beginne in der ersten Zelle der Spaltenmenge(A1-An) ,erste interation "A1", dann "B1"
                column_letter = column[0].column_letter
                # Zelle in Spalte die nicht leer, übernehme die Länge des Inhalts und setze es als neues maximum
                for cell in column:
                    if cell.value is not None:
                        cell_length = len(str(cell.value))

                        if cell_length > max_length:
                            max_length = cell_length
                # großtes maximum der Spalte wird übernommen
                worksheet.column_dimensions[column_letter].width = max_length + 4

    return report_path
