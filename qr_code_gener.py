import qrcode
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# Step 1: Load the CSV file
df = pd.read_csv('text_test.csv', sep=';')

# Step 2: Clean and split the 'Text' column into Plate Number and QR Code Title
df[['Plate Number', 'QR Code Title']] = df['Text'].str.split(',', expand=True)

# Step 3: Save the dataframe into an Excel file to work with it
excel_file = 'text_test_with_qrcodes.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

# Step 4: Load the workbook and the worksheet
wb = load_workbook(excel_file)
ws = wb.active

# Step 5: Adjust column width for the QR code column (C) and row height
ws.column_dimensions['C'].width = 20  # Set the column width to accommodate the QR codes

# Step 6: Generate QR codes and insert them into the Excel sheet
for index, row in df.iterrows():
    plate_number = row['Plate Number']
    
    # Generate a QR code for each plate number
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,  # Set smaller box size for QR code to fit
        border=2,    # Adjust the border size
    )
    
    qr.add_data(plate_number)
    qr.make(fit=True)
    
    # Create the QR code image
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the QR code image to a file (temporarily)
    qr_code_path = f"{plate_number}.png"
    img.save(qr_code_path)
    
    # Insert the QR code image into the Excel file (e.g., in column 'C')
    img_in_excel = Image(qr_code_path)

    # Set the image size to fit within the cell
    img_in_excel.width = 64  # Set width (adjust as needed)
    img_in_excel.height = 64  # Set height (adjust as needed)

    # Adjust the row height to fit the QR code
    ws.row_dimensions[index + 2].height = 50  # Adjust row height to fit the QR code

    # Insert the image into the specific cell (column C)
    ws.add_image(img_in_excel, f'C{index + 2}')  # Adjust row index (start from row 2)

# Step 7: Save the updated Excel file with QR codes
wb.save(excel_file)

print("QR codes have been successfully inserted and aligned into the Excel file.")
