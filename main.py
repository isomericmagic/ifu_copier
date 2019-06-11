def replicate_prt_sql(name, publication_id, placement_render_template_id):
    return """\n\n\t\t-- Begin Current Statement
    INSERT INTO PlacementRenderTemplate (
        RenderSelector,
        Template,
        Name,
        SupportedTemplates,
        VideoWidth,
        VideoHeight,
        DateUpdated,
        DateCreated,
        PublicationID,
        PublisherID,
        Type,
        Notes
        )
    SELECT
        RenderSelector,
        Template,
        '%s',
        SupportedTemplates,
        VideoWidth,
        VideoHeight,
        GETDATE(),
        GETDATE(),
        %s,
        PublisherID,
        Type,
        Notes
    FROM PlacementRenderTemplate
    WHERE PlacementRenderTemplateID = %s;

    """ % (name, publication_id, placement_render_template_id)

def read_file(fname):
        with open(fname, 'r') as f:
            return f.readlines()

def write_file(fname):
    #Create array to house all the CSV lines
    lines = read_file("CSVFile.csv") #This is the CSV file you're parsing
    headers = lines[0].strip('\n').split(',')
    print(headers)

    #Get the index of the arrays for each column (will be different for your specific CSV file) 
    ifu_name_index = headers.index("New IFU Name")
    publication_id_index = headers.index("PublicationID")
    ifu_id_index = headers.index("IFU ID to leverage")
    lines = lines[1:]

    #Open new SQL file to write to
    with open(fname, 'w') as f:
    #Loop through lines array from CSV, line by line
        for line in lines:
            line = line.strip('\n').split(',')
            f.write(replicate_prt_sql(
                line[ifu_name_index],
                line[publication_id_index],
                line[ifu_id_index]))

write_file("SQL_Output.sql")

print("You're Done!")