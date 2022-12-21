

CREATE TABLE "Biosample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	well_pos TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "BiosampleCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
