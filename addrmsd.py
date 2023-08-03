class DataManipulator:
    def __init__(self, traceback_file, i_rmsd_file):
        self.traceback_file = traceback_file
        self.i_rmsd_file = i_rmsd_file

    def extract_numbers_from_traceback(self):
        numbers = []
        with open(self.traceback_file) as file:
            for line in file:
                if line.strip().startswith("complex"):
                    continue  # Skip the header row
                columns = line.strip().split()
                if len(columns) >= 6:
                   number = columns[5]
                   if number.isdigit():
                       numbers.append(number)
                else:
                    print(f"Warning: Skipping line due to insufficient columns: {line.strip()}")
        return numbers


  

    def update_traceback_with_rmsd(self, output_file, rmsd_values):
        with open(self.traceback_file) as infile, open(output_file, "w") as outfile:
            for _ in range(7):
                outfile.write(next(infile))
            for line, rmsd in zip(infile, rmsd_values):
                line = line.strip() + f"\t{rmsd}\n"
                outfile.write(line)
      

if __name__ == "__main__":
    traceback_file = "/Users/H/Desktop/Red_Sky/ensemble_477/traceback.list"
    i_rmsd_file = "/Users/H/Desktop/Red_Sky/ensemble_477/structures/it1/water/i-RMSD.dat"
    output_file = "/Users/H/Desktop/Red_Sky/ensemble_477/updated_traceback.list"

    data_manipulator = DataManipulator(traceback_file, i_rmsd_file)

    with open(i_rmsd_file) as rmsd_file:
        rmsd_values = [float(line.strip().split()[1]) for line in rmsd_file if not line.startswith("#")]

    data_manipulator.update_traceback_with_rmsd(output_file,rmsd_values)
