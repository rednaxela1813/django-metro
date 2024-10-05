import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from metro.models import Product, Supliers, Factura

class Command(BaseCommand):
    help = 'Load products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be loaded')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, encoding='ISO-8859-2') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            current_factura = None

            for row in reader:
                if row[0] == 'HDR':  # Assuming 'HDR' indicates the header row for suppliers
                    factura_number = row[1]
                    factura_date = row[2]
                    try:
                        factura_date = datetime.strptime(factura_date, '%d.%m.%Y').strftime('%Y-%m-%d')
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f"Invalid date format: {factura_date}"))
                        continue

                    sup_name = row[3]
                    ulica = row[5]
                    zip_code = row[6]
                    city = row[7]
                    ICDPH = row[9]

                    # Check if the supplier already exists
                    supplier = Supliers.objects.filter(
                        sup_name=sup_name,
                        ICDPH=ICDPH,
                        ulica=ulica
                    ).first()

                    if not supplier:
                        # Create the supplier if it doesn't exist
                        supplier = Supliers.objects.create(
                            sup_name=sup_name,
                            ICDPH=ICDPH,
                            ulica=ulica,
                            zip_code=zip_code,
                            city=city
                        )

                    # Check if the factura already exists
                    current_factura = Factura.objects.filter(
                        factura_number=factura_number
                    ).first()

                    if current_factura:
                        self.stdout.write(self.style.WARNING(f"Factura {factura_number} already exists. Skipping products for this factura."))
                        continue

                    # Create a new factura if it doesn't exist
                    current_factura = Factura.objects.create(
                        factura_number=factura_number,
                        factura_date=factura_date,
                        supliers=supplier,
                    )

                elif row[0] == 'LIN':  # Assuming 'LIN' indicates a product line
                    if current_factura is None:
                        self.stdout.write(self.style.ERROR('Factura must be created before products'))
                        continue

                    product_code = row[2]
                    product_price = float(row[6])
                    product_name = row[13]
                    quantity = int(row[5])
                    unit_price = float(row[11])
                    product_dph = float(row[9])
                    dph = int(row[12])

                    # Create the product in the database
                    Product.objects.create(
                        product_code=product_code,
                        product_name=product_name,
                        product_price=product_price,
                        quantity=quantity,
                        unit_price=unit_price,
                        product_dph=product_dph,
                        dph=dph,
                        factura=current_factura  # Set the factura instance
                    )
