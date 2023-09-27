import sys, json
import snowflake.snowpark as sp
#READ CREDS INTO DICTIONARY
with open("credentials.json") as jsonfile:
    creds = json.load(jsonfile)
    jsonfile.close()
#CREATE SESSION VARIABLE
session = sp.Session.builder.configs(creds).create()
#LOAD LOCAL VARS
sf_stage_name:str = "@STAGE_NAME"
upload_file:str = "FILE NAME"
#TRY TO PUT FILE
try:
    #PUT THE FILE
    put_results = session.file.put(
        local_file_name=upload_file,
        stage_location=sf_stage_name,
        overwrite=False,
        auto_compress=False)
    #PRINT THE RESULTS
    for r in put_results:
        str_output = ("File {src}: {stat}").format(src=r.source,stat=r.status)
        print(str_output)        
except Exception as e:
    #PRINT THE ERROR
    print(e)