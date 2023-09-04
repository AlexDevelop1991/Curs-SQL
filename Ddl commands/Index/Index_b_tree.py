"""CREATE {UNIQUE | BITMAP} INDEX
 schema.index_name ON
 schema.table_name(column1, column2,...);"""

"""По default  INDEX создётся B_TREE(NON UNIQUE, NOT NULL)"""

"""DROP INDEX schema.index_name"""

# CREATE INDEX in1 ON students (id);

# CREATE UNIQUE INDEX in2 ON students (name);

# CREATE INDEX in3 ON students (name, id);

#