
from __init__ import cursor, conn
from parent import Parent
import ipdb

Parent.drop_table()
Parent.create_table()


laura = Parent.create('Laura')
jeff = Parent.create('Jeff')

jeff.name = "Jeffereson"

jeff.update()



#ipdb.set_trace()


