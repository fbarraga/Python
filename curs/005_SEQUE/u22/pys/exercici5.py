filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
def tiene_extension(filename,extension):
    nombre=filename
    if nombre[len(nombre)-4:len(nombre)] == ".hpp":
        return True
    return False

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

for i,filename in enumerate(filenames):
    if tiene_extension(filename, ".hpp"):
        newfilenames.append(filename[:-4] + ".h")
    else:
        newfilenames.append(filename)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]