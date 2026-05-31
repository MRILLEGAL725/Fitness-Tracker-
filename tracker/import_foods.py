import csv

from tracker.models import FoodDatabase


CSV_FILE = "food_databse.csv"


with open(
    CSV_FILE,
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    count = 0

    for row in reader:

        try:

            FoodDatabase.objects.get_or_create(

                name=row["name"],

                defaults={

                    "calories":
                    float(row["calories"]),

                    "protein":
                    float(row["protein"]),

                    "carbs":
                    float(row["carbs"]),

                    "fat":
                    float(row["fat"]),

                    "fibre":
                    float(row["fibre"])
                }
            )

            count += 1

            if count % 100 == 0:

                print(
                    f"Imported {count} foods"
                )

        except Exception as e:

            print(e)

print("Import completed")