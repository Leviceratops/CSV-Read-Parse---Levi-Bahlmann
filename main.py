import csv, random

try: 

    with open('dndstats.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open('dndbackgrounds.csv', 'w') as new_file:
            column_names = ['Character Name', 'Class', 'Race', 'Campaign Name']

            csv_writer = csv.DictWriter(new_file, fieldnames=column_names, delimiter=';')
    
            csv_writer.writeheader()

            for line in csv_reader:
                random_list = ["Curse of Strahd", "Out of the Abyss", "Storm Kings Thunder", "Tomb of Annihilation"]
                parsed_line = {'Character Name': line['Character Name'], 'Class': line['Class'],'Race': line['Race'], 'Campaign Name': random.choice(random_list)}

                csv_writer.writerow(parsed_line)

except IOError:
	print("I/O error --> Check your file names!")

else:
	print('Character background check complete!')
  
finally:
  print("Goodbye.")
    