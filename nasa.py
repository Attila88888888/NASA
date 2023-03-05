import csv


def most_frequents(l):
    frequency = []
    for i in range(13):
        frequency.append(l.count(str(i)))
    print(f'A leggyakoribb születési hónap: {frequency.index(sorted(frequency)[-1])}. '
          f'{round(l.count(str(frequency.index(sorted(frequency)[-1]))) / len(l) * 100, 1)}%')
    print(f'A 2. leggyakoribb születési hónap: {frequency.index(sorted(frequency)[-2])}. '
          f'{round(l.count(str(frequency.index(sorted(frequency)[-2]))) / len(l) * 100, 1)}%')
    print(f'A 3. leggyakoribb születési hónap: {frequency.index(sorted(frequency)[-3])}. '
          f'{round(l.count(str(frequency.index(sorted(frequency)[-3]))) / len(l) * 100, 1)}%')


def main():
    with open("astronauts.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        months = []
        for line in csv_reader:
            months.append(line[-1].split("/")[0])
        most_frequents(months)


main()
