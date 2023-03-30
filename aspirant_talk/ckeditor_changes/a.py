
def movefile():
    import os
    import shutil
    with open('a.txt','r') as firstfile, open('config.js','w+') as secondfile:
        # read content from first file
        for line in firstfile:

                 # append content to second file
                 secondfile.write(line)

    shutil.move("config.js", "workspace/.heroku/python/lib/python3.10/site-packages/ckeditor/static/ckeditor/ckeditor")
