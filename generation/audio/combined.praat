## http://phonetics.linguistics.ucla.edu/facilities/acoustic/text_grid_maker.txt

# Here we define the directory
sound_directory$ = "/Users/sangheekim/Dropbox/01_Research/1__Project/Project_Exo/3_Material/4_Crossing-Boundary/01_Pronoun/audio/target/input/"

# This will create a list 
# with the names of the files in your folder:
# Create file list
Create Strings as file list: "fileList", sound_directory$ + "*.mp3"
numFiles = Get number of strings

# And this bit opens the files 
# with the names on the list that we created:
for ifile to numFiles
	select Strings fileList
	filename$ = Get string... ifile
	Read from file: sound_directory$ + filename$
	# This generates textgrids
	object_name$ = selected$ ("Sound")
	To TextGrid... "sentence words pauses"
	Write to text file... 'sound_directory$''object_name$'.TextGrid
endfor



# This creates a table called "data", 
# with 0 rows (Praat appends them later)
# and two columns.
# One column has the file name, 
# and the other one has the total duration
table_ID = Create Table with column names... data 0 File Duration

# And this bit opens the files 
# with the names on the list that we created:
for ifile to numFiles
	select Strings fileList
	filename$ = Get string... ifile
	Read from file: sound_directory$ + filename$
	# This fills in the table with rows with 
	# file names and the total file duration
	audio_len = Get total duration
	select table_ID
	Append row
	Set string value... ifile File 'filename$'
	Set numeric value... ifile Duration audio_len
endfor