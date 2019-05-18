from CreateMappingFiles import mapping_file_builder

def main():
    out= open("test.csv",'w')
    mapper=mapping_file_builder(out)
    mapper.addToModa("TEST1","teST2")
    mapper.addToModa("TEST1","teST2")
    mapper.addToModa("TEST3","teST3")
    mapper.writeMappings()
    out.close

if __name__ == '__main__':
    main()
