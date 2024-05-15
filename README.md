# Required Classes -

from `junior.tablepdf` import `TableContentParser` as Parser

from `junior.tablepdf` import `Runner` as runner

# Parser Class -

parser = `Parser(name:str)`

!this `name` variable is important it will be the name of the pdf output file and also the raw value file name of the doc.


# .putKeysAndValues(heads:list,body:list) method —

`.putKeysAndValues(headings:list,body:list)`  - the `headings` and the `body` are the list values which will be the contents of the pdf file.

# Parsing values — 
Most important method to create PDF doccument.

`parse()` - it parses the values given in the `.putKeysAndValues(head:list,body:list)`

finally use the Runner class the create the PDF Documment.

# Runner Class - 
from `junior.tablepdf` import `Runner` as runner

`.run(name=None,orientation=None)`

•Note: this method is not static method.

`.run()` — method takes 2 argument `name` and `orientation`. 
`name` variable is takes the value given to the `@Parser()` class at the top, without this value the output cannot be created it will throw `"NoFileFound" or "FileNotFoundError`.


the `orientation` could be "L" for landscape or "P" for potrait.
or pass nothing and the PORTRAIT is default orientation of the PDF doc.


# Example -
from `junior.tablepdf` import `TableContentParser` as `Parser`


from `junior.tablepdf` import `Runner` as `runner`

parser=`Parser("my_first_pdf_in_python")`

parser.`putKeysAndValues(["Name","Age","Contact"],["JuniorXR","18","business.juniormail@gmail.com","JuniorXR","18","example@mail.com"])`

parser.`parse()`

runner().run("my_first_pdf_in_python")