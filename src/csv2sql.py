import sys
import re

if (len(sys.argv) != 3):
    print "Uso: csv2sql input.csv output.sql"
else:
    input_file_path  = sys.argv[1]
    output_file_path = sys.argv[2]
    input_file  = open(input_file_path,  'r')
    output_file = open(output_file_path, 'w')

    # En el archivo csv, las columna son_
    # Pais,Ciudad,Codigo,Nombre

    pattern = re.compile(r'"(.*?)","(.*?)","(.*?)","(.*?)"')
    for line in input_file:
        match = pattern.search(line)
        if (match):
            Pais, Ciudad, Codigo, Nombre = match.groups()
            output_string = "insert into Aeropuertos (Codigo, Nombre, Pais, Ciudad) values (\"" + Codigo + "\", \"" + Nombre + "\", \"" + Pais + "\", \"" + Ciudad + "\");\n"
            output_file.write(output_string)
        else:
            print "Dropped line: ", line

    output_file.close()
    input_file.close()
